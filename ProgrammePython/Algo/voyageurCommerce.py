import itertools
import math

# Calculer la distance entre deux points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculer la longueur d'un chemin donné
def calculate_total_distance(path, points):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance(points[path[i]], points[path[i + 1]])
    total_distance += distance(points[path[-1]], points[path[0]])  # Retour au point de départ
    return total_distance

# Résoudre le TSP par brute force
def solve_tsp(points):
    # Créer une liste des indices des points
    n = len(points)
    all_permutations = itertools.permutations(range(n))

    min_distance = float('inf')
    best_path = None

    # Essayer toutes les permutations
    for perm in all_permutations:
        current_distance = calculate_total_distance(perm, points)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm

    return best_path, min_distance

# Exemple d'utilisation
if __name__ == "__main__":
    # Coordonnées des points (x, y)
    points = [(0, 0), (1, 3), (4, 3), (6, 1), (3, 0)]

    # Résoudre le TSP
    best_path, min_distance = solve_tsp(points)

    # Afficher le résultat
    print("Meilleur chemin :", best_path)
    print("Distance totale :", min_distance)
