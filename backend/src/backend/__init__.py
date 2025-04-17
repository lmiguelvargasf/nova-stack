from litestar import Litestar, get, asgi
from litestar.types import Receive, Scope, Send
from pydantic import BaseModel
from piccolo_admin.endpoints import create_admin, BaseUser

from .db import open_database_connection_pool, close_database_connection_pool


@asgi("/admin/", is_mount=True, copy_scope=False)
async def admin(scope: "Scope", receive: "Receive", send: "Send") -> None:
    await create_admin(tables=[BaseUser])(scope, receive, send)


class HealthStatus(BaseModel):
    status: str


@get("/health")
async def health_check() -> HealthStatus:
    return HealthStatus(status="ok")


app = Litestar(
    route_handlers=[admin, health_check],
    # Reference the imported functions
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)
