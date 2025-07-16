# planner/ml_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_energy_predictor(data_path="data/simulated_drone_energy.csv", model_path="drone_energy_model.pkl"):
    """
    Train an ML model to predict energy consumption.
    """
    df = pd.read_csv(data_path)
    X = df[["speed", "acceleration", "altitude"]]
    y = df["power"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print(f"Model training complete. Test R^2: {model.score(X_test, y_test):.2f}")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def load_energy_predictor(model_path="drone_energy_model.pkl"):
    """
    Load the trained energy prediction model.
    """
    return joblib.load(model_path)
