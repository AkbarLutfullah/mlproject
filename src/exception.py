import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message by extracting information from the given error and error detail.

    :param error: The error message.
    :param error_detail: The sys.exc_info() object containing exception details.
    :return: A formatted error message containing the file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    """
    A custom exception class that extends the built-in Python Exception class.

    It provides a more detailed error message, containing the file name, line number, and error message.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the custom exception with a given error message and error detail.

        :param error_message: The error message.
        :param error_detail: The sys.exc_info() object containing exception details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the custom error message as a string.

        :return: The custom error message.
        """
        return self.error_message

