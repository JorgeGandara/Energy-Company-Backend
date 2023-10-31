from datetime import datetime

class Event:
    def __init__(self, id: int = 0, date: str = "", hour: str = "hour") -> None:
        self._id = id
        self._date = datetime.strptime(date, "%Y-%m-%d").date() if date else None            
        self._hour = hour
    @property
    def id(self):
        return self._id
    @property
    def date(self):
        return self._date
    @property
    def hour(self):
        return self._hour
    @id.setter
    def id(self, id):
        self._id = id
    @date.setter
    def date(self, date):
        self._date = date
    @hour.setter
    def hour(self, hour):
        self._hour = hour
    def __str__(self) -> str:
        return f"ID: {self._id}\nDate: {self._date}\nHour: {self._hour}"
