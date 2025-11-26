import os
import sys
import argparse
import matplotlib.pyplot as plt

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.ga.genetic_algorithm import GeneticAlgorithm
from src.tsp.instance_loader import InstanceLoader
from src.visualization.plot_route import plot_route
from src.visualization.evolution_plot import plot_evolution

def main():
    """
    Ponto de entrada principal para o projeto evoTSP.
    """
    # Configuração de argumentos
    parser = argparse.ArgumentParser(description='Evolutionary TSP Solver (evoTSP)')
    parser.add_argument('--dataset', type=str, default='berlin52.csv', 
                        help='Nome do arquivo CSV dentro da pasta datasets/')
    parser.add_argument('--pop_size', type=int, default=100, help='Tamanho da população')
    parser.add_argument('--generations', type=int, default=500, help='Número de gerações')
    parser.add_argument('--mutation_rate', type=float, default=0.01, help='Taxa de mutação')
    parser.add_argument('--crossover_rate', type=float, default=0.9, help='Taxa de crossover')
    parser.add_argument('--elitism', action='store_true', default=True, help='Ativar elitismo')
    
    args = parser.parse_args()

    # Definição de diretórios
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, 'datasets', args.dataset)
    results_dir = os.path.join(base_dir, 'results')
    routes_dir = os.path.join(base_dir, 'routes')

    # Cria diretórios se não existirem
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(routes_dir, exist_ok=True)

    print("-" * 50)
    print("🧬 evoTSP - Travelling Salesman Problem Solver")
    print("-" * 50)

    # 1. Carregamento
    if not os.path.exists(dataset_path):
        print(f"❌ Erro: Dataset não encontrado em: {dataset_path}")
        return

    print(f"📂 Carregando dataset: {args.dataset}...")
    loader = InstanceLoader(dataset_path)
    try:
        cities = loader.load_cities()
        print(f"✅ {len(cities)} cidades carregadas.")
    except Exception as e:
        print(f"❌ Erro ao ler o dataset: {e}")
        return

    # 2. Configuração do AG
    ga = GeneticAlgorithm(
        cities=cities,
        pop_size=args.pop_size,
        mutation_rate=args.mutation_rate,
        crossover_rate=args.crossover_rate,
        elitism=args.elitism
    )

    # 3. Execução
    print("\n🚀 Iniciando evolução...")
    best_route, history = ga.run(generations=args.generations)

    # 4. Resultados no Console
    print("\n🏆 Execução Finalizada!")
    print(f"📏 Melhor Distância: {best_route.distance:.4f}")

    # 5. Salvando a Rota em Arquivo de Texto (Pasta routes/)
    dataset_name = os.path.splitext(args.dataset)[0]
    solution_filename = os.path.join(routes_dir, f"{dataset_name}_solution.txt")
    
    route_indices = [str(city.index) for city in best_route.cities]
    # Fecha o ciclo adicionando o início ao fim para visualização
    route_indices_closed = route_indices + [route_indices[0]]
    
    print(f"\n📝 Salvando solução em: {solution_filename}")
    with open(solution_filename, 'w') as f:
        f.write(f"Dataset: {args.dataset}\n")
        f.write(f"Distancia Total: {best_route.distance:.4f}\n")
        f.write(f"Geracoes: {args.generations}\n")
        f.write("-" * 20 + "\n")
        f.write("Ordem das Cidades:\n")
        f.write(" -> ".join(route_indices_closed))
        f.write("\n")
    
    # Exibe prévia no console
    print("   -> Rota: " + " -> ".join(route_indices_closed[:10]) + " ...")

    # 6. Gerando Gráficos (Pasta results/)
    print("\n📊 Gerando gráficos...")
    
    # Gráfico 1: O Mapa da Rota
    route_img_filename = os.path.join(results_dir, f"{dataset_name}_best_route.png")
    plot_route(best_route, filename=route_img_filename, 
               title=f"Melhor Rota ({dataset_name}) - Dist: {best_route.distance:.2f}")
    print(f"   -> Mapa salvo em: {route_img_filename}")

    # Gráfico 2: A Evolução (Convergência)
    evolution_img_filename = os.path.join(results_dir, f"{dataset_name}_evolution.png")
    plot_evolution(history, filename=evolution_img_filename, 
                   title=f"Evolução da Fitness ({dataset_name})")
    print(f"   -> Gráfico de evolução salvo em: {evolution_img_filename}")
    
    print("\n✅ Processo concluído com sucesso.")

if __name__ == "__main__":
    main()