from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio
from contextlib import AsyncExitStack
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
    # Calling a tool
    async def call_tool(self, tool_name, args: dict, **kwargs):
        return await self._sess.call_tool(tool_name, args, **kwargs)
async def main():
    
    async with MyClientSession("http://localhost:8000/mcp") as session:
        tools = await session.call_tool("calculate_sum", {'a': 7, 'b':9})
        # tools = await session.list_tools()
        print(tools, "tools")
        # for tool in tools:
        #   print(tools)
asyncio.run(main())
   