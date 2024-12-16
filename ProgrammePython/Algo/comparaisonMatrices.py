import numpy as np

# Variables globales
m = None  # Matrice des coûts
s = None  # Matrice des indices de division

def recensement_chaine_de_matrices(p):
    """Recensement de la chaîne de matrices (calcul du coût minimal)."""
    n = len(p) - 1  # Longueur de p, c'est-à-dire le nombre de matrices
    global m, s
    
    # Initialisation des matrices m et s
    m = np.full((n, n), np.inf)  # Remplir m avec des infinis
    s = np.zeros((n, n), dtype=int)  # Initialisation de s avec des zéros
    
    # Appel à la fonction récursive pour remplir m et s
    return recuperation_chaine(p, 0, n - 1)

def recuperation_chaine(p, i, j):
    """Calcul récursif du coût minimal et de la division optimale."""
    if m[i, j] < np.inf:
        return m[i, j]  # Retourner le coût déjà calculé si c'est mémorisé
    
    if i == j:
        m[i, j] = 0  # Coût de multiplication d'une seule matrice est nul
        return 0
    
    # Si m[i, j] n'a pas encore été calculé
    for k in range(i, j):
        # Calcul récursif du coût pour la division à la position k
        q = recuperation_chaine(p, i, k) + recuperation_chaine(p, k + 1, j) + p[i] * p[k + 1] * p[j + 1]
        
        # Mise à jour de m[i, j] et s[i, j] si une solution plus optimale est trouvée
        if q < m[i, j]:
            m[i, j] = q
            s[i, j] = k
    
    return m[i, j]

def multiplier_chaine_de_matrices(A, s, i, j):
    """Multiplication de la chaîne de matrices en utilisant l'index optimal de s."""
    if i == j:
        return A[i]  # Retourne la matrice A[i] si c'est une seule matrice
    k = s[i, j]  # Obtenir la position optimale pour la division
    # Récursion pour multiplier les sous-chaînes
    X = multiplier_chaine_de_matrices(A, s, i, k)
    Y = multiplier_chaine_de_matrices(A, s, k + 1, j)
    return np.dot(X, Y)  # Multiplier les deux sous-chaînes

# Exemple d'utilisation
if __name__ == "__main__":
    # Dimensions des matrices (exemple)
    p = [30, 35, 15, 5, 10, 20, 25]  # Dimensions: A1 (30x35), A2 (35x15), A3 (15x5), etc.
    
    # Recensement des chaînes de matrices
    recensement_chaine_de_matrices(p)
    
    # Afficher les résultats
    print("Matrice des coûts (m):")
    print(m)
    
    print("\nMatrice des indices de division (s):")
    print(s)
    
    # Exemple de matrices pour multiplier
    A = [np.random.rand(p[i], p[i+1]) for i in range(len(p) - 1)]
    
    # Multiplier la chaîne de matrices avec les indices de division optimaux
    resultat = multiplier_chaine_de_matrices(A, s, 0, len(A) - 1)
    
    print("\nRésultat de la multiplication des matrices :")
    print(resultat)
