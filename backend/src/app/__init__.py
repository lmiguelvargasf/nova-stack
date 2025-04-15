from litestar import Litestar, get

@get("/")
async def get_root() -> str:
    return "Hello, World!"

app = Litestar(route_handlers=[get_root])
