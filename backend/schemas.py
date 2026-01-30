from pydantic import BaseModel

class OnboardingInput(BaseModel):
    name: str
    idea: str
    target_users: str
    region: str = "Kerala"
