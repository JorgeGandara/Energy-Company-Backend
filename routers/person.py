import json
from fastapi import APIRouter
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "../data/data_person.json"), "r") as f:
    data = json.load(f)

router = APIRouter()

@router.get("/person")
async def get_person():
    return data 

@router.get("/person/{id}")
async def get_person(id: int):
    return list(filter(lambda item: item["id"] == id,  data)) 

@router.post("/person")
async def create_person(person: dict = data):
    data.append(person)
    return data

@router.put("/person/{id}")
async def update_person(id: int, person: dict):
    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i] = person
    return data

@router.delete("/person/{id}")
async def delete_person(id: int):
    data.remove(list(filter(lambda item: item["id"] == id,  data))[0])
    return data