from .Active import Active
class Vehicle(Active):
    def __init__(self, id: int = 0, name: str = " ", status: bool = False, km: float = 0.0) -> None:
        super().__init__(id, name, status)
        self._km = km