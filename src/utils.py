import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np
import dill

def save_object(file_path: str, obj: object):
    """
    Save an object to a file using dill.
    
    :param file_path: Path where the object will be saved.
    :param obj: The object to save.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(e, sys) from e