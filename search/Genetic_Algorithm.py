import random
import math
from search.local_search_base import LocalSearchBase
class GeneticAlgorithm(LocalSearchBase):
    def __init__(self, world):
        super().__init__(world)

    def run(self, initial_state, **kwargs):
        pop_size = kwargs.get('pop_size', 30)
        generations = kwargs.get('generations', 80)
        mutation_rate = kwargs.get('mutation_rate', 0.3)

       
        population = [list(initial_state)] + [self.initialize_state() for _ in range(pop_size - 1)]
        evaluations, states_history = [], []

        for gen in range(generations):
            costs = [self.evaluate(chrom) for chrom in population]
            best_idx = costs.index(min(costs))
            
            
            evaluations.append(costs[best_idx])
            states_history.append(list(population[best_idx]))

            new_pop = [list(population[best_idx])]
    

