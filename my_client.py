import asyncio
from fastmcp import Client


client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Jahirul"))

async def list_tools():
    async with client:
        tools = await client.list_tools()
        # tools -> list[mcp.types.Tool]
        
        for tool in tools:
            print(f"Tool: {tool.name}")
            print(f"Description: {tool.description}")
            if tool.inputSchema:
                print(f"Parameters: {tool.inputSchema}")
            # Access tags and other metadata
            if hasattr(tool, 'meta') and tool.meta:
                fastmcp_meta = tool.meta.get('_fastmcp', {})
                print(f"Tags: {fastmcp_meta.get('tags', [])}")


asyncio.run(list_tools())


async def list_resources():
    async with client:
        resources = await client.list_resources()
        # resources -> list[mcp.types.Resource]
        
        for resource in resources:
            print(f"Resource URI: {resource.uri}")
            print(f"Name: {resource.name}")
            print(f"Description: {resource.description}")
            print(f"MIME Type: {resource.mimeType}")
            
            if hasattr(resource, '_meta') and resource._meta:
                fastmcp_meta = resource._meta.get('_fastmcp', {})
                print(f"Tags: {fastmcp_meta.get('tags', [])}")
               


asyncio.run(list_resources())