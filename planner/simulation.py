# planner/simulation.py

import numpy as np
import pandas as pd

def simulate_drone_energy_data(num_samples=5000, seed=42):
    """
    Simulate drone flight data for ML training.
    """
    np.random.seed(seed)
    speeds = np.random.uniform(0, 15, num_samples)          # m/s
    accelerations = np.random.uniform(-5, 5, num_samples)   # m/s^2
    altitudes = np.random.uniform(0, 100, num_samples)      # m

    # Power model: P = k1*v^2 + k2*|a| + k3*h
    k1, k2, k3 = 0.2, 0.5, 0.05
    power = k1 * speeds**2 + k2 * np.abs(accelerations) + k3 * altitudes

    df = pd.DataFrame({
        "speed": speeds,
        "acceleration": accelerations,
        "altitude": altitudes,
        "power": power
    })

    df.to_csv("data/simulated_drone_energy.csv", index=False)
    print(f"Simulated dataset saved to data/simulated_drone_energy.csv")
