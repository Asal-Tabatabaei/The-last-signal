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

        if not state:
            return len(self.targets) * 100 

        covered_targets = set()
        overlap_penalty = 0
        
        covered_cells = {}

        for (sx, sy) in state:
            min_r = max(0, sx - self.sensor_range)
            max_r = min(self.rows - 1, sx + self.sensor_range)
            
            for i in range(min_r, max_r + 1):
                remaining_dist = self.sensor_range - abs(sx - i)
                min_c = max(0, sy - remaining_dist)
                max_c = min(self.cols - 1, sy + remaining_dist)
                
                for j in range(min_c, max_c + 1):
                    covered_cells[(i, j)] = covered_cells.get((i, j), 0) + 1
                    
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

    def initialize_state(self):
        
        num_sensors = random.randint(1, self.max_sensors)

        initialize_state_set = set()

        attempts = 0
        while len(initialize_state_set) < num_sensors and attempts < 1000:
            attempts +=1
        
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)

            if self.world.is_valid_position(x, y) and (x,y) not in initialize_state_set:
                initialize_state_set.add((x,y))

        return list(initialize_state_set) 

