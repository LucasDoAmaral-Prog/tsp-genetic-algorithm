import math
from dataclasses import dataclass

@dataclass(frozen=True)
class City:
    index: int
    x: float
    y: float

    def distance_to(self, other: 'City') -> float:
        """Calculates Euclidean distance between self and another city."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def __repr__(self) -> str:
        return f"City(id={self.index}, x={self.x}, y={self.y})"