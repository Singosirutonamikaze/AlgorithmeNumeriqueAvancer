import math

def chaineDeMatricesRec(p, i, j, m):
    # Cas de base : Si i == j, aucune multiplication, retour 0
    if i == j:
        return 0
    else:
        m[i][j] = math.inf  # Initialiser m[i,j] à l'infini
        
        # Essayer toutes les divisions possibles entre i et j
        for k in range(i, j):
            q = (chaineDeMatricesRec(p, i, k, m) + 
                 chaineDeMatricesRec(p, k + 1, j, m) + 
                 p[i - 1] * p[k] * p[j])

            # Mettre à jour m[i, j] si la nouvelle valeur de q est plus petite
            if q < m[i][j]:
                m[i][j] = q
        
        return m[i][j]

# Fonction principale pour appeler le calcul et initialiser m
def matriceMultiplicationChain(p):
    n = len(p) - 1  # n est le nombre de matrices (p contient les tailles des matrices)
    
    # Créer la table m, initialisée à l'infini
    m = [[math.inf] * (n + 1) for _ in range(n + 1)]
    
    # Appeler la fonction de programmation dynamique
    return chaineDeMatricesRec(p, 1, n, m), m

# Exemple d'utilisation
p = [30, 35, 15, 5, 10, 20, 25]  # Tailles des matrices successives
resultat, m = matriceMultiplicationChain(p)

print("Le nombre minimum d'opérations de multiplication est:", resultat)
