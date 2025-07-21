# 🚁 Energy-Efficient Drone Path Planner

This project demonstrates an **end-to-end pipeline** combining:
✅ **Robotics (simulation and control).**  
✅ **Machine Learning (energy prediction).**  
✅ **SQL (path logging and querying).**  
✅ **Streamlit (frontend demo).**  
✅ **Git-structured, production-ready design.**

## Features
- Simulate drone paths in a 2D environment.
- Predict energy consumption using a trained ML model.
- Plan energy-efficient paths.
- Log paths and energy in a SQL database.
- Query paths by energy constraints.
- Visualize and manage everything in a Streamlit app.

## Getting Started
```bash
pip install -r requirements.txt
python -m planner.simulation  # to generate data
python -m planner.ml_predictor  # to train ML model
streamlit run app.py
