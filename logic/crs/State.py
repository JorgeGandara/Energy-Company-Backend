from .Event import Event
class State(Event):
    def __init__(self, id: int = 0, date: str = "", hour: str = "hour", description: str = "") -> None:
        super().__init__(id, date, hour)
        self._description = description
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description
    def __str__(self) -> str:
        return super().__str__() + f"\nDescription: {self._description}"