from .Active import Active
class Building(Active):
    def __init__(self, id: int = 0, name: str = " ", status: bool = False, phone: int = 0) -> None:
        super().__init__(id, name, status)
        self._phone = phone
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, phone):
        self._phone = phone
    def __str__(self) -> str:
        return super().__str__() + f"\nPhone: {self._phone}"