import random
import time
import matplotlib.pyplot as plt
import heapq

# Algorithme de Bellman-Ford
def bellman_ford(graph, start):
    V = len(graph)
    distances = [float("inf")] * V
    distances[start] = 0
    for _ in range(V - 1):
        for u in range(V):
            for v, weight in graph[u]:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances

# Algorithme de Dijkstra
def dijkstra(graph, start):
    V = len(graph)
    distances = [float("inf")] * V
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, u = heapq.heappop(pq)
        if current_distance > distances[u]:
            continue
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    return distances

# Générer un graphe aléatoire
def generate_random_graph(V, E):
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u = random.randint(0, V - 1)
        v = random.randint(0, V - 1)
        weight = random.randint(1, 10)
        graph[u].append((v, weight))
    return graph

# Mesurer le temps d'exécution
def measure_time(graph, start):
    # Mesurer le temps pour Bellman-Ford
    start_time = time.time()
    bellman_ford(graph, start)
    bellman_ford_time = time.time() - start_time
    
    # Mesurer le temps pour Dijkstra
    start_time = time.time()
    dijkstra(graph, start)
    dijkstra_time = time.time() - start_time
    
    return bellman_ford_time, dijkstra_time

# Paramètres
V_values = [10, 20, 30, 40, 50, 100]  # Tailles de graphes à tester
E_values = [20, 50, 100, 150, 200, 500]  # Nombre d'arêtes
times_bf = []
times_dijkstra = []

# Mesurer le temps pour chaque taille de graphe
for V, E in zip(V_values, E_values):
    graph = generate_random_graph(V, E)
    bf_time, dijkstra_time = measure_time(graph, 0)
    times_bf.append(bf_time)
    times_dijkstra.append(dijkstra_time)

# Tracer les courbes
plt.plot(V_values, times_bf, label="Bellman-Ford", marker='o')
plt.plot(V_values, times_dijkstra, label="Dijkstra", marker='x')
plt.xlabel("Nombre de sommets (V)")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Comparaison de la vitesse entre Bellman-Ford et Dijkstra")
plt.legend()
plt.grid(True)
plt.show()
