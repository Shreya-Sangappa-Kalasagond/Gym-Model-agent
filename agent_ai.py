import streamlit as st
import json
import os
import csv
import random
from datetime import datetime

USERS_FILE = "users.json"
PROGRESS_FILE = "progress.csv"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register(username, password):
    users = load_users()
    users[username] = {"password": password}
    save_users(users)

def login(username, password):
    users = load_users()
    return username in users and users[username]["password"] == password

st.title("🏋️ Gym AI Agent")

menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "Register",
        "Login",
        "BMI Calculator",
        "Calories",
        "Workout Generator",
        "Meal Planner",
        "Water Tracker",
        "Progress Tracker",
        "Motivation Coach",
        "AI Coach"
    ]
)

if menu == "Register":
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Register"):
        register(u, p)
        st.success("Registered Successfully")

elif menu == "Login":
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(u, p):
            st.success("Login Successful")
        else:
            st.error("Invalid Login")

elif menu == "BMI Calculator":
    w = st.number_input("Weight (kg)", 1.0)
    h = st.number_input("Height (m)", 0.5)

    if st.button("Calculate BMI"):
        bmi = w / (h * h)
        st.success(f"BMI = {bmi:.2f}")

elif menu == "Calories":
    w = st.number_input("Weight (kg)", 1.0)

    if st.button("Estimate Calories"):
        st.info(f"Estimated Calories: {int(w*33)}")

elif menu == "Workout Generator":
    plans = {
        "Chest":["Bench Press","Pushups","Incline Press"],
        "Back":["Pullups","Rows","Lat Pulldown"],
        "Legs":["Squats","Lunges","Leg Press"],
        "Arms":["Curls","Tricep Pushdown","Hammer Curl"]
    }

    part = st.selectbox("Body Part", list(plans.keys()))

    if st.button("Generate Workout"):
        st.write(plans[part])

elif menu == "Meal Planner":
    st.write("Breakfast: Oats, Eggs")
    st.write("Lunch: Rice, Chicken/Paneer")
    st.write("Dinner: Salad, Protein Source")

elif menu == "Water Tracker":
    w = st.number_input("Weight (kg)", 1.0)

    if st.button("Calculate Water"):
        st.success(f"{round(w*35/1000,2)} Litres/day")

elif menu == "Progress Tracker":
    wt = st.number_input("Current Weight", 1.0)

    if st.button("Save Progress"):
        with open(PROGRESS_FILE, "a", newline="") as f:
            csv.writer(f).writerow([datetime.now(), wt])
        st.success("Progress Saved")

elif menu == "Motivation Coach":
    msgs = [
        "Consistency beats intensity.",
        "One workout at a time.",
        "Progress is progress."
    ]
    if st.button("Motivate Me"):
        st.success(random.choice(msgs))

elif menu == "AI Coach":
    q = st.text_input("Ask Coach")

    if st.button("Get Advice"):
        st.write(
            f"Coach: {q}\n\nFocus on protein, sleep and consistency."
        )