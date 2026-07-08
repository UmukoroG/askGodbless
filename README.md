# askGodbless MCP Server

A personal MCP (Model Context Protocol) server for Godbless Umukoro, deployed at `https://askgodbless.fly.dev`. Connect it to Claude to query tools over the web.

## Project Structure

```
server/
├── app.py            # FastAPI app, lifespan, setup page
├── auth.py           # Bearer token guard
├── main.py           # uvicorn entry point
├── oauth/
│   ├── config.py     # CLIENT_ID, allowed redirect origins
│   ├── store.py      # in-memory token/code stores
│   └── routes.py     # OAuth 2.0 + PKCE endpoints
└── mcp/
    ├── tools.py      # MCP tool definitions (add new tools here)
    └── transport.py  # Streamable HTTP session manager + /mcp route

client/
└── test_client.py    # MCP test client
```

## Stack

- **Python 3.12**
- **FastAPI** + **uvicorn** — HTTP server
- **MCP SDK 1.28** — Streamable HTTP transport
- **OAuth 2.0 + PKCE** — auth for Claude.ai connector
- **Fly.io** — deployment
- **Docker** — containerisation
- **uv** — dependency management

## Connecting from Claude

**Claude Desktop or claude.ai:**
1. Add a custom connector with URL: `https://askgodbless.fly.dev/mcp`
2. Enter OAuth Client ID: `askgodbless-claude`
3. Click **Authorize** when the sign-in page appears

## Local Development

```bash
uv sync
uvicorn server.app:app --reload --port 8000
```

## Deploy

```bash
fly deploy
```

## Adding Tools

All tools live in `server/mcp/tools.py`. Add a new `@mcp_server.list_tools()` entry and a matching branch in `call_tool`.

## Current Tools

| Tool | Description |
|------|-------------|
| `hello` | Returns a greeting for a given name |
