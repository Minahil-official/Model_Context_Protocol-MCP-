from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MCP Server", stateless_http = True)


@mcp.tool()
async def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two integers."""
    return a + b

mcp_app = mcp.streamable_http_app()

