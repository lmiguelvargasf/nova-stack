from litestar import Litestar, get
from piccolo.engine import engine_finder


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

@get("/")
async def get_root() -> str:
    return "Hello, World!"

app = Litestar(
    route_handlers=[get_root],
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)
