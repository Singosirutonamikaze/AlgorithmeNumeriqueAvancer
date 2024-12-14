import heapq
import random
import time
import matplotlib.pyplot as plt
from collections import deque

# 1. BFS pour graphe non pondéré
# 1. BFS pour graphe non pondéré
def bfs(graph, start, end):
    queue = deque([(start, [start])])  # (sommet actuel, chemin parcouru)
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path  # Retourner le chemin dès que le noeud final est trouvé

        for neighbor, _ in graph[node]:  # Ignorez le poids de l'arête
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Si aucun chemin n'est trouvé

# 2. Dijkstra pour graphe pondéré
def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, sommet)
    previous_nodes = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            path.insert(0, start)
            return path, distances[end]

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return None

# 3. Bellman-Ford pour graphe pondéré
def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):  # Nombre d'itérations égale au nombre de sommets - 1
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Détection des cycles négatifs
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Le graphe contient un cycle négatif")

    return distances

# Fonction pour générer un graphe aléatoire (simple)
# Fonction pour générer un graphe aléatoire (simple)
def generate_graph(num_vertices, edge_density=0.5):
    graph = {i: [] for i in range(num_vertices)}  # Initialisation d'un dictionnaire vide pour chaque sommet
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < edge_density:  # Si une arête existe entre i et j
                weight = random.randint(1, 10)  # Poids aléatoire pour l'arête
                graph[i].append((j, weight))  # Ajouter l'arête (sommet, poids) dans le dictionnaire
                graph[j].append((i, weight))  # Ajouter l'arête symétrique (pour un graphe non dirigé)
    return graph

# Fonction pour mesurer le temps d'exécution
def measure_time(algorithm, graph, start, end):
    start_time = time.time()
    algorithm(graph, start, end)
    return time.time() - start_time

# Fonctions pour tester plusieurs tailles de graphes
def test_algorithms(max_size, edge_density=0.5):
    sizes = list(range(5, max_size + 1, 5))  # Tester des tailles de graphes entre 5 et max_size
    bfs_times = []
    dijkstra_times = []
    bellman_times = []

    for size in sizes:
        graph = generate_graph(size, edge_density)
        start_node = 0
        end_node = size - 1

        # Mesurer le temps pour chaque algorithme
        bfs_time = measure_time(bfs, graph, start_node, end_node)
        dijkstra_time = measure_time(dijkstra, graph, start_node, end_node)
        bellman_time = measure_time(lambda g, s, e: bellman_ford(g, s), graph, start_node, end_node)

        bfs_times.append(bfs_time)
        dijkstra_times.append(dijkstra_time)
        bellman_times.append(bellman_time)

    return sizes, bfs_times, dijkstra_times, bellman_times

# Tester les algorithmes avec des graphes de tailles croissantes
sizes, bfs_times, dijkstra_times, bellman_times = test_algorithms(50)

# Tracer les courbes
plt.figure(figsize=(10, 6))
plt.plot(sizes, bfs_times, label="BFS (Non-pondéré)", color="blue", marker='o')
plt.plot(sizes, dijkstra_times, label="Dijkstra (Pondéré)", color="red", marker='o')
plt.plot(sizes, bellman_times, label="Bellman-Ford (Pondéré)", color="green", marker='o')

plt.xlabel('Taille du graphe (Nombre de sommets)')
plt.ylabel('Temps d\'exécution (secondes)')
plt.title('Comparaison des temps d\'exécution des algorithmes de cheminement')
plt.legend()
plt.grid(True)
plt.show()
