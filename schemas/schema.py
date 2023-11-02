from pydantic import BaseModel
from datetime import date

class VehicleSchema(BaseModel):
    idvehicle: int | None = None 
    name: str
    status: int
    type: str
    km: float
    function: str

class ClientSchema(BaseModel):
    idclient: int | None = None
    name: str
    phone: int
    email: str
    city: str
    neighborhood: str
    address: str
    kw: float

class EmployeeSchema(BaseModel):
    idemployee: int | None = None
    name: str
    phone: int
    email: str
    city: str
    neighborhood: str
    address: str
    salary: float

class CutSchema(BaseModel):
    idcut: int | None = None
    date: str
    hour: str
    city: str
    neighborhood: str