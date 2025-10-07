from fastapi import FastAPI
from joblib import load
import joblib
from pydantic import BaseModel
import numpy as np
from pathlib import Path
import uvicorn
import json


app = FastAPI()

model_path = "models/model.joblib"
model = joblib.load(model_path)

class Inputs(BaseModel):
    
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.get('/health')
async def home():
    return 'working fine!'

@app.post('/predict')
async def predict(inputs: Inputs):
    print(type(Inputs))
    dict_inputs = inputs.model_dump()
    features = [value for key,value in dict_inputs.items()]
    prediction = model.predict([features])[0].item()
    return prediction


if __name__ == "__main__":
    uvicorn.run('app:app',host='0.0.0.0',port=8000,reload=True)



    