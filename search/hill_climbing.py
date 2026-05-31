from search.local_search_base import LocalSearchBase


class HillClimbing(LocalSearchBase):
    def run(self, initial_state, max_iterations=1000, **kwargs):

        current_state = copy.deepcopy(initial_state)
        current_cost = self.evaluate(current_state)

        best_state = copy.deepcopy(current_state)
        best_cost = current_cost
        
    