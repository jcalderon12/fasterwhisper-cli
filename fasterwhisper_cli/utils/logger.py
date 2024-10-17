import logging

def configure_logger():
    """
    Configures the logger and returns it

    Returns:
        logger: logger used to display messages by console
    """
    logging.basicConfig()
    logger = logging.getLogger("fasterwhisper_cli").setLevel(logging.INFO)
    return logger