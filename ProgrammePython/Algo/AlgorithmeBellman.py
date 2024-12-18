def bellman_ford(graph, start):
    # Nombre de sommets dans le graphe
    V = len(graph)
    
    # Initialiser les distances à l'infini, sauf la distance du sommet de départ
    distances = [float("inf")] * V  # Crée une liste de distances infinies
    distances[start] = 0  # La distance du sommet de départ à lui-même est 0
    
    # Relaxation des arêtes du graphe V-1 fois (où V est le nombre de sommets)
    # Cela garantit que toutes les distances les plus courtes sont trouvées
    for _ in range(V - 1):
        # Parcours de chaque sommet
        for u in range(V):
            # Parcours des voisins de chaque sommet
            for v, weight in graph[u]:
                # Vérification si on peut améliorer la distance pour v en passant par u
                # Si la distance actuelle de u est différente de "infini" (indiquant que u a été atteint)
                # et que la distance d(u) + le poids de l'arête (u, v) est plus petite que d(v),
                # alors on met à jour la distance pour v
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Vérification des cycles de poids négatif
    # Si, après avoir effectué V-1 relaxations, il existe encore une arête dont la distance peut être améliorée,
    # cela signifie qu'il y a un cycle de poids négatif dans le graphe.
    for u in range(V):
        for v, weight in graph[u]:
            # Si on peut encore améliorer la distance pour v, cela indique un cycle négatif
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Le graphe contient un cycle de poids négatif")
                return None
    
    # Si aucun cycle de poids négatif n'a été détecté, retourner la liste des distances les plus courtes
    return distances

# Exemple d'utilisation de l'algorithme de Bellman-Ford
# Représentation du graphe sous forme de liste d'adjacence, où chaque sommet u a une liste de paires (v, poids)
graph = [
    [(1, 5), (2, 2)],  # Sommet 0 : voisins (1, 5) et (2, 2)
    [(2, 3), (3, 1)],  # Sommet 1 : voisins (2, 3) et (3, 1)
    [(3, 4)],          # Sommet 2 : voisin (3, 4)
    []                 # Sommet 3 : pas de voisins
]

start = 0  # Sommet de départ
distances = bellman_ford(graph, start)  # Appel de l'algorithme de Bellman-Ford
# Affichage des distances les plus courtes depuis le sommet de départ
print(f"Les distances les plus courtes à partir du sommet {start}: {distances}")
 