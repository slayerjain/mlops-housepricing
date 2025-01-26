import os
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.logger.logging import logging
from src.exception.exception import customexception
from src.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initialize_data_transformation(self, train_path: str, test_path: str):
        """
        Reads training and testing datasets, preprocesses the data, and saves the preprocessor object.

        Parameters:
        - train_path: str : Path to the training dataset.
        - test_path: str : Path to the testing dataset.

        Returns:
        - train_arr: np.ndarray : Preprocessed training data.
        - test_arr: np.ndarray : Preprocessed testing data.
        """
        try:
            # Load the datasets
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Successfully read train and test datasets.")

            # Log dataset heads
            logging.info(f'Train Dataframe Head:\n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head:\n{test_df.head().to_string()}')

            # Define target column and input features
            target_column_name = 'Price'
            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            # Identify categorical and numerical columns
            categorical_columns = input_feature_train_df.select_dtypes(include=['object']).columns.tolist()
            numerical_columns = input_feature_train_df.select_dtypes(exclude=['object']).columns.tolist()

            # Define the preprocessor
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', StandardScaler(), numerical_columns),
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
                ]
            )

            logging.info("Fitting and transforming datasets with the preprocessor.")

            # Apply transformations
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df).toarray()
            input_feature_test_arr = preprocessor.transform(input_feature_test_df).toarray()

            # Reshape target features
            target_feature_train_arr = target_feature_train_df.values.reshape(-1, 1)
            target_feature_test_arr = target_feature_test_df.values.reshape(-1, 1)

            # Combine features and targets
            train_arr = np.c_[input_feature_train_arr, target_feature_train_arr]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_arr]

            # Save the preprocessor object
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )
            logging.info("Preprocessor object saved successfully.")

            return train_arr, test_arr

        except Exception as e:
            logging.error("An error occurred during data transformation.")
            raise customexception(e, sys)
