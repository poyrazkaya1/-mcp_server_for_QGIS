from fastmcp import FastMCP
import time
from .tools import OSMService,qgis_tools

mcp_server = FastMCP("qgis_mcp_server" )
osm = OSMService()
qgis = qgis_tools()

@mcp_server.tool
def get_layer_info():
 return qgis.run(qgis.list_active_layers())
time.sleep(3)
pass

@mcp_server.tool
def add_point(place,layer): 
 qgis.run(qgis.add_point_by_name(place,layer))
 lon = qgis.add_point_by_name(lon)
 lat  = qgis.add_point_by_name(lat)
 layer_name = qgis.add_point_by_name(layer_name)
 return qgis.layer_renderer(layer_name,lon,lat)
time.sleep(3)
pass



