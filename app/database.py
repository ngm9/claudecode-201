import asyncpg
import asyncio
from typing import Optional

_DB_POOL: Optional[asyncpg.pool.Pool] = None

async def get_pool():
    global _DB_POOL
    if _DB_POOL is None:
        for _ in range(10):
            try:
                _DB_POOL = await asyncpg.create_pool(
                    database="shopflow",
                    user="shopuser",
                    password="shoppass",
                    host="postgres",
                    port=5432,
                    min_size=1,
                    max_size=20
                )
                break
            except Exception:
                await asyncio.sleep(2)
        else:
            raise RuntimeError("Could not connect to PostgreSQL after retries.")
    return _DB_POOL

async def get_conn():
    pool = await get_pool()
    return await pool.acquire()

async def release_conn(conn):
    pool = await get_pool()
    await pool.release(conn)
