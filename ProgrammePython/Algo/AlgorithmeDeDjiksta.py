import heapq

# Algorithme de Dijkstra
def dijkstra(graph, start):
    V = len(graph)
    # Distance initiale à l'infini
    distances = [float("inf")] * V
    distances[start] = 0
    
    # Utilisation d'une file de priorité pour gérer les sommets à explorer
    pq = [(0, start)]  # (distance, sommet)
    
    while pq:
        # Extraire le sommet avec la distance minimale
        current_distance, u = heapq.heappop(pq)
        
        # Si cette distance est déjà dépassée, on passe au suivant
        if current_distance > distances[u]:
            continue
        
        # Exploration des voisins
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return distances

# Exemple d'utilisation
# Représentation du graphe sous forme d'adjacence (u, v, poids)
graph = [
    [(1, 5), (2, 2)],  # Sommet 0
    [(2, 3), (3, 1)],  # Sommet 1
    [(3, 4)],          # Sommet 2
    []                 # Sommet 3
]

start = 0
distances = dijkstra(graph, start)
print(f"Les distances les plus courtes à partir du sommet {start}: {distances}")
