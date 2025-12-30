# CARBON_FOOTPRINT_API_USING_ML

A RESTful API that predicts an individual's estimated carbon footprint using a machine learning model. This repository contains the model training code, API implementation, and instructions to run the service locally.

## Project Overview

This project provides an API that accepts user features and returns an estimated carbon footprint (in kg CO2e). It is intended for educational/demo purposes and can be extended for production use with additional validation, logging, monitoring, and security hardening.

## Features

- Predict carbon footprint using a trained machine learning model.
- Simple REST API for integration with web or mobile applications.
- Scripts for training and evaluating the model.

## Installation

1. Clone the repository:

   git clone https://github.com/Akshat77O/CARBON_FOOTPRINT_API_USING_ML.git
   cd CARBON_FOOTPRINT_API_USING_ML

2. (Recommended) Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows

3. Install dependencies:

   pip install -r requirements.txt

##  Machine Learning Approach

- **Problem Type:** Regression
- **Model Used:** Linear Regression
- **Features:**
  - Distance (km)
  - Package weight (kg)
  - Transport mode (road / air / sea)
  - Packaging type (cardboard / plastic / eco)
  - 
- **Target:** CO₂ emissions (kg)

The model is trained on **synthetic but realistic logistics data**, saved using `joblib`, and loaded for real-time inference via API.

## Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Geopy

### Frontend
- HTML
- CSS
- JavaScript

## Demo Screenshots
<img width="568" height="855" alt="image" src="https://github.com/user-attachments/assets/2fce6e13-503d-458f-a7e9-1e1881879010" />
<img width="561" height="872" alt="image" src="https://github.com/user-attachments/assets/bc02205b-d181-4b88-a151-a93d3abd3e3b" />

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with a clear description of changes. Include tests for new features or bug fixes where possible.


