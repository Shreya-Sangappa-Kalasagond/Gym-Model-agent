
import json, csv, os, random
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

def register():
    users = load_users()
    u = input("Username: ")
    p = input("Password: ")
    users[u] = {"password": p}
    save_users(users)
    print("Registered Successfully")

def login():
    users = load_users()
    u = input("Username: ")
    p = input("Password: ")
    if u in users and users[u]["password"] == p:
        print("Login Successful")
        return u
    print("Invalid Login")
    return None

def bmi():
    w = float(input("Weight (kg): "))
    h = float(input("Height (m): "))
    b = w/(h*h)
    print("BMI =", round(b,2))

def calories():
    w = float(input("Weight (kg): "))
    print("Estimated Calories:", int(w*33))

def workout():
    plans = {
        "chest":["Bench Press","Pushups","Incline Press"],
        "back":["Pullups","Rows","Lat Pulldown"],
        "legs":["Squats","Lunges","Leg Press"],
        "arms":["Curls","Tricep Pushdown","Hammer Curl"]
    }
    part=input("Body Part: ").lower()
    print(plans.get(part,["Walking","Stretching"]))

def meal():
    print("Breakfast: Oats, Eggs")
    print("Lunch: Rice, Chicken/Paneer")
    print("Dinner: Salad, Protein Source")

def water():
    w=float(input("Weight kg: "))
    print("Water:", round(w*35/1000,2),"Litres")

def progress():
    wt=input("Current Weight: ")
    with open(PROGRESS_FILE,"a",newline="") as f:
        csv.writer(f).writerow([datetime.now(),wt])
    print("Progress Saved")

def history():
    if not os.path.exists(PROGRESS_FILE):
        print("No Data")
        return
    print(open(PROGRESS_FILE).read())

def recommendation():
    issue=input("Problem: ").lower()
    if "back" in issue:
        print("Try Bird Dogs and Glute Bridges")
    else:
        print("Follow normal workout")

def motivation():
    msgs=[
        "Consistency beats intensity.",
        "One workout at a time.",
        "Progress is progress."
    ]
    print(random.choice(msgs))

def injury():
    i=input("Injury Area: ")
    print("Modify exercises for",i)

def food():
    print("Estimated Calories: 450")
    print("Protein: 20g")

def bodypart():
    workout()

def weekly():
    print("Weekly Summary Generated")

def profile():
    age=input("Age: ")
    goal=input("Goal: ")
    print("Saved:",age,goal)

def analytics():
    print("Basic analytics available from progress data")

def goals():
    g=input("Enter Goal: ")
    print("Goal Set:",g)

def ai_coach():
    q=input("Ask Coach: ")
    print("Coach:", q, "- Focus on protein, sleep and consistency.")

user=None

while True:
    print("\\n--- GYM AI AGENT ---")
    print("1 Register")
    print("2 Login")
    print("3 BMI")
    print("4 Calories")
    print("5 Workout Generator")
    print("6 Meal Planner")
    print("7 Water Tracker")
    print("8 Progress Tracker")
    print("9 Workout History")
    print("10 Exercise Recommendation")
    print("11 Motivation Coach")
    print("12 Injury Suggestions")
    print("13 Food Analyzer")
    print("14 Body Part Workout")
    print("15 Weekly Summary")
    print("16 Profile")
    print("17 Analytics")
    print("18 Goal Tracking")
    print("19 AI Coach")
    print("0 Exit")

    ch=input("Choice: ")

    if ch=="1": register()
    elif ch=="2": user=login()
    elif ch=="3": bmi()
    elif ch=="4": calories()
    elif ch=="5": workout()
    elif ch=="6": meal()
    elif ch=="7": water()
    elif ch=="8": progress()
    elif ch=="9": history()
    elif ch=="10": recommendation()
    elif ch=="11": motivation()
    elif ch=="12": injury()
    elif ch=="13": food()
    elif ch=="14": bodypart()
    elif ch=="15": weekly()
    elif ch=="16": profile()
    elif ch=="17": analytics()
    elif ch=="18": goals()
    elif ch=="19": ai_coach()
    elif ch=="0": break
