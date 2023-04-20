import logging
import os
from datetime import datetime

"""
This module sets up a basic logging configuration to log messages throughout the application.

A log file is created with a timestamp in its name, and it is stored in the "logs" folder.
Messages are logged with the following format: [ timestamp ] line_number module_name - log_level - message

The default log level is set to INFO.
"""

# create log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

