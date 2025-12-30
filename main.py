from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from utils.distance import calculate_distance

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model
model = joblib.load("model/carbon_model.pkl")

@app.get("/calculate")
def calculate(
    weight: float,
    origin: str,
    destination: str,
    transport: str,
    packaging: str
):
    distance = calculate_distance(origin, destination)

    input_df = pd.DataFrame([{
        "distance": distance,
        "weight": weight,
        "transport": transport,
        "packaging": packaging
    }])

    co2 = model.predict(input_df)[0]

    eco_score = "High" if co2 < 20 else "Medium" if co2 < 50 else "Low"

    return {
        "distance_km": distance,
        "co2_kg": round(co2, 2),
        "eco_score": eco_score
    }
