from itertools import combinations
def held_karp(distances):
    n = len(distances)
    # Initialiser la structure de données pour stocker les sous-problèmes
    OPT = {}

    # Étape 1 : Initialisation pour les sous-ensembles de taille 1
    for i in range(1, n):  # Index des villes {c2, ..., cn}
        OPT[(frozenset([i]), i)] = distances[0][i]

    # Étape 2 : Construction des sous-problèmes
    for subset_size in range(2, n):  # Taille des sous-ensembles (j)
        for subset in combinations(range(1, n), subset_size):  # Sous-ensembles S
            subset = frozenset(subset)
            for current in subset:  # Ville ci (arrivée)
                # Calcul de la distance minimale
                OPT[(subset, current)] = min(
                    OPT[(subset - frozenset([current]), prev)] + distances[prev][current]
                    for prev in subset if prev != current
                )

    # Étape 3 : Résolution finale
    full_set = frozenset(range(1, n))  # Toutes les villes {c2, ..., cn}
    return min(
        OPT[(full_set, last)] + distances[last][0]  # Retour à c1
        for last in range(1, n)
    )

# Exemple d'utilisation :
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Distance minimale :", held_karp(distances))