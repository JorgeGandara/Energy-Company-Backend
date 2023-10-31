from fastapi import FastAPI
from routers.vehicle import router as VehicleRouter

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "/docs"}

app.include_router(VehicleRouter)