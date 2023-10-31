class Person:
    def __init__(self, id: int = 0, name: str = "Name", phone: bool = False, email: str = "name@domain", city: str = "City", neigborhood: str = "neigborhood", address: str = "address") -> None:
        self._id = id
        self._name = name
        self._phone = phone
        self._email = email
        self._city = city
        self._neigborhood = neigborhood
        self._address = address
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
    @property
    def city(self):
        return self._city
    @property
    def neigborhood(self):
        return self._neigborhood
    @property
    def address(self):
        return self._address
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
    @city.setter
    def city(self, city):
        self._city = city
    @neigborhood.setter
    def neigborhood(self, neigborhood):
        self._neigborhood = neigborhood
    @address.setter
    def address(self, address):
        self._address = address
    def __str__(self) -> str:
        return f"ID: {self._id}\nName: {self._name}\nPhone: {self._phone}\nEmail: {self._email}\nCity: {self._city}\nNeigborhood: {self._neigborhood}\nAddress: {self._address}" 