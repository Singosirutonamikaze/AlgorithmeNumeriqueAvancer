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
        count = [0] * self.V  # Compter le nombre de fois qu'un sommet est mis à jour

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
                        print("Graph contains a negative weight cycle")
                        return None

                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True

        return dist

# Exemple d'utilisation
g = GraphSPFA(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

distances = g.spfa(0)
if distances:
    print("Distances depuis le sommet source :", distances)
