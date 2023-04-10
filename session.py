from starlette.applications import Starlette
from starlette.middleware.sessions import SessionMiddleware

app = Starlette()

app.add_middleware(
    SessionMiddleware,
    secret_key="my-secret-key",
    session_cookie="my-session-cookie",
    max_age=3600,  # 1 hour
    cookie_path="/myapp",
    cookie_domain=".example.com",
    secure=True,
    httponly=True,
    prefix="myapp_",
)
