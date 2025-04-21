from litestar import Litestar, asgi, get
from litestar.types import Receive, Scope, Send
from piccolo_admin.endpoints import create_admin
from piccolo.apps.user.tables import BaseUser
from pydantic import BaseModel

from .db import close_database_connection_pool, open_database_connection_pool


@asgi("/admin/", is_mount=True, copy_scope=False)
async def admin(scope: Scope, receive: Receive, send: Send) -> None:
    await create_admin(tables=[BaseUser])(scope, receive, send) # type: ignore[arg-type]


class HealthStatus(BaseModel):
    status: str


@get("/health")
async def health_check() -> HealthStatus:
    return HealthStatus(status="ok")


app = Litestar(
    route_handlers=[admin, health_check],
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)
