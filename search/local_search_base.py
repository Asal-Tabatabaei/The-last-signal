class LocalSearchBase:
    def __init__(self, world):
        self.world = world

    def evaluate(self, state):
        covered_targets = set()

        overlap_penalty = 0

        covered_cells = {}

        
        for (sx, sy) in state:

            for i in range(self.world.rows):
                for j in range(self.world.cols):

                    dist = abs(sx - i) + abs(sy - j)

                    if dist <= self.world.sensor_range:

                        
                        covered_cells[(i, j)] = (
                            covered_cells.get((i, j), 0) + 1
                        )

                        
                        if self.world.grid[i][j] == self.world.TARGET:
                            covered_targets.add((i, j))
        for count in covered_cells.values():

            if count > 1:
                overlap_penalty += (count - 1)

        score = (
            len(covered_targets) * 100
            - overlap_penalty * 3
            - len(state) * 2
        )

        
        return -score
    def get_neighbor(self, state):
        """
        TODO: Implement the neighbor generation function.
        
        Generate a new valid state by applying a local change to the current state.
        Ensure you include all the required operations mentioned in the project PDF
        to support a dynamic search space.
        
        Returns:
            neighbor_state (list of tuples): The newly generated valid state.
        """
        raise NotImplementedError("Students must implement this method.")

    def initialize_state(self):
        """
        TODO: Generate a valid initial state.
        
        Create a starting configuration of sensors within the grid boundaries,
        respecting the maximum sensor limits and obstacle placements.
        
        Returns:
            initial_state (list of tuples): The starting coordinates of the sensors.
        """
        raise NotImplementedError("Students must implement this method.")