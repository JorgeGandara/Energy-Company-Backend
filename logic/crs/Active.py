class Active:
    def __init__(self, id: int = 0, name: str = " ", status: bool = False) -> None:
        self._id = id
        self._name = name
        self._status = status
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def status(self):
        return self._status
    @id.setter
    def id(self, id):
        self._id = id
    @name.setter
    def name(self, name):
        self._name = name
    @status.setter
    def status(self, status):
        self._status = status
    def __str__(self) -> str:
        return f"ID: {self._id}\nName: {self._name}\nStatus: {self._status}"