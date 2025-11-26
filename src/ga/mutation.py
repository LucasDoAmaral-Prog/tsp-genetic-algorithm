import random
from typing import List, Any

def swap_mutation(chromosome: List[Any]) -> List[Any]:
    """
    Performs Swap Mutation.
    Selects two genes at random and swaps their positions.
    """
    mutated = chromosome[:]
    size = len(mutated)
    
    idx1, idx2 = random.sample(range(size), 2)
    mutated[idx1], mutated[idx2] = mutated[idx2], mutated[idx1]
    
    return mutated

def inversion_mutation(chromosome: List[Any]) -> List[Any]:
    """
    Performs Inversion Mutation (2-opt).
    Selects a sub-sequence and reverses its order.
    Often better for TSP as it preserves adjacency information.
    """
    mutated = chromosome[:]
    size = len(mutated)
    
    start, end = sorted(random.sample(range(size), 2))
    
    # Reverse the slice [start:end+1]
    # Adding 1 to end because python slices are exclusive at the upper bound
    mutated[start:end+1] = mutated[start:end+1][::-1]
    
    return mutated