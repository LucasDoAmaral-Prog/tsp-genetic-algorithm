import math
from dataclasses import dataclass

@dataclass(frozen=True)
class City:
    """
    Representa uma cidade no grafo TSP.
    Agora utiliza 'name' (string) como identificador.
    """
    name: str
    x: float
    y: float

    def distance_to(self, other: 'City') -> float:
        """Calcula a distância Euclidiana entre esta cidade e outra."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def __repr__(self) -> str:
        return f"City(name='{self.name}', x={self.x}, y={self.y})"