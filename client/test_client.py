"""MCP test client — exercises the hello tool over stdio."""
import asyncio
import logging

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

logging.basicConfig(level=logging.INFO)


async def test_hello_tool():
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "server.main"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            logging.info("Available tools: %s", [t.name for t in tools.tools])

            result = await session.call_tool("hello", {"name": "Godbless"})
            logging.info("Result: %s", result.content[0].text)

            result2 = await session.call_tool("hello", {"name": "World"})
            logging.info("Result: %s", result2.content[0].text)


if __name__ == "__main__":
    asyncio.run(test_hello_tool())
