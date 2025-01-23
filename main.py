import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
from src.pipeline.predict_pipeline import predict as predict_price

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/",response_class=HTMLResponse)
def serve_homepage():
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content) 
class Features(BaseModel):
    income: float
    house_age: float
    num_rooms: float
    num_bedrooms: float
    population: float
    address: str

@app.post("/predict")
def predict(features: Features):
    features_dict = {
        "Avg. Area Income": [features.income],
        "Avg. Area House Age": [features.house_age],
        "Avg. Area Number of Rooms": [features.num_rooms],
        "Avg. Area Number of Bedrooms": [features.num_bedrooms],
        "Area Population": [features.population],
        "Address": [features.address]
    }
    
    features_df = pd.DataFrame(features_dict)
    prediction = predict_price(features_df)
    return {"price": prediction[0]}    