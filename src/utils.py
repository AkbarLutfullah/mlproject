import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Saves a given object to a file at the specified file path.

    :param file_path: The path where the object should be saved.
    :param obj: The object to be saved.
    :raises CustomException: If there is an error during the saving process.
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
