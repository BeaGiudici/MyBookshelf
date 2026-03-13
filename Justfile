set windows-shell := ["powershell.exe", "-c"]
set shell := ["bash", "-c"]
export PYTHONPATH := "."

set dotenv-load

# Show commands
list:
    @just --list --unsorted

# Setup environment and dependencies
[group("setup")]
setup:
    @uv sync

# Database creation
[group("database")]
create-database:
    @uv run src/database/db.py

# Database reset
[group("database")]
reset-database:
    @uv run src/database/db.py --reset

# Fake entries creation
[group("fake-entries")]
populate-fake:
    @uv run src/utils/fake_entries.py

# API
[group("api")]
run-api:
    @uv run uvicorn src.api:app --reload --host 0.0.0.0 --port 8000

# -------------------------
# Code quality
# -------------------------

# Lint code with ruff (auto-fix enabled)
[group("code-quality")]
lint:
    @uv run ruff check . --fix

# Format code with ruff formatter
[group("code-quality")]
format:
    @uv run ruff format .

# Type check (default target: src/)
[group("code-quality")]
type-check target=".":
    @uvx typing check {{target}}