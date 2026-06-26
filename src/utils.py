import logging

logging.basicConfig(
    filename="logs/preprocessing.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(message):
    logging.info(message)

#Call 
from utils import log_message

log_message("Dataset loaded successfully")
log_message("Outliers removed")
log_message("Features engineered")
