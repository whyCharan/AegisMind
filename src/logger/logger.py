import os 
from datetime import datetime
import logging

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"AegisMind_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    filemode='a'
)

logger = logging.getLogger("AegisMind")
