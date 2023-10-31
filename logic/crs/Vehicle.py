from .Active import Active
class Vehicle(Active):
    def __init__(self, id: int = 0, name: str = " ", status: bool = False, km: float = 0.0, type: str = "", funtion: str = "") -> None:
        super().__init__(id, name, status)
        self._km = km
        self._type = type
        self._funtion = funtion
    @property
    def km(self):
        return self._km
    @km.setter
    def km(self, km):
        self._km = km
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type
    @property
    def funtion(self):
        return self._funtion
    @funtion.setter
    def funtion(self, funtion):
        self._funtion = funtion
    def __str__(self) -> str:
        return super().__str__() + f"\nKM: {self._km}\nType: {self._type}\nFuntion: {self._funtion}"