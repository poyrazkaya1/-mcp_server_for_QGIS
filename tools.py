import requests
import time
from urllib.parse import quote


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
    def tool():
        print("qgis_deneme") 