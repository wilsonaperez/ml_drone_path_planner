# planner/database.py

import sqlite3
import json

def init_db():
    conn = sqlite3.connect("drone_paths.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS paths (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT,
            total_energy REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_path(path, total_energy):
    path_json = json.dumps(path)  # store clean JSON
    conn = sqlite3.connect("drone_paths.db")
    c = conn.cursor()
    c.execute("INSERT INTO paths (path, total_energy) VALUES (?, ?)", (path_json, total_energy))
    conn.commit()
    conn.close()

def query_paths_by_energy(max_energy):
    conn = sqlite3.connect("drone_paths.db")
    c = conn.cursor()
    c.execute("SELECT * FROM paths WHERE total_energy <= ?", (max_energy,))
    results = c.fetchall()
    conn.close()
    return results
