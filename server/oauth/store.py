import time

_auth_codes: dict[str, dict] = {}
_access_tokens: dict[str, dict] = {}


def purge_expired() -> None:
    now = time.time()
    for k in [k for k, v in _auth_codes.items() if v["expires_at"] < now]:
        del _auth_codes[k]
    for k in [k for k, v in _access_tokens.items() if v["expires_at"] < now]:
        del _access_tokens[k]
