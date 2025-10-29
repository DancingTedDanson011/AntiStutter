"""
Logging utilities for AntiStutter
"""

import logging
import sys
from pathlib import Path
from datetime import datetime

class Logger:
    """Custom logger for AntiStutter"""

    def __init__(self, name="AntiStutter", log_dir=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Remove existing handlers
        self.logger.handlers = []

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)

        # File handler
        if log_dir is None:
            log_dir = Path.home() / ".antistutter" / "logs"
        else:
            log_dir = Path(log_dir)

        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"antistutter_{datetime.now().strftime('%Y%m%d')}.log"

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_format)
        self.logger.addHandler(file_handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

# Global logger instance
logger = Logger()
