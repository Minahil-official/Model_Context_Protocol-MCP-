from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio
from contextlib import AsyncExitStack

class MyClientSession:
    def __init__(self, url):
        self.url = url
        self.stack = AsyncExitStack()
        self._sess = None
        
    async def list_tools(self):
        async with self.session as session:
            response = (await session.list_tools()).tools 
            return 
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
        
    # async def list_tools(self):
    #     return (await self._sess.list_tools()).tools
    
    async def call_tool(self, tool_name, *args, **kwargs):
        return await self._sess.call_tool(tool_name, *args, **kwargs)
    
async def main():
    async with MyClientSession("http://localhost:8000/mcp") as session:
        tools = await session.call_tool('hello', {'name': 'Hashim'})
        print(tools, "tools")

asyncio.run(main())