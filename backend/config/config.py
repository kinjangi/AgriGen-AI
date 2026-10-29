import logging
from config.settings import settings

def setup_logging():
    """Configures standard logging for the backend application."""
    logging.basicConfig(
        level=logging.DEBUG if settings.DEBUG else logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(settings.PROJECT_NAME)
    return logger

logger = setup_logging()
