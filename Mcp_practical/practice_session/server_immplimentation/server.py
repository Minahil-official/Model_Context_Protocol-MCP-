from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="practice_session",stateless_http =True)

@mcp.tool()
def calculate(a: int, b: int) -> int:
    return a + b    

mcp_app = mcp.streamable_http_app()