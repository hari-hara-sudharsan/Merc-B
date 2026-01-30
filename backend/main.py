from fastapi import FastAPI
from schemas import OnboardingInput
from db import init_db, save_user, fetch_report
from graph import onboarding_graph

app = FastAPI()

init_db()

@app.post("/onboarding")
def onboarding(data: OnboardingInput):
    user_data = data.dict()
    user_id = save_user(user_data)

    user_data["user_id"] = user_id
    report = onboarding_graph.invoke(user_data)

    return {
        "user_id": user_id,
        "report": report
    }

@app.get("/report/{user_id}")
def get_report(user_id: int):
    return fetch_report(user_id)
from chat import chat_with_ai

@app.post("/chat")
def chat(prompt: str):
    return {"response": chat_with_ai(prompt)}
