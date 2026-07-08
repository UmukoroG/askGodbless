import hashlib
import base64
import html
import secrets
import time
from urllib.parse import urlencode, urlparse

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.requests import Request

from .config import CLIENT_ID, ALLOWED_REDIRECT_ORIGINS
from .store import _auth_codes, _access_tokens, purge_expired

router = APIRouter()


@router.get("/.well-known/oauth-authorization-server")
async def oauth_metadata(request: Request):
    base = str(request.base_url).rstrip("/")
    return {
        "issuer": base,
        "authorization_endpoint": f"{base}/oauth/authorize",
        "token_endpoint": f"{base}/oauth/token",
        "response_types_supported": ["code"],
        "grant_types_supported": ["authorization_code"],
        "code_challenge_methods_supported": ["S256"],
    }


@router.get("/.well-known/oauth-protected-resource")
async def oauth_protected_resource(request: Request):
    base = str(request.base_url).rstrip("/")
    return {"resource": base, "authorization_servers": [base]}


@router.get("/oauth/authorize", response_class=HTMLResponse)
async def oauth_authorize(
    response_type: str,
    client_id: str,
    redirect_uri: str,
    code_challenge: str,
    code_challenge_method: str = "S256",
    state: str = "",
):
    if client_id != CLIENT_ID:
        raise HTTPException(status_code=400, detail="Unknown client_id")

    parsed = urlparse(redirect_uri)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    if origin not in ALLOWED_REDIRECT_ORIGINS:
        raise HTTPException(status_code=400, detail="Invalid redirect_uri")

    e = html.escape
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Authorize Claude.ai — askGodbless</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 480px; margin: 80px auto; padding: 0 1rem; }}
    h1 {{ font-size: 1.4rem; }}
    .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 1.5rem; }}
    button {{ background: #0066cc; color: #fff; border: none; padding: .6rem 1.4rem;
              border-radius: 6px; font-size: 1rem; cursor: pointer; }}
    button:hover {{ background: #0052a3; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Authorize Claude.ai</h1>
    <p>Claude.ai is requesting access to your <strong>askGodbless</strong> MCP server.</p>
    <form method="post" action="/oauth/approve">
      <input type="hidden" name="client_id"             value="{e(client_id)}">
      <input type="hidden" name="redirect_uri"          value="{e(redirect_uri)}">
      <input type="hidden" name="code_challenge"        value="{e(code_challenge)}">
      <input type="hidden" name="code_challenge_method" value="{e(code_challenge_method)}">
      <input type="hidden" name="state"                 value="{e(state)}">
      <button type="submit">Authorize</button>
    </form>
  </div>
</body>
</html>""")


@router.post("/oauth/approve")
async def oauth_approve(request: Request):
    form = await request.form()
    client_id      = form.get("client_id", "")
    redirect_uri   = form.get("redirect_uri", "")
    code_challenge = form.get("code_challenge", "")
    state          = form.get("state", "")

    code = secrets.token_urlsafe(32)
    _auth_codes[code] = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_challenge": code_challenge,
        "expires_at": time.time() + 600,
    }
    params = {"code": code, **({"state": state} if state else {})}
    return RedirectResponse(f"{redirect_uri}?{urlencode(params)}", status_code=302)


@router.post("/oauth/token")
async def oauth_token(request: Request):
    purge_expired()
    form = await request.form()
    grant_type    = form.get("grant_type")
    code          = form.get("code", "")
    code_verifier = form.get("code_verifier", "")

    if grant_type != "authorization_code":
        return JSONResponse({"error": "unsupported_grant_type"}, status_code=400)

    code_data = _auth_codes.pop(code, None)
    if not code_data or code_data["expires_at"] < time.time():
        return JSONResponse({"error": "invalid_grant"}, status_code=400)

    digest   = hashlib.sha256(code_verifier.encode()).digest()
    expected = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
    if expected != code_data["code_challenge"]:
        return JSONResponse({"error": "invalid_grant"}, status_code=400)

    token = secrets.token_urlsafe(32)
    _access_tokens[token] = {"expires_at": time.time() + 3600}
    return {"access_token": token, "token_type": "bearer", "expires_in": 3600}
