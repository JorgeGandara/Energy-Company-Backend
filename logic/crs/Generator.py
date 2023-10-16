from .Active import Active
class Generator(Active):
    def __init__(self, id: int = 0, name: str = " ", status: bool = False, eco: bool = False, power: float = 0.0) -> None:
        super().__init__(id, name, status)
        self._eco = eco
        self._power = power
    @property
    def eco(self):
        return self._eco
    @eco.setter
    def eco(self, eco):
        self._eco = eco
    @property
    def power(self):
        return self._power
    @power.setter
    def power(self, power):
        self._power = power
    def __str__(self) -> str:
        return super().__str__() + f"\nEco: {self._eco}\nPower: {self._power}"