import math
import random
from search.local_search_base import LocalSearchBase


class SimulatedAnnealing(LocalSearchBase):
    def __init__(self, world):

        super().__init__(world)

    def run(self, initial_state, **kwargs):

        initial_temp = kwargs.get('initial_temp', 100.0)
        cooling_rate = kwargs.get('cooling_rate', 0.99)
        min_temp = kwargs.get('min_temp', 0.01)
        max_iterations = kwargs.get('max_iterations', 3000)

        current_state = list(initial_state)
        current_cost = self.evaluate(current_state)

        best_state = current_state
        best_cost = current_cost

        evaluations = [current_cost]
        states_history = [current_state]

        T = initial_temp

        for iteration in range(max_iterations):
            if T < min_temp:
                break

            neighbor = self.get_neighbor(current_state)
            neighbor_cost = self.evaluate(neighbor)

            delta_e = neighbor_cost - current_cost

            if delta_e < 0:
                current_state = neighbor
                current_cost = neighbor_cost

                if current_cost < best_cost:
                    best_state = current_state
                    best_cost = current_cost

            else:
                acceptance_probability = math.exp(-delta_e / T)

                if random.random() < acceptance_probability:

                    current_state = neighbor
                    current_cost = neighbor_cost

            evaluations.append(current_cost)
            states_history.append(current_state)

            T *= cooling_rate
        return best_state, best_cost, evaluations, states_history