from loguru import logger
import re


def hide_sensitive_data(record):
    """
    Modify a log record to hide sensitive data.
    This function searches for specific patterns related to authorization,
    client ID, client secret, and password in a given log record and replaces
    the associated values with asterisks to mask the sensitive data
    """
    message = record["message"]
    message = re.sub(r'Authorization.*?,', '"Authorization": "********",', message)
    record["message"] = message
    return True


def setup_logger():
    """
    This function sets up the logger to output logs to a file named 'test_log.log'.
    The log format includes the timestamp in green, the logging level in white space-padded text, and the logger name,
    function name, and line number in cyan. The log message itself is displayed at the logging level's color.
    """
    log_format = ('{time:YYYY-MM-DD HH:mm:ss.SSSSSS} '
                  '| <level>{level: <8}</level> '
                  '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>')
    log_file = './reports/test_log.log'

    logger.remove()
    logger.add(sink=log_file, level='DEBUG', format=log_format, filter=hide_sensitive_data)

    return logger


log = setup_logger()

