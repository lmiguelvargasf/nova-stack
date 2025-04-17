from litestar import Litestar, get, asgi
from litestar.types import Receive, Scope, Send
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin, BaseUser



@asgi("/admin/", is_mount=True, copy_scope=False)
async def admin(scope: "Scope", receive: "Receive", send: "Send") -> None:
    await create_admin(tables=[BaseUser])(scope, receive, send)


async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

app = Litestar(
    route_handlers=[admin, health],
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)
