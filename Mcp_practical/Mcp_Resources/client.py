from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession,types
import asyncio
from contextlib import AsyncExitStack
from typing import Any
from pydantic import AnyUrl
import json
# initialization and state management
class MyClientSession:
    def __init__(self, url):
        self.url = url
        self.stack = AsyncExitStack()
        self._sess = None #due to this none if there is no session it will be visibl
        # super().__init__(url, headers=headers)
    async def list_tools(self):
        async with self.session as session:
            response = (await session.list_tools()).tools 
            return response
    async def __aenter__(self):
        read, write,_ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )
        self._sess = await self.stack.enter_async_context(
            ClientSession(read,write)
        )
        await self._sess.initialize()
        return self
    async def __aexit__(self, exc_type, exc, tb):
        await self.stack.aclose()  
    async def list_tools(self):
        return (await self._sess.list_tools()).tools
    # # Calling a tool
    # async def call_tool(self, tool_name, args: dict, **kwargs):
    #     return await self._sess.call_tool(tool_name, args, **kwargs)
    async def list_resources(self)-> list[types.Resource]:
        result:types.ListResourcesResult = await self._sess.list_resources()
        return result.resources
    
    async def list_resource_templates(self)-> list[types.ResourceTemplate]:
        result:types.ListResourceTemplatesResult = await self._sess.list_resource_templates()
        # print("result", result.__dict__)
        return result.resourceTemplates 
    
    async def read_resource(self, uri:str)-> types.ReadResourceResult:
        assert self._sess , "Session not initialized. Use 'async with' to initialize."
        _urls = AnyUrl(uri)
        result= await self._sess.read_resource(AnyUrl(_urls))
        # print("result", result.__dict__)
        resource = result.contents[0]
        if isinstance(resource,types.TextResourceContents):
            if resource.mimeType == "application/json":
                try:
                    return json.loads(resource.text)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        return resource.text
async def main():
    
    async with MyClientSession("http://localhost:8000/mcp") as session:
        # tools = await session.call_tool("calculate_sum", {'a': 7, 'b':9})
        # tools = await session.list_tools()
        # print(tools, "tools")
        # # for tool in tools:
        # #   print(tools)
        # resources = await session.list_resources()
        # print(resources, "resources")
        # read_resource = await session.read_resource("docs://documents")
        # print(read_resource, "read_resource")
        templates = await session.list_resource_templates()
        # print(templates, "templates")
        for template in templates:
            print(f'resource template: {template.uriTemplate},')
            # print(f"data: {template.text},")
            data = await session.read_resource(template.uriTemplate.replace("{doc_name}","info"))
            print("data", {data})
asyncio.run(main())
   