import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Generate synthetic dataset
np.random.seed(42)
data_size = 500

data = pd.DataFrame({
    "distance": np.random.randint(50, 3000, data_size),
    "weight": np.random.uniform(0.5, 50, data_size),
    "transport": np.random.choice(["road", "air", "sea"], data_size),
    "packaging": np.random.choice(["cardboard", "plastic", "eco"], data_size)
})

# Emission logic (hidden from model)
transport_factor = {"road": 0.12, "air": 0.6, "sea": 0.04}
packaging_factor = {"cardboard": 1.0, "plastic": 1.3, "eco": 0.7}

data["co2"] = (
    data["distance"]
    * data["weight"]
    * data["transport"].map(transport_factor)
    * data["packaging"].map(packaging_factor)
    / 100
)

X = data.drop("co2", axis=1)
y = data["co2"]

# Preprocessing
categorical_features = ["transport", "packaging"]
numerical_features = ["distance", "weight"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

model.fit(X, y)

joblib.dump(model, "carbon_model.pkl")

print("✅ ML Model trained and saved successfully")
