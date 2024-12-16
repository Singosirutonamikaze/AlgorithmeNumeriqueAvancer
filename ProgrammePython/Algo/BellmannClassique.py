class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        dist = [float('inf')] * self.V
        dist[source] = 0

        # Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains a negative weight cycle")
                return None

        return dist

# Exemple d'utilisation
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

distances = g.bellman_ford(0)
if distances:
    print("Distances depuis le sommet source :", distances)
