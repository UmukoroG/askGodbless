import os

CLIENT_ID = os.environ.get("MCP_CLIENT_ID", "askgodbless-claude")
PUBLIC_URL = os.environ.get("PUBLIC_URL", "https://askgodbless.onrender.com")

ALLOWED_REDIRECT_ORIGINS = {
    "https://claude.ai",
    "https://claude.anthropic.com",
}
