import os
import sys
from pathlib import Path
from loguru import logger

def setup_logging() -> None:
    logger.remove()
    
    log_dir = os.getenv("LOG_DIR", "var/logs")
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    logger.add(str(Path(log_dir) / "app.log"), serialize=True, level="INFO", rotation="10 MB", retention="7 days", compression="gz")
    logger.add(sys.stdout, serialize=True, level="INFO")

def get_logger(name: str) -> logger:
    return logger.bind(name=name)