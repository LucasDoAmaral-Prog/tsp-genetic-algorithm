import matplotlib.pyplot as plt
from typing import List, Optional


def plot_evolution(
    best_fitness_history: List[float],
    avg_fitness_history: Optional[List[float]] = None,
    title: str = "Evolução da Aptidão ao Longo das Gerações",
    save_path: Optional[str] = None
):
    """
    Plota a evolução da aptidão durante as gerações.

    Args:
        best_fitness_history (List[float]): lista contendo o melhor fitness de cada geração.
        avg_fitness_history (List[float], optional): lista com a média de fitness de cada geração.
        title (str): título do gráfico.
        save_path (str, optional): caminho para salvar o gráfico como imagem.

    Exemplo de uso:
        plot_evolution(best_history, avg_history, save_path="evolution.png")
    """

    plt.figure(figsize=(10, 6))

    # Linha do melhor fitness
    plt.plot(
        best_fitness_history,
        label="Melhor Fitness",
        linewidth=2
    )

    # Linha da média (se fornecida)
    if avg_fitness_history is not None:
        plt.plot(
            avg_fitness_history,
            label="Fitness Médio",
            linestyle="--"
        )

    plt.xlabel("Gerações")
    plt.ylabel("Fitness (Distância Total)")
    plt.title(title)
    plt.grid(alpha=0.3)
    plt.legend()

    # Salvar imagem se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()
