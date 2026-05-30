import random

class LocalSearchBase:
    def __init__(self, world):
        self.world = world
        self.rows = world.rows
        self.cols = world.cols
        self.max_sensors = world.max_sensors
        self.sensor_range = world.sensor_range
        self.targets = world.get_targets()
        
    def evaluate(self, state):
<<<<<<< HEAD
        """
        TODO: Implement the evaluation (Cost) function.
        
        Design a function that calculates the cost of the current sensor placement.
        Refer to the project documentation for the primary objectives and constraints.
        
        Returns:    
            cost (int or float): The evaluated cost of the state (lower is better).
        """
        raise NotImplementedError("Students must implement this method.")

=======
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
>>>>>>> 697989e659a00b46638967e206063f6054c7855f
    def get_neighbor(self, state):

        neighbor_state = list(state)
        state_set = set(state)

        possible_operations = []

        if len(neighbor_state) > 0:
            possible_operations.append("MOVE")

        if len(neighbor_state) < self.max_sensors:
                    possible_operations.append("ADD")

        if len(neighbor_state) > 1:
            possible_operations.append("REMOVE")
        
        if not possible_operations:
            return neighbor_state
        
        operation = random.choice(possible_operations)

        if operation == "MOVE":
            idx = random.randint(0, len(neighbor_state) - 1)
            x, y = neighbor_state[idx]

            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            random.shuffle(directions)
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if self.world.is_valid_position(nx, ny) and (nx, ny) not in state_set:
                    neighbor_state[idx] = (nx, ny)
                    break
        elif operation == "ADD":
            for _ in range(100):
                nx = random.randint(0, self.rows - 1)
                ny = random.randint(0, self.cols - 1)
                if self.world.is_valid_position(nx, ny) and (nx, ny) not in state_set:
                    neighbor_state.append((nx, ny))
                    break

        elif operation == "REMOVE":
            idx = random.randint(0, len(neighbor_state) - 1)
            neighbor_state.pop(idx)
                    
        return neighbor_state


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
    
    #test ehsan