from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "MCP Practical Server",stateless_http = True)

docs = {
    "title": "MCP Practical Server",
   'info': "This is a practical implementation of MCP server with tools and resources.",
   'guidelines': "Use the tools and resources wisely.",
   'readme': "This server is for practical purposes only.",
}
@mcp.resource("docs://documents")
def list_docs():
    """list all available docs"""
    return list(docs.keys())
print("Available docs:", list_docs())


@mcp.resource("docs://documents/{doc_name}",mime_type="application/json")
def read_doc(doc_name: str):
    """Read a specific doc by name."""
    return docs.get(doc_name, "Document not found.")
    
mcp_server = mcp.streamable_http_app()
