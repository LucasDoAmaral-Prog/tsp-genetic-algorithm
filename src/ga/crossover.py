import random
from typing import List, Any, Tuple

def ordered_crossover(parent1: List[Any], parent2: List[Any]) -> Tuple[List[Any], List[Any]]:
    """
    Executes Ordered Crossover (OX1).
    Preserves a subsequence from one parent and relative order from the other.
    """
    size = len(parent1)
    # Select random cross section
    start, end = sorted(random.sample(range(size), 2))

    def _build_child(p_primary: List[Any], p_secondary: List[Any]) -> List[Any]:
        child = [None] * size
        # Copy segment from primary parent
        child[start:end] = p_primary[start:end]
        
        # Fill remaining slots with secondary parent's genes
        current_idx = 0
        for gene in p_secondary:
            if gene not in child:
                # Find next empty slot
                while child[current_idx] is not None:
                    current_idx += 1
                child[current_idx] = gene
        return child

    child1 = _build_child(parent1, parent2)
    child2 = _build_child(parent2, parent1)
    
    return child1, child2

def cycle_crossover(parent1: List[Any], parent2: List[Any]) -> Tuple[List[Any], List[Any]]:
    """
    Executes Cycle Crossover (CX).
    Preserves absolute positions of elements from parents.
    """
    size = len(parent1)

    def _build_child(p_primary: List[Any], p_secondary: List[Any]) -> List[Any]:
        child = [None] * size
        cycle_indices = set()
        
        # Trace the first cycle
        idx = 0
        while idx not in cycle_indices:
            cycle_indices.add(idx)
            val_in_p2 = p_secondary[idx]
            idx = p_primary.index(val_in_p2)
        
        # Assign genes based on cycle membership
        for i in range(size):
            child[i] = p_primary[i] if i in cycle_indices else p_secondary[i]
            
        return child

    child1 = _build_child(parent1, parent2)
    child2 = _build_child(parent2, parent1)

    return child1, child2