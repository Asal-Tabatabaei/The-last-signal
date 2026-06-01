import copy
from collections import deque
from search.local_search_base import LocalSearchBase

class TabuSearch(LocalSearchBase):
    def run(self, initial_state, max_iterations=500, tabu_limit=10, **kwargs):
        current_state = copy.deepcopy(initial_state)
        current_cost = self.evaluate(current_state)
        
        best_state = copy.deepcopy(current_state)
        best_cost = current_cost
        
        tabu_list = deque(maxlen=tabu_limit)
        
        evaluations = [best_cost]
        states_history = [copy.deepcopy(best_state)]
        
        for iteration in range(max_iterations):
            # Generate neighbors
            neighbors = []
            for _ in range(20):  
                neighbor = self.get_neighbor(current_state)
                neighbor_cost = self.evaluate(neighbor)
                
                neighbor_key = frozenset(neighbor)
                
                neighbors.append((neighbor_cost, neighbor, neighbor_key))
            
            # Sorting them by lowest cost ...
            neighbors.sort(key=lambda x: x[0])
            
            # Find best non-tabu neighbor (or allow tabu if it improves global best)
            best_neighbor = None
            best_neighbor_cost = float('inf')
            best_neighbor_key = None
            
            for cost, neighbor, neighbor_key in neighbors:
                if neighbor_key not in tabu_list:
                    best_neighbor = neighbor
                    best_neighbor_cost = cost
                    best_neighbor_key = neighbor_key
                    break
            
            # If all neighbors are tabu, pick the best one
            if best_neighbor is None and neighbors:
                best_neighbor = neighbors[0][1]
                best_neighbor_cost = neighbors[0][0]
                best_neighbor_key = neighbors[0][2]
            
            if best_neighbor is not None:
                current_state = best_neighbor
                current_cost = best_neighbor_cost
                
                tabu_list.append(best_neighbor_key)
                
                # Updating the best one
                if current_cost < best_cost:
                    best_state = copy.deepcopy(current_state)
                    best_cost = current_cost
            
            evaluations.append(best_cost)
            states_history.append(copy.deepcopy(best_state))
        
        return best_state, best_cost, evaluations, states_history