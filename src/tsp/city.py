import math
from dataclasses import dataclass

@dataclass(frozen=True)
class City:
    """
    Representa uma localização geográfica real.
    Utiliza Latitude e Longitude.
    """
    name: str
    lat: float  # Latitude em graus
    lon: float  # Longitude em graus

    def distance_to(self, other: 'City') -> float:
        """
        Calcula a distância entre duas coordenadas usando a Fórmula de Haversine.
        Retorna a distância em Quilômetros (km).
        """
        # Raio da Terra em km
        R = 6371.0

        # Converte graus para radianos
        lat1 = math.radians(self.lat)
        lon1 = math.radians(self.lon)
        lat2 = math.radians(other.lat)
        lon2 = math.radians(other.lon)

        # Diferenças
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Fórmula de Haversine
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    def __repr__(self) -> str:
        return f"City(name='{self.name}', lat={self.lat}, lon={self.lon})"