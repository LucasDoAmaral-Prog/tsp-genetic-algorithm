import matplotlib.pyplot as plt
from typing import List

def plot_evolution(history: List[float], filename: str = None, title: str = "Evolução da Fitness"):
    """
    Plota o gráfico de convergência (distância vs gerações).
    """
    plt.figure(figsize=(10, 6))
    plt.plot(history, 'b-', linewidth=2)
    
    plt.title(title)
    plt.xlabel("Geração")
    plt.ylabel("Melhor Distância (Menor é melhor)")
    plt.grid(True, linestyle='--', alpha=0.5)
    
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()