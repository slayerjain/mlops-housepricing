import numpy as np
import pandas as pd

import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    url:str='https://raw.githubusercontent.com/connectaditya/House-price-prediction/refs/heads/master/USA_Housing.csv'

class DataIngestion:
    def __init__(self):
        self.data_config=DataIngestionConfig()

    def fetch_and_save_data(self):
        data = pd.read_csv(self.data_config.url)
        
        os.makedirs("artifacts",exist_ok=True)
        
        data.to_csv(self.data_config.raw_data_path,index=False)
        
        train_data,test_data=train_test_split(data,test_size=0.25)
        
        train_data.to_csv(self.data_config.train_data_path,index=False)
        test_data.to_csv(self.data_config.test_data_path,index=False)
