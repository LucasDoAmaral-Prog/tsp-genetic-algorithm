import matplotlib.pyplot as plt
from ..tsp.route import Route

def plot_route(route: Route, filename: str = None, title: str = "Rota"):
    """
    Plota a rota visualmente usando Matplotlib.
    """
    x = [city.x for city in route.cities]
    y = [city.y for city in route.cities]
    
    # Adiciona a primeira cidade ao final para fechar o ciclo no gráfico
    x.append(x[0])
    y.append(y[0])

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'co-', markersize=5, linewidth=1, alpha=0.7)
    plt.plot(x[0], y[0], 'rs', markersize=8, label='Início/Fim')  # Destaca o início
    
    plt.title(title)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()