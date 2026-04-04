import logging
import os

os.makedirs("artifacts", exist_ok=True)

logging.basicConfig(
    filename="artifacts/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

def get_logger():
    return logging