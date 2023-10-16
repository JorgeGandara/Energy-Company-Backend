from .Person import Person

class Employee(Person):
    def __init__(self, id: int = 0, name: str = " ", phone: int = 0, email: str = " ", salary: int = 0.0):
        super().__init__(id, name, phone, email)
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        self._salary = salary