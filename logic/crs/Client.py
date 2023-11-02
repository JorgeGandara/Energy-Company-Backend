from .Person import Person

class Client(Person):
    def __init__(self, id: int = 0, name: str = "Name", phone: int = 0, email: str = "name@domain", city: str = "City", neigborhood: str = "neigborhood", address: str = "address", kw: float = 0.0) -> None:
        super().__init__(id, name, phone, email, city, neigborhood, address)
        self._kw = kw
    @property
    def kw(self):
        return self._kw
    @kw.setter
    def kw(self, kw):
        self._kw = kw
    def __str__(self) -> str:
        return super().__str__() + f"\nKW: {self._kw}"
    
