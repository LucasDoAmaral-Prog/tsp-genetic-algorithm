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
    Configurado para Cenários Logísticos Reais.
    """
    parser = argparse.ArgumentParser(description='Evolutionary TSP Solver (evoTSP)')
    
    # --- CONFIGURAÇÕES PADRÃO ATUALIZADAS (Recomendação IA) ---
    # Dataset padrão alterado para o de logística
    parser.add_argument('--dataset', type=str, default='logistica_brasil.csv', 
                        help='Nome do arquivo CSV dentro da pasta datasets/')
    
    # Aumentado para 200 para garantir diversidade genética em mapas complexos
    parser.add_argument('--pop_size', type=int, default=200, 
                        help='Tamanho da população')
    
    # Aumentado para 2000. Para ~30 cidades, 500 é pouco. 2000 garante convergência.
    parser.add_argument('--generations', type=int, default=2000, 
                        help='Número de gerações')
    
    parser.add_argument('--mutation_rate', type=float, default=0.01, 
                        help='Taxa de mutação')
    
    parser.add_argument('--crossover_rate', type=float, default=0.9, 
                        help='Taxa de crossover')
    
    parser.add_argument('--elitism', action='store_true', default=True, 
                        help='Ativar elitismo')
    
    args = parser.parse_args()

    # Diretórios
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, 'datasets', args.dataset)
    results_dir = os.path.join(base_dir, 'results')
    routes_dir = os.path.join(base_dir, 'routes')

    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(routes_dir, exist_ok=True)

    print("-" * 60)
    print("🚛 evoTSP - Otimizador Logístico (Genetic Algorithm)")
    print("-" * 60)

    # 1. Carregamento
    if not os.path.exists(dataset_path):
        print(f"❌ Erro: Dataset não encontrado em: {dataset_path}")
        return

    print(f"📂 Carregando malha logística: {args.dataset}...")
    loader = InstanceLoader(dataset_path)
    try:
        cities = loader.load_cities()
        print(f"✅ {len(cities)} pontos de parada carregados.")
    except Exception as e:
        print(f"❌ Erro ao ler o dataset: {e}")
        return

    # 2. Configuração do AG
    print("\n⚙️  Parâmetros da IA:")
    print(f"   - População: {args.pop_size} indivíduos")
    print(f"   - Gerações: {args.generations} ciclos evolutivos")
    
    ga = GeneticAlgorithm(
        cities=cities,
        pop_size=args.pop_size,
        mutation_rate=args.mutation_rate,
        crossover_rate=args.crossover_rate,
        elitism=args.elitism
    )

    # 3. Execução
    print("\n🚀 Calculando melhor rota de entrega...")
    best_route, history = ga.run(generations=args.generations)

    # 4. Resultados
    print("\n🏆 Otimização Concluída!")
    print(f"🚚 Distância Total Estimada: {best_route.distance:.2f} km")

    # 5. Salvando Rota
    dataset_name = os.path.splitext(args.dataset)[0]
    solution_filename = os.path.join(routes_dir, f"{dataset_name}_route.txt")
    
    route_names = [city.name for city in best_route.cities]
    route_names_closed = route_names + [route_names[0]]
    
    with open(solution_filename, 'w', encoding='utf-8') as f:
        f.write(f"Malha Logística: {args.dataset}\n")
        f.write(f"Distância Total: {best_route.distance:.2f} km\n")
        f.write("-" * 30 + "\n")
        f.write("SEQUÊNCIA DE ENTREGA SUGERIDA:\n")
        for i, city_name in enumerate(route_names_closed):
            f.write(f"{i+1}. {city_name}\n")
    
    print(f"📝 Manifesto de carga salvo em: {solution_filename}")

    # Exibe prévia
    print("\n🗺️  Resumo do Itinerário:")
    print(f"   Início: {route_names_closed[0]}")
    print(f"   Passando por: {', '.join(route_names_closed[1:4])}...")
    print(f"   Fim: {route_names_closed[-1]}")

    # 6. Gráficos
    print("\n📊 Gerando mapas e relatórios...")
    
    plot_route(best_route, filename=os.path.join(results_dir, f"{dataset_name}_map.png"), 
               title=f"Rota Logística Otimizada - Total: {best_route.distance:.0f} km")

    plot_evolution(history, filename=os.path.join(results_dir, f"{dataset_name}_convergence.png"), 
                   title=f"Curva de Aprendizado da IA ({dataset_name})")
    
    print(f"✅ Mapas salvos na pasta 'results/'.")

if __name__ == "__main__":
    main()