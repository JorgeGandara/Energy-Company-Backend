from .Event import Event

class Cut(Event):
    def __init__(self, id: int = 0, date: str = "", hour: str = "hour", 
                 city: str = "", neighborhood: str = "") -> None:
        super().__init__(id, date, hour)
        self._city = city
        self._neighborhood = neighborhood
    @property
    def city(self):
        return self._city
    @property
    def neighborhood(self):
        return self._neighborhood
    @city.setter
    def city(self, city):
        self._city = city
    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self._neighborhood = neighborhood
    def __str__(self) -> str:
        return super().__str__() + f"\nCity: {self._city}\nNeighborhood: {self._neighborhood}"