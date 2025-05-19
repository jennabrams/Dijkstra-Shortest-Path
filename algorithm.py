import heapq

# Define the graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Dummy heuristic values for A* (must be optimistic/lower than or equal to actual cost)
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

# A* Algorithm
def a_star(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start, [])]
    visited = set()
    
    while open_set:
        est_total, cost_so_far, current, path = heapq.heappop(open_set)
        
        if current in visited:
            continue
        
        path = path + [current]
        visited.add(current)
        
        if current == goal:
            return path, cost_so_far
        
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(open_set, (
                    cost_so_far + weight + heuristic[neighbor],
                    cost_so_far + weight,
                    neighbor,
                    path
                ))
    
    return None

# Run the A* algorithm
print("A* result:", a_star(graph, 'A', 'D', heuristic))
