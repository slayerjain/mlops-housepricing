import argparse
import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logging import logging
from src.utils.utils import load_object


def predict(features) -> pd.DataFrame:
    try:
        preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
        model_path=os.path.join("artifacts","model.pkl")

        preprocessor=load_object(preprocessor_path)
        model=load_object(model_path)

        scaled_fea=preprocessor.transform(features)    
        pred=model.predict(scaled_fea)

        return pred

    except Exception as e:
        raise customexception(e,sys)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict house price based on features")
    parser.add_argument("--income", type=float, required=True, help="Avg. Area Income")
    parser.add_argument("--house_age", type=float, required=True, help="Avg. Area House Age")
    parser.add_argument("--num_rooms", type=float, required=True, help="Avg. Area Number of Rooms")
    parser.add_argument("--num_bedrooms", type=float, required=True, help="Avg. Area Number of Bedrooms")
    parser.add_argument("--population", type=float, required=True, help="Area Population")
    parser.add_argument("--address", type=str, required=True, help="Address (Categorical Column)")

    args = parser.parse_args()

    # Create DataFrame including categorical columns
    data = {
        "Avg. Area Income": [args.income],
        "Avg. Area House Age": [args.house_age],
        "Avg. Area Number of Rooms": [args.num_rooms],
        "Avg. Area Number of Bedrooms": [args.num_bedrooms],
        "Area Population": [args.population],
        "Address": [args.address]  # Categorical Feature
    }

    features_df = pd.DataFrame(data)

    pred = predict(features_df)
    print(f"Predicted House Price: {pred[0]}")