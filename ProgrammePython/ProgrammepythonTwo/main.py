import numpy as np

def factorisation_lu_avec_pivot(A):
    """
    Effectue la factorisation LU avec pivot partiel.
    
    :param A: Matrice carrée (numpy array, n x n)
    :return: Matrices L (triangulaire inférieure), U (triangulaire supérieure), et P (matrice de permutation)
    """
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)
    U = A.astype(float).copy()
    P = np.eye(n)
    
    for k in range(n - 1):
        # Recherche du pivot maximal en valeur absolue
        ligne_pivot = np.argmax(abs(U[k:, k])) + k
        if U[ligne_pivot, k] == 0:
            raise ValueError("Matrice singulière : pas de pivot possible.")
        
        # Permutation des lignes dans U et P
        U[[k, ligne_pivot]] = U[[ligne_pivot, k]]
        P[[k, ligne_pivot]] = P[[ligne_pivot, k]]
        if k > 0:
            L[[k, ligne_pivot], :k] = L[[ligne_pivot, k], :k]
        
        # Calcul des coefficients de L et mise à jour de U
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    
    np.fill_diagonal(L, 1)
    return L, U, P

def resoudre_triangulaire_inferieure(L, B):
    """
    Résout le système LX = B pour une matrice triangulaire inférieure L.
    
    :param L: Matrice triangulaire inférieure (numpy array, n x n)
    :param B: Vecteur des constantes (numpy array, taille n)
    :return: Vecteur solution X (numpy array, taille n)
    """
    n = B.size
    X = np.zeros_like(B, dtype=float)
    for i in range(n):
        X[i] = (B[i] - np.dot(L[i, :i], X[:i])) / L[i, i]
    return X

def resoudre_triangulaire_superieure(U, B):
    """
    Résout le système UX = B pour une matrice triangulaire supérieure U.
    
    :param U: Matrice triangulaire supérieure (numpy array, n x n)
    :param B: Vecteur des constantes (numpy array, taille n)
    :return: Vecteur solution X (numpy array, taille n)
    """
    n = B.size
    X = np.zeros_like(B, dtype=float)
    for i in range(n - 1, -1, -1):
        X[i] = (B[i] - np.dot(U[i, i + 1:], X[i + 1:])) / U[i, i]
    return X

def resoudre_systeme_avec_lu(A, B):
    """
    Résout le système AX = B en utilisant la factorisation LU avec pivot.
    
    :param A: Matrice des coefficients (numpy array, n x n)
    :param B: Vecteur des constantes (numpy array, taille n)
    :return: Vecteur solution X (numpy array, taille n)
    """
    L, U, P = factorisation_lu_avec_pivot(A)
    # Résolution de Ly = Pb
    Pb = np.dot(P, B)
    Y = resoudre_triangulaire_inferieure(L, Pb)
    # Résolution de Ux = y
    X = resoudre_triangulaire_superieure(U, Y)
    return X

def saisir_matrice_et_vecteur():
    """
    Permet à l'utilisateur de saisir la matrice A et le vecteur B.
    
    :return: La matrice A et le vecteur B sous forme de numpy arrays
    """
    n = int(input("Entrez la taille de la matrice carrée A (n x n) : "))
    print(f"Entrez les {n} lignes de la matrice A, avec les éléments séparés par des espaces :")
    A = np.array([list(map(float, input(f"Ligne {i + 1} : ").split())) for i in range(n)])
    print("Entrez les éléments du vecteur B séparés par des espaces :")
    B = np.array(list(map(float, input("B : ").split())))
    
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matrice A doit être carrée.")
    if B.size != A.shape[0]:
        raise ValueError("Le vecteur B doit avoir une taille compatible avec A.")
    
    return A, B

if __name__ == "__main__":
    print("Résolution d'un système linéaire AX = B par factorisation LU")
    try:
        A, B = saisir_matrice_et_vecteur()
        solution = resoudre_systeme_avec_lu(A, B)
        print("Solution du système AX = B :")
        print(solution)
    except ValueError as e:
        print("Erreur :", e)
