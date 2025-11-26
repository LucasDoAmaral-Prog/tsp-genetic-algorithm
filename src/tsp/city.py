import math
from dataclasses import dataclass

@dataclass(frozen=True)
class City:
    """
    Representa uma cidade/localização.
    Suporta tanto coordenadas Geográficas (Lat/Lon) quanto Cartesianas (X/Y).
    """
    name: str
    c1: float  # Pode ser Latitude ou X
    c2: float  # Pode ser Longitude ou Y
    is_geo: bool = False # Define o modo de cálculo

    @property
    def lat(self): return self.c1
    @property
    def lon(self): return self.c2
    @property
    def x(self): return self.c1
    @property
    def y(self): return self.c2

    def distance_to(self, other: 'City') -> float:
        """
        Calcula a distância dependendo do modo (Geográfico ou Euclidiano).
        """
        if self.is_geo and other.is_geo:
            return self._haversine_distance(other)
        else:
            return self._euclidean_distance(other)

    def _euclidean_distance(self, other: 'City') -> float:
        """Cálculo simples de Pitágoras para planos 2D."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def _haversine_distance(self, other: 'City') -> float:
        """Cálculo real de navegação (considerando curvatura da Terra)."""
        R = 6371.0 # Raio da Terra em km
        
        # Converte graus para radianos
        lat1, lon1 = math.radians(self.lat), math.radians(self.lon)
        lat2, lon2 = math.radians(other.lat), math.radians(other.lon)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c

    def __repr__(self) -> str:
        coord_type = "Geo" if self.is_geo else "Cartesian"
        return f"City({self.name}, {coord_type}, {self.c1:.2f}, {self.c2:.2f})"