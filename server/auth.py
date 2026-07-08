import time

from fastapi import HTTPException
from starlette.requests import Request

from .oauth.store import _access_tokens


def require_token(request: Request) -> None:
    auth = request.headers.get("authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = auth.removeprefix("Bearer ")
    entry = _access_tokens.get(token)
    if not entry or entry["expires_at"] < time.time():
        raise HTTPException(status_code=401, detail="Invalid or expired token")
