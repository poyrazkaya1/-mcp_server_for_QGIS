from fastmcp import FastMCP
import time
from .tools import OSMService,qgis_tools

mcp_server = FastMCP("qgis_mcp_server" )
osm = OSMService()
qgis = qgis_tools()

@mcp_server.tool
def get_layer_info(ctx=None):
 return qgis.list_active_layers(ctx)
time.sleep(3)
pass


@mcp_server.tool
def add_point(place,layer): 
 return qgis.add_point_by_name(place,layer)
time.sleep(3)
pass



