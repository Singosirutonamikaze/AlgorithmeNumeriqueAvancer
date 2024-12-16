import numpy as np
import time
import matplotlib.pyplot as plt

# Algorithmes de multiplication de matrices

# Algorithme naïf
def multiplication_naive(A):
    """Multiplication naïve de matrices."""
    result = A[0]
    for matrix in A[1:]:
        result = np.dot(result, matrix)
    return result

# Algorithme de programmation dynamique pour multiplication de chaînes de matrices
def recensement_chaine_de_matrices(p):
    """Recensement de la chaîne de matrices (calcul du coût minimal)."""
    n = len(p) - 1
    global m, s
    
    # Initialisation des matrices m et s
    m = np.full((n, n), np.inf)
    s = np.zeros((n, n), dtype=int)
    
    # Appel à la fonction récursive pour remplir m et s
    return recuperation_chaine(p, 0, n - 1)

def recuperation_chaine(p, i, j):
    """Calcul récursif du coût minimal et de la division optimale."""
    if m[i, j] < np.inf:
        return m[i, j]
    
    if i == j:
        m[i, j] = 0
        return 0
    
    for k in range(i, j):
        q = recuperation_chaine(p, i, k) + recuperation_chaine(p, k + 1, j) + p[i] * p[k + 1] * p[j + 1]
        
        if q < m[i, j]:
            m[i, j] = q
            s[i, j] = k
    
    return m[i, j]

def multiplier_chaine_de_matrices(A, s, i, j):
    """Multiplication de la chaîne de matrices en utilisant l'index optimal de s."""
    if i == j:
        return A[i]
    k = s[i, j]
    X = multiplier_chaine_de_matrices(A, s, i, k)
    Y = multiplier_chaine_de_matrices(A, s, k + 1, j)
    return np.dot(X, Y)

# Fonction pour mesurer le temps d'exécution d'un algorithme
def mesurer_temps_algo(algo, *args):
    start_time = time.time()
    algo(*args)
    return time.time() - start_time

# Test avec des tailles croissantes de matrices
sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
times_naive = []
times_dynamic = []

# Tester pour différentes tailles de matrices
for size in sizes:
    p = np.random.randint(10, 100, size=size + 1)  # Dimensions des matrices
    A = [np.random.rand(p[i], p[i+1]) for i in range(len(p) - 1)]  # Matrices à multiplier
    
    # Mesurer le temps pour l'algorithme naïf
    time_naive = mesurer_temps_algo(multiplication_naive, A)
    times_naive.append(time_naive)
    
    # Mesurer le temps pour l'algorithme de programmation dynamique
    recensement_chaine_de_matrices(p)
    time_dynamic = mesurer_temps_algo(multiplier_chaine_de_matrices, A, s, 0, len(A) - 1)
    times_dynamic.append(time_dynamic)

# Tracer les résultats
plt.plot(sizes, times_naive, label="Naïf", color='red')
plt.plot(sizes, times_dynamic, label="Dynamique", color='blue')
plt.xlabel('Taille de la chaîne de matrices')
plt.ylabel('Temps d\'exécution (secondes)')
plt.title('Comparaison des performances des algorithmes de multiplication de matrices')
plt.legend()
plt.grid(True)
plt.show()
