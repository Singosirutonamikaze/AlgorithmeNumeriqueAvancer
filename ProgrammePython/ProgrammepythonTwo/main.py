from methodeDeResolution import *
from FonctionDuMain import *
import numpy as np

def gauss_elimination(A, B):
    """
    Résout le système d'équations linéaires AX = B en utilisant la méthode de Gauss.
    
    :param A: Matrice des coefficients (numpy array)
    :param B: Vecteur des constantes (numpy array)
    :return: Vecteur solution X (numpy array)
    """
    # Convertir A et B en matrices flottantes pour éviter des erreurs d'entiers
    A = A.astype(float)
    B = B.astype(float)
    n = len(B)  # Taille du système (nombre d'équations)
    
    # Étape 1 : Transformation de la matrice en une matrice triangulaire supérieure
    for i in range(n):
        # Vérification si le pivot est nul
        if A[i, i] == 0:
            raise ValueError("Pivot nul détecté, résolution impossible.")
        
        # Normalisation de la ligne (rendre le pivot égal à 1)
        pivot = A[i, i]
        A[i] = A[i] / pivot
        B[i] = B[i] / pivot
        
        # Élimination des éléments sous le pivot
        for j in range(i + 1, n):
            facteur = A[j, i]
            A[j] = A[j] - facteur * A[i]
            B[j] = B[j] - facteur * B[i]
    
    # Étape 2 : Résolution par substitution arrière
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = B[i] - np.dot(A[i, i + 1:], X[i + 1:])
    
    return X


# Exemple d'utilisation
if __name__ == "__main__":
    # Matrice des coefficients A
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]])
    
    # Vecteur des constantes B
    B = np.array([8, -11, -3])
    
    # Résolution du système
    try:
        solution = gauss_elimination(A, B)
        print("Solution du système AX = B :", solution)
    except ValueError as e:
        print("Erreur :", e)
