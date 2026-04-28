import sys
import requests
import time
import subprocess
from urllib.parse import quote
from qgis.core import QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, edit, QgsTask,QgsTaskManager,QgsApplication
from qgis.utils import iface
try:
 from PyQt6.QtGui import QColor
except ImportError:
 from PyQt5.QtGui import QColor

class OSMService:
    def __init__(self, email="QGIS_AI@example.com"):
        self.base_url = "https://nominatim.openstreetmap.org/search"
        self.headers = {
            'User-Agent': 'QGIS_Urban_Agent_PoC_Poyraz_Kaya_v1',
            'Referer': 'https://github.com/poyrazkaya/urban-agent'
        }
    def get_coordinate(self,place_name):
     time.sleep(1.1)
     safe_name = quote(place_name)
     url = f"{self.base_url}?q={safe_name}&format=json&limit=1"
     
     try:
         response = requests.get(url, headers=self.headers, timeout=10, verify=False)
         
         if response.status_code != 200:
             return {"error": f"HTTP {response.status_code}"}
             
         data = response.json()
         if not data:
             return {"error": "Place not found"}
             
         return {
             "lat": float(data[0]['lat']),
             "lon": float(data[0]['lon']),
             "display_name": data[0]['display_name']
         }
     except Exception as e:
         return {"error": str(e)}

class qgis_tools:
 def layer_renderer(self,layer_name,lon,lat):
     project = QgsProject.instance()
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
              layer.updateExtents() 
              QgsProject.instance().addMapLayer(layer)
            # Check if the feature was actually accepted
              if not layer.addFeature(feat):
               layer.triggerRepaint()
            iface.mapCanvas().refresh()
            return "işlem tamamlandı"
        
 def list_active_layers(*args, **kwargs) -> str:
  all_layers = list(QgsProject.instance().mapLayers().values())
  if not all_layers:
    return "there is not active layer in this project"
  else:
    layer_names = [layer.name() for layer in all_layers]
    return f"The active layers are: {', '.join(layer_names)}"
 def add_point_by_name(self,place_name: str, layer_name: str = "AI_Points") -> str:
    osm = OSMService()
    result = osm.get_coordinate(place_name)
    
    if not result or "lat" not in result:
        return f"Could not find coordinates for '{place_name}'"

    try:
        # 2. CRITICAL: Convert strings to floats immediately
        # PyQGIS will fail silently if these stay as strings
        lon = float(result["lon"])
        lat = float(result["lat"])

        # 3. Access QGIS through the instance
       
        return f"Successfully added {place_name} at ({lat}, {lon}) to layer '{layer_name}'"

    except Exception as e:
        # This will catch PyQGIS specific errors (like Thread errors)
        return f"PyQGIS Error: {str(e)}" 
# 
def run(self,tool_name, *args, **kwargs):
    task = QgsTask.fromFunction('MCP_server_task', tool_name,on_finished=completed, wait_time=4)
    QgsApplication.taskManager().addTask(task)
    iface.mapCanvas().refreshAllLayers()
def completed():
   return "finished" 