from piccolo.engine import engine_finder
from loguru import logger


async def open_database_connection_pool():
    """Start database connection pool."""
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
        logger.info("Database connection pool started.")
    except Exception as e:
        logger.exception(f"Failed to start database connection pool: {e}")
        raise


async def close_database_connection_pool():
    """Close database connection pool."""
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
        logger.info("Database connection pool closed.")
    except Exception as e:
        logger.exception(f"Error closing database connection pool: {e}")
        raise
