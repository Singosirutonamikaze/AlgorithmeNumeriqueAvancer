import time
import random
import matplotlib.pyplot as plt

# Algorithme de Bellman-Ford classique
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        dist = [float('inf')] * self.V
        dist[source] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return None  # Cycle négatif détecté
        return dist

# Algorithme SPFA optimisé
from collections import deque

class GraphSPFA:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))

    def spfa(self, source):
        dist = [float('inf')] * self.V
        in_queue = [False] * self.V
        count = [0] * self.V

        dist[source] = 0
        queue = deque([source])
        in_queue[source] = True

        while queue:
            u = queue.popleft()
            in_queue[u] = False

            for v, weight in self.adj_list[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    count[v] += 1

                    if count[v] >= self.V:  # Détection de cycle négatif
                        return None  # Cycle négatif détecté

                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
        return dist

# Fonction pour mesurer le temps d'exécution
def measure_time(graph, source, algorithm_type):
    start_time = time.time()
    if algorithm_type == 'bf':
        graph.bellman_ford(source)
    elif algorithm_type == 'spfa':
        graph.spfa(source)
    return time.time() - start_time

# Comparaison des algorithmes pour différentes tailles de graphes
def compare_algorithms(max_size, step_size):
    sizes = list(range(10, max_size+1, step_size))
    bf_times = []
    spfa_times = []

    for size in sizes:
        # Générer un graphe avec `size` sommets et arêtes aléatoires
        g_bf = Graph(size)
        g_spfa = GraphSPFA(size)

        # Ajouter des arêtes aléatoires
        for _ in range(size * 2):
            u, v = random.randint(0, size-1), random.randint(0, size-1)
            weight = random.randint(-10, 10)
            g_bf.add_edge(u, v, weight)
            g_spfa.add_edge(u, v, weight)

        # Mesurer le temps d'exécution de Bellman-Ford
        bf_time = measure_time(g_bf, 0, 'bf')
        bf_times.append(bf_time)

        # Mesurer le temps d'exécution de SPFA
        spfa_time = measure_time(g_spfa, 0, 'spfa')
        spfa_times.append(spfa_time)

    return sizes, bf_times, spfa_times

# Tracer la comparaison des deux algorithmes
def plot_comparison(sizes, bf_times, spfa_times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bf_times, label='Bellman-Ford', marker='o')
    plt.plot(sizes, spfa_times, label='SPFA', marker='x')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison des algorithmes Bellman-Ford et SPFA')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main pour lancer la comparaison
if __name__ == "__main__":
    max_size = 200  # Nombre maximal de sommets
    step_size = 20  # Incrément des tailles de graphes
    sizes, bf_times, spfa_times = compare_algorithms(max_size, step_size)
    plot_comparison(sizes, bf_times, spfa_times)
