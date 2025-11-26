import matplotlib.pyplot as plt
from ..tsp.route import Route

def plot_route(route: Route, filename: str = None, title: str = "Rota"):
    """
    Plota a rota geográfica.
    Eixo X = Longitude
    Eixo Y = Latitude
    """
    # Extrai coordenadas
    lons = [city.lon for city in route.cities]
    lats = [city.lat for city in route.cities]
    
    # Fecha o ciclo
    lons.append(lons[0])
    lats.append(lats[0])

    plt.figure(figsize=(10, 6))
    
    # Plota a linha do trajeto
    plt.plot(lons, lats, 'bo-', markersize=4, linewidth=1, alpha=0.7, label='Trajeto')
    
    # Destaca o início (Vermelho)
    plt.plot(lons[0], lats[0], 'rs', markersize=8, label='Início')

    # Adiciona nomes das cidades no gráfico
    for city in route.cities:
        plt.annotate(city.name, (city.lon, city.lat), 
                     textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

    plt.title(title)
    plt.xlabel("Longitude (Graus)")
    plt.ylabel("Latitude (Graus)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    
    # Ajusta proporção para não distorcer o mapa geograficamente
    plt.axis('equal') 

    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()