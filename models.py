import sqlite3

# Create database connection
conn = sqlite3.connect("agriculture.db")
cursor = conn.cursor()

# ================= TABLES =================

cursor.execute("""
CREATE TABLE IF NOT EXISTS crop_details (
    crop TEXT PRIMARY KEY,
    n REAL NOT NULL,
    p REAL NOT NULL,
    k REAL NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    ph REAL NOT NULL,
    rainfall REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rain_info (
    state TEXT PRIMARY KEY,
    january REAL NOT NULL,
    february REAL NOT NULL,
    march REAL NOT NULL,
    april REAL NOT NULL,
    may REAL NOT NULL,
    june REAL NOT NULL,
    july REAL NOT NULL,
    august REAL NOT NULL,
    september REAL NOT NULL,
    october REAL NOT NULL,
    november REAL NOT NULL,
    december REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS msp_details (
    crop TEXT PRIMARY KEY,
    year2010 INTEGER NOT NULL,
    year2011 INTEGER NOT NULL,
    year2012 INTEGER NOT NULL,
    year2013 INTEGER NOT NULL,
    year2014 INTEGER NOT NULL,
    year2015 INTEGER NOT NULL,
    year2016 INTEGER NOT NULL,
    year2017 INTEGER NOT NULL,
    year2018 INTEGER NOT NULL,
    year2019 INTEGER NOT NULL,
    year2020 INTEGER NOT NULL,
    year2021 INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    api_token TEXT NOT NULL,
    auth_key TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS personal_model (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api_token TEXT NOT NULL,
    model_name TEXT NOT NULL,
    recommendation_model TEXT NOT NULL,
    labelencoder_model TEXT NOT NULL,
    yield_model TEXT NOT NULL,
    crops TEXT NOT NULL,
    state TEXT NOT NULL,
    city TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully using pure Python.")