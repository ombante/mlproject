import logging 
import os 
from datetime import datetime
import colorlog

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# File handler (no colors)
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Console handler (with colors)
console_handler = colorlog.StreamHandler()
console_formatter = colorlog.ColoredFormatter(
    "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
    }
)
console_handler.setFormatter(console_formatter)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, console_handler]
)

