from fastapi import FastAPI
from routers.vehicle import router as VehicleRouter
from routers.client import router as ClientRouter
from routers.employee import router as EmployeeRouter
from routers.cut import router as CutRouter

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "/docs"}

app.include_router(ClientRouter, prefix="/client", tags=["client"])
app.include_router(EmployeeRouter, prefix="/employee", tags=["employee"])
app.include_router(VehicleRouter, prefix="/vehicle", tags=["vehicle"])
app.include_router(CutRouter, prefix="/cut", tags=["cut"])