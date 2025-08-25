# from contextlib import asynccontextmanager
# @asynccontextmanager
# async def conection(name: str):
#     print(f"Connecting to {name}...")
#     yield name
#     print(f"connected {name}...")
    

# async def main():
#     async with conection("mcp_client") as name:
#         print(f"Using connection: {name}")
# asyncio.run(main())
    
import asyncio
from contextlib import AsyncExitStack

async def get_connection(name):
    class ctx():
        async def __aenter__(self):
            print(f"Connecting to {name}...")
            return name
# from contextlib import asynccontextmanager
        
        async def __aexit__(self,exc_type, exc_val, exc_tb):
            print(f"Existing {name}...")
    return ctx()

async def main():
    async with await get_connection("A") as a:
        async with await get_connection("B") as b:
           print(f"Using connection: {a} and {b}")
async def main():
    async with AsyncExitStack() as stack:
        a = await stack.enter_async_context(await get_connection("A"))
        if a == "A":
            b = await stack.enter_async_context(await get_connection("B"))
            print(f"Using connection: {a} and {b}")
        async def customcleanup():
            print("Custom cleanup logic here")
        stack.push_async_callback(customcleanup)
        print(f"doing work with {a} and maybe {locals().get("b")}")
        
asyncio.run(main())       
 