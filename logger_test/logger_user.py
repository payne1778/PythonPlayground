import logging

logger = logging.getLogger(__name__)


def create_file(path):
    logger.info("Creating file %s", path)
    try:
        with open(path, "w") as f:
            f.write(f"hello from {path}")
        logger.info("Successfully created %s", path)
    except Exception:
        logger.exception("Failed to create %s", path)
