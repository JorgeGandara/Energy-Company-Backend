import json
from fastapi import APIRouter
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "../data/data_active.json"), "r") as f:
    data = json.load(f)

router = APIRouter()

@router.get("/active")
async def get_active():
    return data 

@router.get("/active/{id}")
async def get_active(id: int):
    return list(filter(lambda item: item["id"] == id,  data)) 

@router.post("/active")
async def create_active(active: dict = data):
    data.append(active)
    return data

@router.put("/active/{id}")
async def update_active(id: int, active: dict):
    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i] = active
    return data

@router.delete("/active/{id}")
async def delete_active(id: int):
    data.remove(list(filter(lambda item: item["id"] == id,  data))[0])
    return data