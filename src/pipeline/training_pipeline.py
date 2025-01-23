import pandas as pd

from src.data.data_ingestion import DataIngestion
from src.data.data_transformation import DataTransformation
from src.data.model_trainer import ModelTrainer
from src.data.model_evaluation import ModelEvaluation


obj=DataIngestion()

obj.fetch_and_save_data()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(obj.data_config.train_data_path,obj.data_config.test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)