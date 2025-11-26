import random
from typing import List, Tuple, Optional
from tqdm import tqdm

from ..tsp.city import City
from ..tsp.route import Route
from .selection import tournament_selection
from .crossover import ordered_crossover
from .mutation import inversion_mutation

class genetic_algorithm:
    def __init__(self, cities: List[City], pop_size: int = 100, 
                 mutation_rate: float = 0.01, crossover_rate: float = 0.9, 
                 elitism: bool = True):
        self.cities = cities
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        self.population: List[Route] = []
        
        self._initialize_population()

    def _initialize_population(self):
        """Creates initial random population."""
        self.population = []
        for _ in range(self.pop_size):
            # Create random permutation of cities
            shuffled_cities = random.sample(self.cities, len(self.cities))
            self.population.append(Route(shuffled_cities))

    def _get_best_route(self) -> Route:
        """Returns the route with the shortest distance in current population."""
        # Sort population by distance (ascending)
        self.population.sort(key=lambda x: x.distance)
        return self.population[0]

    def _evolve(self):
        """Executes one generation of evolution."""
        new_population = []

        # Elitism: Keep the best individual
        if self.elitism:
            new_population.append(self.population[0])

        # Generate offspring
        while len(new_population) < self.pop_size:
            # Selection
            p1 = tournament_selection(self.population)
            p2 = tournament_selection(self.population)

            # Crossover
            if random.random() < self.crossover_rate:
                # Operates on list of cities (genes)
                child1_cities, child2_cities = ordered_crossover(p1.cities, p2.cities)
                c1, c2 = Route(child1_cities), Route(child2_cities)
            else:
                c1, c2 = p1, p2

            # Mutation
            for child in [c1, c2]:
                if len(new_population) < self.pop_size:
                    if random.random() < self.mutation_rate:
                        mutated_cities = inversion_mutation(child.cities)
                        child = Route(mutated_cities)
                    new_population.append(child)

        self.population = new_population
        # Ensure population is sorted after evolution step
        self.population.sort(key=lambda x: x.distance)

    def run(self, generations: int) -> Tuple[Route, List[float]]:
        """
        Runs the GA loop.
        Returns: (best_route, distance_history)
        """
        distance_history = []
        
        # Initial sort
        self.population.sort(key=lambda x: x.distance)
        initial_best = self.population[0]
        distance_history.append(initial_best.distance)

        progress_bar = tqdm(range(generations), desc="Evolving", unit="gen")
        
        for _ in progress_bar:
            self._evolve()
            best_current = self.population[0]
            distance_history.append(best_current.distance)
            
            # Update progress bar description with current best
            progress_bar.set_postfix({"Best Dist": f"{best_current.distance:.2f}"})

        return self.population[0], distance_history