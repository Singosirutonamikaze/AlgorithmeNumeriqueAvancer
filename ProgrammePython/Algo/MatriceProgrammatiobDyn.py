def cout_multiplication_prog_dynamique(dimensions):
    """
    Calcule le nombre minimal de multiplications scalaires nécessaires pour multiplier une chaîne de matrices.
    
    :param dimensions: Liste des dimensions des matrices, où la matrice Ai a pour dimensions dimensions[i-1] x dimensions[i].
    :return: Nombre minimal de multiplications scalaires.
    """
    n = len(dimensions) - 1  # Nombre de matrices
    # Initialisation de la matrice des coûts
    m = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    
    # Remplissage de la matrice des coûts
    for l in range(2, n + 1):  # l est la longueur de la chaîne considérée
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[0][n - 1]

# Exemple d'utilisation
dimensions = [10, 20, 30, 40, 30]  # Dimensions des matrices
resultat = cout_multiplication_prog_dynamique(dimensions)
print(f"Nombre minimal de multiplications scalaires : {resultat}")
