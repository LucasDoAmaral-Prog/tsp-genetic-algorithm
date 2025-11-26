import random
from typing import List
from ..tsp.route import Route

def tournament_selection(population: List[Route], k: int = 3) -> Route:
    """
    Selects the best individual from a random subset of size k.
    """
    candidates = random.sample(population, k)
    # Returns the route with the smallest distance
    return min(candidates, key=lambda x: x.distance)

def roulette_selection(population: List[Route]) -> Route:
    """
    Selects an individual based on fitness probability (Fitness = 1/Distance).
    """
    # Calculate fitness (inverse of distance for minimization)
    fitnesses = [1 / route.distance for route in population]
    total_fitness = sum(fitnesses)
    
    pick = random.uniform(0, total_fitness)
    current = 0
    
    for route, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            return route
            
    return population[-1]