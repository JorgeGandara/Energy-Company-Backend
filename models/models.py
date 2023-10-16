from pydantic import BaseModel

class Person(BaseModel):
    id: int = 123
    name: str = "Jorge Gandara"
    phone: int = 1234567890
    email: str = "gandaraj@utb.edu.co"