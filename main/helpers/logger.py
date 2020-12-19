""" Module which contains the logger of my application. """
# Python libs.
import logging
# Project files.
from .main_config import CONFIGURATION


class Logger:
    """ Logger class. """

    def get_logger(self, module_name):
        """
        Set up logging and return logger name.
        
        :param str module_name: Module's name, from which logger is called.
        """

        logger = logging.getLogger(f"app:{module_name}")
        logger.setLevel(CONFIGURATION.level)

        # Create & save to file.
        file_handler = logging.FileHandler(CONFIGURATION.file_path)
        file_handler.setFormatter(logging.Formatter(CONFIGURATION.format))

        logger.addHandler(file_handler)

        return logger
