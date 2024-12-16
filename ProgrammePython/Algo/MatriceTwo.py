import math

def ordonnerChaineDeMatrices(p):
    n = len(p) - 1  # Nombre de matrices (taille de p - 1)
    
    # Initialiser les matrices m et s
    m = [[0] * (n + 1) for _ in range(n + 1)]  # m[i][j] contient le minimum des multiplications
    s = [[0] * (n + 1) for _ in range(n + 1)]  # s[i][j] contient l'indice optimal k
    
    # Remplir m et s selon l'algorithme
    for i in range(1, n + 1):
        m[i][i] = 0  # Aucune multiplication pour une seule matrice
    
    for z in range(2, n + 1):  # z est la longueur de la chaîne
        for i in range(1, n - z + 2):  # i est l'indice de la matrice de début
            j = i + z - 1  # j est l'indice de la matrice de fin
            m[i][j] = math.inf  # Initialiser m[i,j] à l'infini
            
            for k in range(i, j):  # k est l'indice où on coupe la chaîne
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                
                # Mettre à jour m[i,j] et s[i,j] si on trouve un nombre d'opérations plus faible
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return m, s

# Exemple d'utilisation
p = [30, 35, 15, 5, 10, 20, 25]  # Tailles des matrices successives
m, s = ordonnerChaineDeMatrices(p)

# Afficher les matrices m et s
print("Matrice m (nombre minimum d'opérations):")
for row in m[1:]:
    print(row[1:])

print("\nMatrice s (index optimal de division):")
for row in s[1:]:
    print(row[1:])
