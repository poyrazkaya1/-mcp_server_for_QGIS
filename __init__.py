import sys
import os
import threading
import logging
# --- 1. ENVIRONMENT SETUP ---
LOG_FILE = os.path.join(os.path.dirname(__file__), "urban_agent.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w' # 'w' overwrites every time you restart QGIS
)
logger = logging.getLogger("UrbanAgent")
def setup_environment():
    plugin_dir = os.path.dirname(__file__)
    # Check for both .venv and venv
    venv_names = [".venv", "venv"]
    site_packages_path = None   
    for name in venv_names:
        venv_lib_dir = os.path.join(plugin_dir, name, "lib")
        if os.path.exists(venv_lib_dir):
            # Find the python3.x folder
            subdirs = [d for d in os.listdir(venv_lib_dir) if d.startswith("python")]
            if subdirs:
                path = os.path.join(venv_lib_dir, subdirs[0], "site-packages")
                if os.path.exists(path):
                    site_packages_path = path
                    break

    if site_packages_path:
        if site_packages_path not in sys.path:
            sys.path.insert(0, site_packages_path)
        print(f"Urban Agent: Environment linked at {site_packages_path}")
        logger.info("venv path found")
        return True
    else:
        print("Urban Agent: CRITICAL ERROR - No virtual environment found!")
        logger.error("venv path not found")
        return False

# Run setup immediately on load
ENV_READY = setup_environment()

# --- 2. PLUGIN CLASS ---
class UrbanAgent:
    def __init__(self, iface):
        self.iface = iface
        self.server_thread = None

    def initGui(self):
        if not ENV_READY:
            print("Urban Agent: Server not started because environment is missing.")
            return

        def run_server():
            try:
                # Import inside the thread to ensure it sees the updated sys.path
                from .mcp_qgis import mcp_server
                
                print("Urban Agent: Starting MCP Server on port 8000...")
                # host="0.0.0.0" is essential for LM Studio to connect on Linux
                mcp_server.run(transport="sse",host="0.0.0.0",port=8888)
                logger.info("mcp server start")
            except Exception as e:
                print(f"Urban Agent Server Error: {e}")
                logger.error(f"mcp server cannot start {e}")

        # daemon=True ensures the thread closes when QGIS closes
        self.server_thread = threading.Thread(target=run_server, daemon=True)
        self.server_thread.start()
        print("Urban Agent: Background thread initialized.")
        logger.info("mcp server starts without problem")
          
    def unload(self):
        print("Urban Agent: Unloaded.")
        logger.info("plugn closed")

# --- 3. QGIS FACTORY ---
def classFactory(iface):
    return UrbanAgent(iface)