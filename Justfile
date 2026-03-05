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
    @uv run src/main.py

# Database reset
[group("database")]
reset-database:
    @uv run src/main.py --reset

# Fake entries creation
[group("fake-entries")]
populate-fake:
    @uv run src/fake_entries.py