from mcp.server import Server
from mcp.types import Tool, TextContent

mcp_server = Server("askme")


@mcp_server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="hello",
            description="Say hello to someone by name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "The name of the person to greet"}
                },
                "required": ["name"],
            },
        )
    ]


@mcp_server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "hello":
        return [TextContent(type="text", text=f"Hello, {arguments.get('name')}!")]
    raise ValueError(f"Unknown tool: {name}")
