import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def call_top_headlines(query: str):
    async with client:
        result = await client.call_tool("top_headlines", {"query": query})
        print(result)


async def call_everything(query: str):
    async with client:
        result = await client.call_tool("everything", {"query": query})
        print(result)


asyncio.run(call_top_headlines("bitcoin"))
asyncio.run(call_everything("united states"))
