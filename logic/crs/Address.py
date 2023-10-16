class Address:
    def __init__(self, city: str = " ", neighborhood: str = " ", address: str = " "):
        self._city = city
        self._neighborhood = neighborhood
        self._address = address
    @property
    def city(self):
        return self._city
    @property
    def neighborhood(self):
        return self._neighborhood
    @property
    def address(self):
        return self._address
    @city.setter
    def city(self, city):
        self._city = city
    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self._neighborhood = neighborhood
    @address.setter
    def address(self, address):
        self._address = address
