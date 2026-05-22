#!/bin/sh
set -e

echo "Waiting for PostgreSQL..."
until python -c "
import asyncio
import asyncpg
import os
async def check():
    conn = await asyncpg.connect(
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres'),
        database=os.environ.get('DB_NAME', 'boardmate'),
        host=os.environ.get('DB_HOST', 'db'),
        port=int(os.environ.get('DB_PORT', '5432')),
    )
    await conn.close()
asyncio.run(check())
" 2>/dev/null; do
  sleep 2
done

if [ "${INIT_DB:-false}" = "true" ]; then
  echo "Initializing database..."
  python -m app.main db
fi

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
