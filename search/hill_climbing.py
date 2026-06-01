import copy
from search.local_search_base import LocalSearchBase

class HillClimbing(LocalSearchBase):
    def run(self, initial_state, max_iterations=1000, **kwargs):
        current_state = copy.deepcopy(initial_state)
        current_cost = self.evaluate(current_state)
        
        best_state = copy.deepcopy(current_state)
        best_cost = current_cost
        
        evaluations = [best_cost]
        states_history = [copy.deepcopy(best_state)]
        
        for iteration in range(max_iterations):
            neighbor = self.get_neighbor(current_state)
            neighbor_cost = self.evaluate(neighbor)
            
            if neighbor_cost < current_cost:
                current_state = neighbor
                current_cost = neighbor_cost
                
                if current_cost < best_cost:
                    best_state = copy.deepcopy(current_state)
                    best_cost = current_cost
            
            evaluations.append(best_cost)
            states_history.append(copy.deepcopy(best_state))
        
        return best_state, best_cost, evaluations, states_history