# src/ga/__init__.py

"""
Pacote ga (Genetic Algorithm).

Este pacote contém a implementação completa do Algoritmo Genético, 
incluindo a classe principal de controle e os operadores genéticos 
(seleção, crossover e mutação).
"""

from .genetic_algorithm import GeneticAlgorithm
from .selection import tournament_selection, roulette_selection
from .crossover import ordered_crossover, cycle_crossover
from .mutation import swap_mutation, inversion_mutation

# Define o que é exportado quando se faz "from src.ga import *"
__all__ = [
    'GeneticAlgorithm',
    'tournament_selection',
    'roulette_selection',
    'ordered_crossover',
    'cycle_crossover',
    'swap_mutation',
    'inversion_mutation'
]