import numpy as np
import time

def SortAnalysis(A):
    """
    Analyse le tri par insertion et retourne le nombre de comparaisons effectuées.
    
    Parameters:
    A (list): Liste d'entiers à trier

    Returns:
    int: Nombre de comparaisons effectuées
    """
    n = len(A)
    comparaisons = 0  # Initialisation du compteur

    for i in range(1, n):
        cle = A[i]
        j = i - 1
        while j >= 0 and A[j] > cle:
            comparaisons += 1  # Compte la comparaison
            A[j + 1] = A[j]
            j -= 1
        if j >= 0:  # Compte la comparaison finale si la boucle s'arrête
            comparaisons += 1
        A[j + 1] = cle

    return comparaisons

# Analyse des comparaisons pour différentes tailles de tableaux
tailles = list(range(1000, 10000, 500))
comparaisons_results = []

for taille in tailles:
    A = np.random.randint(0, 10000, taille)  # Génère un tableau aléatoire
    comparaisons = SortAnalysis(list(A))  # Appelle la fonction avec une copie de A
    comparaisons_results.append((taille, comparaisons))

print("Résultats des comparaisons:", comparaisons_results)

# Analyse du temps d'exécution pour différentes tailles de tableaux
temps_results = []

for taille in tailles:
    A = np.random.randint(0, 10000, taille)  # Génère un tableau aléatoire
    start_time = time.time()
    SortAnalysis(list(A))  # Appelle la fonction avec une copie de A
    end_time = time.time()
    temps_results.append((taille, (end_time - start_time) * 1000))  # Temps en millisecondes

print("Résultats des temps d'exécution:", temps_results)
