from fastmcp import FastMCP
from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, edit
import subprocess
from qgis.utils import iface
from PyQt5.QtGui import QColor
from .osm import OSMService

mcp_server = FastMCP("qgis_mcp_server" )
osm = OSMService()
#get the python version
@mcp_server.tool
def python_version():
    version = subprocess.check_output(["python", "--version"], text=True)
    return str(version)
# get the system info
@mcp_server.tool
def get_sys_info(): 
 info = subprocess.check_output(["neofetch", "--off"], text=True)
 return str(info)
@mcp_server.tool
def list_active_layers() -> str:
  all_layers = list(QgsProject.instance().mapLayers().values())
  if not all_layers:
   return "there is not active layer in this project"
  else:
    return str(all_layers)
@mcp_server.tool()
def add_point_by_name(place_name: str, layer_name: str = "AI_Points") -> str:
    # 1. Get the coordinates (We already know this part works)
    result = osm.get_coordinate(place_name)
    
    if not result or "lat" not in result:
        return f"Could not find coordinates for '{place_name}'"

    try:
        # 2. CRITICAL: Convert strings to floats immediately
        # PyQGIS will fail silently if these stay as strings
        lon = float(result["lon"])
        lat = float(result["lat"])

        # 3. Access QGIS through the instance
        project = QgsProject.instance()
        
        # 4. Find or Create the layer
        layers = project.mapLayersByName(layer_name)
        if layers:
            layer = layers[0]
        else:
            # URI must define the CRS to be valid
            uri = "Point?crs=EPSG:4326"
            layer = QgsVectorLayer(uri, layer_name, "memory")
            if not layer.isValid():
                return "Failed to create a valid QGIS memory layer."
            project.addMapLayer(layer)

        # 5. Add the feature with an explicit edit session
        with edit(layer):
            feat = QgsFeature(layer.fields())
            feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(lon, lat)))
            
            # Check if the feature was actually accepted
            if not layer.addFeature(feat):
                return f"QGIS layer refused the feature for '{place_name}'"

        # 6. Force the UI to show the new point
        layer.triggerRepaint()
        iface.mapCanvas().refresh()
        
        return f"Successfully added {place_name} at ({lat}, {lon}) to layer '{layer_name}'"

    except Exception as e:
        # This will catch PyQGIS specific errors (like Thread errors)
        return f"PyQGIS Error: {str(e)}"