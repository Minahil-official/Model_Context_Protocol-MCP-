from mcp import ClientSession
import asyncio
class MyClientSession(ClientSession):
    def __init__(self, url, headers=None):
        self.session = ClientSession(url)
        # super().__init__(url, headers=headers)
    async def list_tools(self):
        async with self.session as session:
            response = (await session.list_tools()).tools 
            return response
        
        
async def main():
    async with MyClientSession("http://localhost:8000") as session:
        tools = await session.list_tools()
        for tool in tools:
          print(tools)
asyncio.run(main())
  