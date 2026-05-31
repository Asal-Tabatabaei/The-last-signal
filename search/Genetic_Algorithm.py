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

            while len(new_pop) < pop_size:
                p1 = population[min(random.sample(range(pop_size), 3), key=lambda i: costs[i])]
                p2 = population[min(random.sample(range(pop_size), 3), key=lambda i: costs[i])]

                combined = list(set(p1 + p2))
                random.shuffle(combined)

                child_size = random.randint(min(len(p1), len(p2)), max(len(p1), len(p2)))
                child = combined[:min(child_size, self.max_sensors)]


                if random.random() < mutation_rate:
                    child = self.get_neighbor(child)
    

                new_pop.append(child if child else self.initialize_state())

            
            population = new_pop

        
        final_costs = [self.evaluate(chrom) for chrom in population]
        final_best_idx = final_costs.index(min(final_costs))
        
        return population[final_best_idx], final_costs[final_best_idx], evaluations, states_history
        

            
