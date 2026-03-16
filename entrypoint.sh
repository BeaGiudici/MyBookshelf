#!/bin/sh
set -e

if ! uv run python -c "
import psycopg2, os
conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'], host=os.environ['DB_HOST'], port=os.environ['DB_PORT'])
conn.close()
" 2>/dev/null; then
    echo "Database not found, initializing..."
    uv run python src/database/db.py
fi

exec uv run uvicorn src.api:app --host 0.0.0.0 --port 8000
