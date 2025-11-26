from typing import List
from .city import City

class Route:
    """
    Representa uma solução candidata (um percurso completo) para o TSP.
    Encapsula a lista de cidades e a distância total do ciclo.
    """
    def __init__(self, cities: List[City]):
        self.cities: List[City] = cities
        # Calcula a distância imediatamente na instanciação
        self.distance: float = self._calculate_distance()

    def _calculate_distance(self) -> float:
        """
        Calcula a distância Euclidiana total do percurso.
        Inclui o retorno da última cidade para a primeira (ciclo fechado).
        """
        total_dist = 0.0
        num_cities = len(self.cities)
        
        for i in range(num_cities):
            current_city = self.cities[i]
            # O operador % garante que o último elemento se conecte ao primeiro
            next_city = self.cities[(i + 1) % num_cities]
            total_dist += current_city.distance_to(next_city)
            
        return total_dist

    def __len__(self) -> int:
        return len(self.cities)

    def __getitem__(self, index: int) -> City:
        return self.cities[index]

    def __repr__(self) -> str:
        return f"Route(cities={len(self.cities)}, distance={self.distance:.2f})"