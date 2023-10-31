from .Person import Person

class Employee(Person):
    def __init__(self, id: int = 0, name: str = "Name", phone: bool = False, email: str = "name@domain", city: str = "City", neigborhood: str = "neigborhood", address: str = "address", salary: float = 0.0) -> None:
        super().__init__(id, name, phone, email, city, neigborhood, address)
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        self._salary = salary
    def __str__(self) -> str:
        return super().__str__() + f"\nSalary: {self._salary}"