import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Grafo di esempio
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2},
    'C': {},
}

# Trova i percorsi minimi da il nodo 'A' a tutti gli altri nodi del grafo
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)  # Output: {'A': 
