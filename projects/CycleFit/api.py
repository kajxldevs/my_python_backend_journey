from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all your modules
from auth import Signup, Login
from user_profile import user
from bmi import CalculateBMI
from Cycle import Phase as GetCyclePhase
from Workout import GetPlan
from mood import SaveMood, LoadMoods
from pydantic import BaseModel

app = FastAPI()

# This allows your frontend to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CycleFit API is running"}



class SignupData(BaseModel):
    username: str
    password: str

@app.post("/signup")
def signup(data: SignupData):
    result = Signup(data.username, data.password)
    return {"message": result}

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginData):
    result = Login(data.username, data.password)
    return {"message": result}

@app.get("/cycle")
def cycle_phase(period_date: str):
    day, phase = GetCyclePhase(period_date)
    return {"day": day, "phase": phase}

@app.get("/bmi")
def bmi(weight: float, height: float):
    bmi_val, category = CalculateBMI(weight, height)
    return {"bmi": round(bmi_val, 1), "category": category}

@app.get("/workout")
def workout(phase: str, equipment: str, body_part: str):
    plan = GetPlan(phase, equipment, body_part)
    return {"exercises": plan}

@app.get("/workout")
def workout(phase: str, equipment: str, body_part: str):
    plan = GetPlan(phase.capitalize(), equipment.capitalize(), body_part.capitalize())
    return {"exercises": plan}


class MoodData(BaseModel):
    mood: str
    energy: int

@app.post("/mood")
def save_mood(data: MoodData):
    SaveMood(data.mood, data.energy)
    return {"message": "Mood saved successfully!"}

@app.get("/moods")
def get_moods():
    return {"moods": LoadMoods()}