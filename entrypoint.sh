#!/bin/sh
set -e

uv run python src/database/db.py
exec uv run uvicorn src.api:app --host 0.0.0.0 --port 8000
