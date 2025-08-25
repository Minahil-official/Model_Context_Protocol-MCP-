from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="second_class",stateless_http=True)

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}
# @mcp.tool()
# def greeting(name: str) -> str:
#     """
#     A simple greeting tool that returns a greeting message.
    
#     Args:
#         name (str): The name of the person to greet.
        
#     Returns:
#         str: A greeting message.
#     """
#     return f"Hello, {name}!"
# TODO: Write a tool to read a doc
@mcp.tool()
async def read_doc(doc_id: str) -> str:
    """
    Reads the content of a document by its ID.
    
    Args:
        doc_id (str): The ID of the document to read.
        
    Returns:
        str: The content of the document.
    """
    return docs.get(doc_id, "Document not found.")             
# TODO: Write a tool to edit a doc
@mcp.tool()
async def edit_doc(doc_id: str, content: str) -> str:
    """
    Edits the content of a document by its ID.
    
    Args:
        doc_id (str): The ID of the document to edit.
        content (str): The new content for the document.
        
    Returns:
        str: A confirmation message indicating the document has been edited.
    """
    if doc_id in docs:
        docs[doc_id] = content
        return f"Document {doc_id} has been updated."
    else:
        return "Edit succesfully."
# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


mcp_app = mcp.streamable_http_app()