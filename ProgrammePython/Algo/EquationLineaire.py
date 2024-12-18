from itertools import product

def F3(d1, d2):
    """
    Sous-problème F3 : maximiser la fonction pour x1, x2, x3
    avec des contraintes réduites (d1, d2).
    """
    max_value = 0
    for x1, x2, x3 in product(range(d1 + 1), range(d1 + 1), range(d1 + 1)):
        # Contraintes
        if 4 * x1 + 6 * x2 + 5 * x3 <= d1 and 3 * x1 + 6 * x2 + 4 * x3 <= d2:
            value = 6 * x1 + 9 * x2 + 8 * x3  # Fonction objectif
            max_value = max(max_value, value)
    return max_value

def F4(d1, d2):
    """
    Sous-problème F4 : maximiser la fonction en incluant x4.
    """
    max_value = 0
    for x4 in range(min(d1 // 4 + 1, d2 // 3 + 1)):
        # Contraintes pour les sous-problèmes F3
        remaining_d1 = d1 - 4 * x4
        remaining_d2 = d2 - 3 * x4
        if remaining_d1 >= 0 and remaining_d2 >= 0:
            value = 4 * x4 + F3(remaining_d1, remaining_d2)
            max_value = max(max_value, value)
    return max_value

# Résolution du problème pour d = (8, 7)
d1, d2 = 8, 7
optimal_value = F4(d1, d2)
print(f"Valeur optimale de F*: {optimal_value}")
