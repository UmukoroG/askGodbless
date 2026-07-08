from fastapi import APIRouter, Depends
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from starlette.requests import Request

from ..auth import require_token
from .tools import mcp_server

session_manager = StreamableHTTPSessionManager(app=mcp_server, stateless=True)

router = APIRouter()


@router.api_route("/mcp", methods=["GET", "POST", "DELETE"])
async def handle_mcp(request: Request, _=Depends(require_token)):
    await session_manager.handle_request(request.scope, request.receive, request._send)
