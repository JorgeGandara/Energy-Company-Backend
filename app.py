from fastapi import FastAPI
from models.models import Person

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/person")
async def create_person(person: Person):
    return person