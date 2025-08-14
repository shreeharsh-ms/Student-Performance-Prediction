import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score

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

def evaluate_model(x_train, y_train, x_test, y_test, models):
    """
    Evaluate multiple regression models and return their performance metrics.
    
    :param x_train: Training feature set.
    :param y_train: Training target variable.
    :param x_test: Testing feature set.
    :param y_test: Testing target variable.
    :param models: Dictionary of model names and instances to evaluate.
    
    :return: Dictionary with model names as keys and their R2 scores as values.
    """
    try:
        model_report = {}
        for model_name, model in models.items():
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            r2_square = r2_score(y_test, y_pred)
            model_report[model_name] = r2_square
            logging.info(f"{model_name} R2 score: {r2_square}")
        return model_report
    except Exception as e:
        raise CustomException(e, sys) from e