from mcp.server.fastmcp import FastMCP
mcp = FastMCP(name="fist_prac", stateless_http=True)

@mcp.tool(name="researcher")
def search_online(query:str):
    return f"result for{ query}"
    
@mcp.tool()
def get_weather(city:str):
    
    return f"weather in {city}"

mcp_server = mcp.streamable_http_app()