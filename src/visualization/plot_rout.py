import matplotlib.pyplot as plt
from typing import List
from tsp.city import City


def plot_route(route: List[City], title: str = "Melhor Rota Encontrada", save_path: str = None):
    """
    Plota graficamente a rota final do TSP.

    Args:
        route (List[City]): lista de objetos City na ordem da rota.
        title (str): título do gráfico.
        save_path (str): caminho para salvar a imagem.
    """
    
    if not route or len(route) < 2:
        raise ValueError("A rota deve conter ao menos duas cidades para plotar.")

    # Extrai coordenadas
    x_coords = [city.x for city in route] + [route[0].x]  # retorna ao início
    y_coords = [city.y for city in route] + [route[0].y]

    plt.figure(figsize=(8, 8))

    # Plota a rota
    plt.plot(x_coords, y_coords, marker='o', linewidth=2)
    
    # Marca as cidades com seus nomes/IDs
    for city in route:
        plt.text(city.x, city.y, str(city.id), fontsize=9, ha='right')

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    # Salvar imagem (se necessário)
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()
