from loguru import logger
from piccolo.engine import engine_finder


async def open_database_connection_pool():
    """Start database connection pool."""
    engine = engine_finder()
    try:
        await engine.start_connection_pool() # type: ignore[union-attr]
        logger.info("Database connection pool started.")
    except AttributeError:
        logger.exception("No Piccolo engine found. Cannot start connection pool.")
        raise RuntimeError("Database engine not configured")
    except Exception as e:
        logger.exception(f"Failed to start database connection pool: {e}")
        raise


async def close_database_connection_pool():
    """Close database connection pool."""
    engine = engine_finder()
    try:
        await engine.close_connection_pool() # type: ignore[union-attr]
        logger.info("Database connection pool closed.")
    except AttributeError:
        logger.warning("No Piccolo engine found. Cannot close connection pool.")
    except Exception as e:
        logger.exception(f"Error closing database connection pool: {e}")
        raise
