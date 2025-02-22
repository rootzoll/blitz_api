from app.auth.auth_bearer import JWTBearer
from fastapi.security import HTTPAuthorizationCredentials


def monkeypatch_auth(monkeypatch):
    async def fake__call__(self, request):
        return HTTPAuthorizationCredentials(scheme="Bearer", credentials="creds")

    monkeypatch.setattr(JWTBearer, "__call__", fake__call__)
