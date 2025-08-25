from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="client_immpli", stateless_http=True)

@mcp.tool()
async def hello(name: str):
    """Say hello to someone."""
    return f"Hello {name}!"

mcp_app = mcp.streamable_http_app()