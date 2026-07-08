import contextlib

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .mcp.transport import session_manager
from .oauth.config import CLIENT_ID
from .oauth.routes import router as oauth_router
from .mcp.transport import router as mcp_router


@contextlib.asynccontextmanager
async def lifespan(app):
    async with session_manager.run():
        yield


app = FastAPI(lifespan=lifespan)
app.include_router(oauth_router)
app.include_router(mcp_router)


@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>askGodbless MCP Server</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 560px; margin: 80px auto; padding: 0 1rem; }}
    code {{ background: #f0f0f0; padding: .2rem .5rem; border-radius: 4px; font-size: 1rem; }}
  </style>
</head>
<body>
  <h1>askGodbless MCP Server</h1>
  <p>To connect from Claude.ai:</p>
  <ol>
    <li>Add a custom connector with URL: <code>https://askgodbless.fly.dev/mcp</code></li>
    <li>When prompted for an OAuth Client ID, enter: <code>{CLIENT_ID}</code></li>
    <li>Click <strong>Authorize</strong> when the sign-in page appears</li>
  </ol>
</body>
</html>""")
