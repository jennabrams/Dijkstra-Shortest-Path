import random
import math

# Define the graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Simulated Annealing Algorithm
def simulated_annealing(graph, start, goal, initial_temp=100, cooling_rate=0.95, stopping_temp=1):
    current = start
    path = [start]
    total_cost = 0
    temperature = initial_temp
    
    while temperature > stopping_temp:
        neighbors = list(graph[current].items())
        if not neighbors:
            break
        next_node, cost = random.choice(neighbors)
        
        if next_node not in path:  # avoid cycles
            delta = cost
            acceptance = math.exp(-delta / temperature)
            if delta < 0 or random.random() < acceptance:
                path.append(next_node)
                total_cost += cost
                current = next_node
        
        if current == goal:
            return path, total_cost
        temperature *= cooling_rate
    
    return None

# Run the algorithm
print("Simulated Annealing:", simulated_annealing(graph, 'A', 'D'))
