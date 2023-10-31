from pydantic import BaseModel

class VehicleSchema(BaseModel):
    idvehicle: int | None = None 
    name: str
    status: int
    type: str
    km: float
    function: str