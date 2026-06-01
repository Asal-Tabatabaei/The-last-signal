import copy
from search.local_search_base import LocalSearchBase

class BeamSearch(LocalSearchBase):
    def run(self, initial_state, beam_width=5, max_iterations=200, **kwargs):

        beam = [(self.evaluate(initial_state), copy.deepcopy(initial_state))]
        evaluations = []
        states_history = []
        
        best_state = copy.deepcopy(initial_state)
        best_cost = self.evaluate(initial_state)
        
        for iteration in range(max_iterations):
            candidates = []
            
            for cost, state in beam:
                for _ in range(beam_width * 2):
                    neighbor = self.get_neighbor(state)
                    neighbor_cost = self.evaluate(neighbor)
                    candidates.append((neighbor_cost, copy.deepcopy(neighbor)))
            
            # Keep only top-k candidates (lowest cost)
            candidates.sort(key=lambda x: x[0])
            beam = candidates[:beam_width]
            
            # Update best solution found so far
            if beam and beam[0][0] < best_cost:
                best_cost = beam[0][0]
                best_state = copy.deepcopy(beam[0][1])
            
            evaluations.append(best_cost)
            states_history.append(copy.deepcopy(best_state))
            
            if len(beam) == 0:
                break
        
        return best_state, best_cost, evaluations, states_history