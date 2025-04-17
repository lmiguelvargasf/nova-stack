from piccolo.engine import engine_finder


async def open_database_connection_pool():
    """Starts the Piccolo database connection pool."""
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
        print("Database connection pool started.")
    except Exception as e:
        print(f"Failed to start database connection pool: {e}")
        raise


async def close_database_connection_pool():
    """Closes the Piccolo database connection pool."""
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
        print("Database connection pool closed.")
    except Exception as e:
        print(f"Error closing database connection pool: {e}")
        raise
