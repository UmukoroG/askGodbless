import os

CLIENT_ID = os.environ.get("MCP_CLIENT_ID", "askgodbless-claude")

ALLOWED_REDIRECT_ORIGINS = {
    "https://claude.ai",
    "https://claude.anthropic.com",
}
