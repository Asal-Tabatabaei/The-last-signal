from search.local_search_base import LocalSearchBase


class HillClimbing(LocalSearchBase):
<<<<<<< HEAD
    def run(self, initial_state, max_iterations=1000, **kwargs):

        current_state = copy.deepcopy(initial_state)
        current_cost = self.evaluate(current_state)

        best_state = copy.deepcopy(current_state)
        best_cost = current_cost
        
=======
    def run(self, initial_state, **kwargs):
>>>>>>> 697989e659a00b46638967e206063f6054c7855f
        """
        TODO: Implement the Hill Climbing algorithm.
        
        Parameters
        ----------
        initial_state : list of tuples
            The initial configuration of sensors.
        **kwargs : 
            Define and add any other parameters you might need for the algorithm 

        Returns
        -------
        best_state : list of tuples
            The best configuration found.
        best_cost : int or float
            The cost of the best configuration.
        evaluations : list
            List of costs at each iteration (used for plotting).
        states_history : list of lists
            List of states at each iteration (used for animation).
        """
        
        raise NotImplementedError("Students must implement this method.")