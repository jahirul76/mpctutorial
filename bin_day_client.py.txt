import asyncio
from fastmcp import Client


client = Client("http://localhost:8000/mcp")

async def call_tool(postcode: str):
    async with client:
        result = await client.call_tool("find_council", {"postcode": postcode})
        print(result)

asyncio.run(call_tool("HA9 7NS"))



async def call_tool2(council: str):
    async with client:
        result = await client.call_tool("get_bin_collection_day", {"council": council})
        print(result)

asyncio.run(call_tool2("brent"))

