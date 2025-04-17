from piccolo.engine import engine_finder


async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
        print("Database connection pool started.")
    except Exception as e:
        print(f"Error starting database connection pool: {e}")
        # Optionally re-raise or handle more gracefully depending on requirements
        # raise


async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
        print("Database connection pool closed.")
    except Exception as e:
         print(f"Error closing database connection pool: {e}")
         # Optionally re-raise or handle more gracefully
         # raise 