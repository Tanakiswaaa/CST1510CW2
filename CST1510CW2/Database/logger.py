import logging

LOG_PATH = "system.log"
logging.basicConfig(
    filename="LOG_PATH",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message: str, level: str = "info"):
    if level.lowe() == "error":
        logging.error(message)
    elif level.lower() == "warning":
        logging.warning(message)
    else:
    logging.info(message)
