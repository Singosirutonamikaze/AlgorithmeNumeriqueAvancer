# Algorithme de Bellman-Ford
def bellman_ford(graph, start):
    # Nombre de sommets
    V = len(graph)
    
    # Initialiser les distances à l'infini, sauf la distance du sommet source
    distances = [float("inf")] * V
    distances[start] = 0
    
    # Relaxation des arêtes V-1 fois
    for _ in range(V - 1):
        for u in range(V):
            for v, weight in graph[u]:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Vérification des cycles de poids négatif
    for u in range(V):
        for v, weight in graph[u]:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Le graphe contient un cycle de poids négatif")
                return None
    
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
distances = bellman_ford(graph, start)
print(f"Les distances les plus courtes à partir du sommet {start}: {distances}")
