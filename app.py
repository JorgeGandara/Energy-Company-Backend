# Github & Azure DevOps Remote postgresqlconn branch
# App v1.0.0

from fastapi import FastAPI
from routers.vehicle import router as VehicleRouter
from routers.client import router as ClientRouter
from routers.employee import router as EmployeeRouter
from routers.cut import router as CutRouter
from routers.state import router as StateRouter
from routers.building import router as BuildingRouter
from routers.generator import router as GeneratorRouter

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "/docs"}

app.include_router(ClientRouter, prefix="/client", tags=["Client"])
app.include_router(EmployeeRouter, prefix="/employee", tags=["Employee"])
app.include_router(CutRouter, prefix="/cut", tags=["Cut"])
app.include_router(StateRouter, prefix="/state", tags=["State"])
app.include_router(VehicleRouter, prefix="/vehicle", tags=["Vehicle"])
app.include_router(BuildingRouter, prefix="/building", tags=["Building"])
app.include_router(GeneratorRouter, prefix="/generator", tags=["Generator"])