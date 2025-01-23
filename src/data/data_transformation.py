import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
from src.utils.utils import save_object
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')
                        
            target_column_name = 'Price'
            drop_columns = [target_column_name]
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            # Identify categorical columns
            categorical_columns = input_feature_train_df.select_dtypes(include=['object']).columns.tolist()
            numerical_columns = input_feature_train_df.select_dtypes(exclude=['object']).columns.tolist()
            
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', StandardScaler(), numerical_columns),
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
                ]
            )
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            # Fit & transform the train set
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df).toarray()
            input_feature_test_arr = preprocessor.transform(input_feature_test_df).toarray()
            
            # Convert target variable to 2D array
            target_feature_train_df = np.array(target_feature_train_df).reshape(-1, 1)
            target_feature_test_df = np.array(target_feature_test_df).reshape(-1, 1)

            # Ensure array shapes match before concatenation
            train_arr = np.c_[input_feature_train_arr, target_feature_train_df]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_df]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            