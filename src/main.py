import os
import sys
import argparse
import matplotlib.pyplot as plt

# Adiciona o diretório pai ao sys.path para permitir a importação dos módulos
# quando o script é executado diretamente de src/
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.ga.genetic_algorithm import GeneticAlgorithm
from src.tsp.instance_loader import InstanceLoader
from src.visualization.plot_route import plot_route
from src.visualization.evolution_plot import plot_evolution

def main():
    """
    Ponto de entrada principal para o projeto evoTSP.
    Coordena o carregamento de dados, execução do AG e visualização dos resultados.
    """
    
    # Configuração de argumentos via linha de comando
    parser = argparse.ArgumentParser(description='Evolutionary TSP Solver (evoTSP)')
    parser.add_argument('--dataset', type=str, default='berlin52.csv', 
                        help='Nome do arquivo CSV dentro da pasta datasets/')
    parser.add_argument('--pop_size', type=int, default=100, 
                        help='Tamanho da população (padrão: 100)')
    parser.add_argument('--generations', type=int, default=500, 
                        help='Número de gerações para evoluir (padrão: 500)')
    parser.add_argument('--mutation_rate', type=float, default=0.01, 
                        help='Taxa de mutação (padrão: 0.01)')
    parser.add_argument('--crossover_rate', type=float, default=0.9, 
                        help='Taxa de crossover (padrão: 0.9)')
    parser.add_argument('--elitism', action='store_true', default=True, 
                        help='Ativar elitismo (mantém o melhor indivíduo)')
    
    args = parser.parse_args()

    # Definição de caminhos absolutos baseados na localização deste arquivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, 'datasets', args.dataset)
    results_dir = os.path.join(base_dir, 'results')

    # Cria o diretório de resultados se não existir
    os.makedirs(results_dir, exist_ok=True)

    print("-" * 50)
    print("🧬 evoTSP - Travelling Salesman Problem Solver")
    print("-" * 50)

    # 1. Carregamento da Instância
    if not os.path.exists(dataset_path):
        print(f"❌ Erro: Dataset não encontrado em: {dataset_path}")
        print("Certifique-se de que o arquivo existe na pasta 'datasets/'.")
        return

    print(f"📂 Carregando dataset: {args.dataset}...")
    loader = InstanceLoader(dataset_path)
    try:
        cities = loader.load_cities()
        print(f"✅ {len(cities)} cidades carregadas com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao ler o dataset: {e}")
        return

    # 2. Inicialização do Algoritmo Genético
    print("\n⚙️  Configurando Algoritmo Genético:")
    print(f"   - População: {args.pop_size}")
    print(f"   - Gerações: {args.generations}")
    print(f"   - Taxa de Mutação: {args.mutation_rate}")
    print(f"   - Taxa de Crossover: {args.crossover_rate}")
    print(f"   - Elitismo: {'Ativado' if args.elitism else 'Desativado'}")

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

    # 4. Resultados
    print("\n🏆 Execução Finalizada!")
    print(f"📏 Melhor Distância Encontrada: {best_route.distance:.4f}")
    
    # 5. Visualização e Salvamento
    print("\n📊 Gerando gráficos e salvando resultados...")
    
    # Nome base para os arquivos de saída
    dataset_name = os.path.splitext(args.dataset)[0]
    
    # Plot da Rota Otimizada
    route_filename = os.path.join(results_dir, f"{dataset_name}_best_route.png")
    plot_route(best_route, filename=route_filename, 
               title=f"Melhor Rota ({dataset_name}) - Dist: {best_route.distance:.2f}")
    print(f"   -> Rota salva em: {route_filename}")

    # Plot da Evolução (Convergência)
    evolution_filename = os.path.join(results_dir, f"{dataset_name}_evolution.png")
    plot_evolution(history, filename=evolution_filename, 
                   title=f"Evolução da Fitness ({dataset_name})")
    print(f"   -> Gráfico de evolução salvo em: {evolution_filename}")

    print("\n✅ Processo concluído.")

if __name__ == "__main__":
    main()