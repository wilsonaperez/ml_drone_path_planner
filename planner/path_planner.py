# planner/path_planner.py

import numpy as np
from planner.ml_predictor import load_energy_predictor

def plan_energy_efficient_path(start, goal, model, grid_size=(50, 50)):
    """
    Simple energy-aware greedy planner on a grid for demonstration.
    """
    path = [list(start)]
    current = np.array(start)
    goal = np.array(goal)

    while not np.all(current == goal):
        step = np.sign(goal - current)
        next_pos = current + step

        # Features for prediction
        speed = np.linalg.norm(step) * 5  # approximate speed
        acceleration = 0  # simplified
        altitude = 10  # flat altitude

        predicted_power = model.predict([[speed, acceleration, altitude]])[0]
        print(f"Step: {tuple(int(i) for i in next_pos)}, Predicted Power: {predicted_power:.2f} W")

        # ✅ Append clean next position as list of ints
        path.append([int(i) for i in next_pos])
        current = next_pos

    return path
