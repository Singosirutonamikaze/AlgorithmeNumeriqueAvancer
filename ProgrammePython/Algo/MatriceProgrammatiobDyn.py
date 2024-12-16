import numpy as np

def multiplier_matrices(X, Y):
    """Multiplie deux matrices X et Y."""
    return np.dot(X, Y)

def multiplier_chaine_de_matrices(A, s, i, j):
    """Multiplie une chaîne de matrices A[i] à A[j] en utilisant la matrice s pour les indices optimaux."""
    if j > i:
        k = s[i][j]  # index de la division optimale
        print(f"Diviser la chaîne entre {i} et {j}, à la position {k}")  # Debug
        # Vérification de l'indice k
        if k < i or k >= j:
            print(f"ERREUR: k={k} est en dehors des bornes ({i}, {j})")
            return None  # Valeur invalide, éviter la récursion infinie
        
        X = multiplier_chaine_de_matrices(A, s, i, k)  # multiplication de la sous-chaîne gauche
        Y = multiplier_chaine_de_matrices(A, s, k + 1, j)  # multiplication de la sous-chaîne droite
        if X is None or Y is None:
            return None
        return multiplier_matrices(X, Y)
    else:
        return A[i]

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de matrices (les tailles doivent être compatibles pour la multiplication)
    A = [np.random.rand(30, 35), np.random.rand(35, 15), np.random.rand(15, 5), np.random.rand(5, 10), np.random.rand(10, 20), np.random.rand(20, 25)]

    # Matrice s (exemple de calcul par la programmation dynamique pour la chaîne de matrices)
    s = [
        [0, 1, 2, 2, 3, 3],  # s[0][5] = 3, s[0][2] = 1, s[3][5] = 4 (indexation 0-based)
        [0, 0, 2, 2, 3, 3],
        [0, 0, 0, 2, 3, 3],
        [0, 0, 0, 0, 4, 4],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0]
    ]

    # Calcul du produit de la chaîne de matrices de 0 à 5 (indexation 0-based pour A)
    resultat = multiplier_chaine_de_matrices(A, s, 0, len(A) - 1)
    
    if resultat is not None:
        print("Résultat de la multiplication de la chaîne de matrices :")
        print(resultat)
    else:
        print("Erreur dans la multiplication de la chaîne de matrices.")
