import logging
from logging.handlers import RotatingFileHandler

# Setup logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

# Rotating file handler
handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

# Logging examples
logger.info("This is an info message.")
logger.error("This is an error message.")

# 🔹 Loop to generate many logs (for testing rotation)
for i in range(200000):
    logger.info(f"Log message number {i}")
