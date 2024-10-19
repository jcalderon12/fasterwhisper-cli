import logging

def configure_logger():
    """
    Configures the logger and returns it

    Returns:
        logger: logger used to display messages by console
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("fasterwhisper-cli")
    return logger