import logging
import time


def apply_file_logger(file_name):
    logger = logging.getLogger("profile_scraper")
    logger.setLevel(logging.DEBUG)

    file_logger = logging.FileHandler(file_name)
    file_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')
    logging.Formatter.converter = time.gmtime
    file_logger.setFormatter(formatter)

    logger.addHandler(file_logger)
    return logger
