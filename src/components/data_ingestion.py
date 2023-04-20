import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer


@dataclass
class DataIngestionConfig:
    """
    A dataclass to define the file paths for the train, test, and raw data.
    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    """
    A class to perform data ingestion, by reading data from a CSV file,
    performing train-test split, and saving the train and test sets into separate CSV files.
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Initiates the data ingestion process by:
        1. Reading data from a CSV file.
        2. Creating necessary directories and saving raw data to a CSV file.
        3. Performing a train-test split on the input data.
        4. Saving the train and test sets into separate CSV files.

        :return: Tuple of train and test file paths.
        :raises CustomException: If there is an error during the data ingestion process.
        """
        logging.info("Entered the data ingestion method or component")

        try:
            # Modify the relative file path to be relative to the current directory
            # df = pd.read_csv(data_file_path)

            # TODO change this before final upload
            df = pd.read_csv(r'C:\Users\AkbarLutfullah\Documents\python-projects\mlproject\notebook\data\stud.csv')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error(f"Error ingesting data")
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_path=train_data_path, test_path=test_data_path)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_array=train_arr, test_array=test_arr))