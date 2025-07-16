# app.py

import streamlit as st
from planner.ml_predictor import load_energy_predictor
from planner.path_planner import plan_energy_efficient_path
from planner.database import init_db, insert_path, query_paths_by_energy
import json

st.title("🚁 Energy-Efficient Drone Path Planner")

init_db()
model = load_energy_predictor()

start = st.text_input("Start position (x,y):", "0,0")
goal = st.text_input("Goal position (x,y):", "10,10")

if st.button("Plan Path"):
    start_tuple = tuple(map(int, start.split(",")))
    goal_tuple = tuple(map(int, goal.split(",")))
    path = plan_energy_efficient_path(start_tuple, goal_tuple, model)

    # Estimate total energy
    total_energy = sum(
        model.predict([[5, 0, 10]])[0] for _ in path
    )
    insert_path(path, total_energy)
    st.success(f"Path planned with estimated total energy: {total_energy:.2f} W")
    st.write("Planned Path:")
    st.json(path)

st.header("🔍 Query Paths by Energy")
max_energy = st.slider("Max total energy (W)", 0, 500, 100)

if st.button("Query Paths"):
    results = query_paths_by_energy(max_energy)
    if results:
        for r in results:
            path_json = r[1]
            path_list = json.loads(path_json)
            st.write(f"ID: {r[0]}, Total Energy: {r[2]:.2f} W")
            st.json(path_list)
    else:
        st.info("No paths found within this energy limit.")
