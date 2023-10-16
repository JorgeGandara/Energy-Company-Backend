from .Person import Person

class Client(Person):
    def __init__(self, id: int = 0, name: str = " ", phone: int = 0, email: str = " ", kw: float = 0.0):
        super().__init__(id, name, phone, email)
        self._kw = kw
    @property
    def kw(self):
        return self._kw
    @kw.setter
    def kw(self, kw):
        self._kw = kw