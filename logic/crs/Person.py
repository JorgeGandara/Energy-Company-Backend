class Person:
    def __init__(self, id: int = 0, name: str = " ", phone: int = 0, email: str = " "):    
        self._id = id
        self._name = name
        self._phone = phone
        self._email = email
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def phone(self):
        return self._phone
    @property
    def email(self):
        return self._email
    @id.setter
    def id(self, id):
        self._id = id
    @name.setter
    def name(self, name):
        self._name = name
    @phone.setter
    def phone(self, phone):
        self._phone = phone
    @email.setter
    def email(self, email):
        self._email = email
    def __str__(self) -> str:
        return f"ID: {self._id}\nName: {self._name}\nPhone: {self._phone}\nEmail: {self._email}"