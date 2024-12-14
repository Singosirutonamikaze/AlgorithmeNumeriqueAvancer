from collections import deque

# Algorithme de BFS pour trouver le plus court chemin dans un graphe non pondéré
def bfs(graph, start, end):
    queue = deque([(start, [start])])  # (sommet actuel, chemin parcouru)
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path  # Retourner le chemin dès que le noeud final est trouvé

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Si aucun chemin n'est trouvé

# Exemple de graphe (représentation par une liste d'adjacence)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Exemple d'utilisation
start_node = 'A'
end_node = 'F'
path = bfs(graph, start_node, end_node)
if path:
    print(f"Le chemin le plus court de {start_node} à {end_node} est : {path}")
else:
    print(f"Aucun chemin trouvé de {start_node} à {end_node}")
