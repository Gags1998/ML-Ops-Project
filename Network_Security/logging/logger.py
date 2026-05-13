from logging import getLogger, StreamHandler, Formatter, INFO
from datetime import datetime
import logging
import os

LOG_FILE = f"/exception/logs/log_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"
LOG_Path = os.path.join(os.getcwd(), LOG_FILE)
os.makedirs(os.path.dirname(LOG_Path), exist_ok=True)
 
LOG_FILE_PATH = os.path.join(LOG_Path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=LOG_FILE_PATH,
)