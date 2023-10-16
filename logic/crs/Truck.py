from .Vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self, id: int = 0, name: str = " ", status: bool = False, km: float = 0.0, funtion: str = " ") -> None:
        super().__init__(id, name, status, km)
        self._funtion = funtion
    @property
    def funtion(self):
        return self._funtion
    @funtion.setter
    def funtion(self, funtion):
        self._funtion = funtion
    def __str__(self) -> str:
        return super().__str__() + f"\nFuntion: {self._funtion}"