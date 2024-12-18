import numpy as np

def saisir_matrice_parametres():
    """Permet de saisir les matrices des coefficients A et le vecteur des termes constants B tout en vérifiant la validité des entrées."""
    while True:
        try:
            nombre_lignes = int(input("Entrez le nombre de lignes (et colonnes) de la matrice A : "))
            nombre_colonnes = nombre_lignes  # La matrice doit être carrée

            if nombre_lignes <= 0:
                raise ValueError("Les dimensions de la matrice doivent être positives et non nulles.")

            print("Entrez les coefficients de la matrice A ligne par ligne :")
            matrice_A = []
            for ligne_index in range(nombre_lignes):
                ligne = list(map(float, input(f"Ligne {ligne_index + 1} : ").split()))
                if len(ligne) != nombre_colonnes:
                    raise ValueError("Le nombre de coefficients par ligne doit correspondre au nombre de colonnes.")
                matrice_A.append(ligne)

            print("Entrez les coefficients du vecteur B (les termes constants) :")
            vecteur_B = list(map(float, input().split()))

            if len(vecteur_B) != nombre_lignes:
                raise ValueError("Le vecteur B doit avoir un nombre de termes égal au nombre de lignes de la matrice A.")

            return np.array(matrice_A), np.array(vecteur_B)
        except ValueError as error:
            print(f"Erreur : {error}. Veuillez recommencer.")

def afficher_resultats(matrice_A, vecteur_B, solutions, methode):
    """Affiche les matrices saisies, les solutions et les détails."""
    print("\n================= RÉSULTATS =================")
    print("Matrice A :")
    print(matrice_A)
    print("\nVecteur B :")
    print(vecteur_B)
    print(f"\nSolutions par la méthode {methode} :")
    print(solutions)
    print("============================================\n")

def gauss_avec_pivot(matrice_A, vecteur_B):
    nombre_equations = len(vecteur_B)
    matrice_etendue = np.hstack((matrice_A, vecteur_B.reshape(-1, 1)))

    for pivot_index in range(nombre_equations):
        max_ligne = np.argmax(np.abs(matrice_etendue[pivot_index:, pivot_index])) + pivot_index
        if matrice_etendue[max_ligne, pivot_index] == 0:
            raise ValueError("Pas de solution unique.")
        if max_ligne != pivot_index:
            matrice_etendue[[pivot_index, max_ligne]] = matrice_etendue[[max_ligne, pivot_index]]

        for ligne_index in range(pivot_index + 1, nombre_equations):
            facteur = matrice_etendue[ligne_index, pivot_index] / matrice_etendue[pivot_index, pivot_index]
            matrice_etendue[ligne_index, pivot_index:] -= facteur * matrice_etendue[pivot_index, pivot_index:]

    solutions = np.zeros(nombre_equations)
    for ligne_index in range(nombre_equations - 1, -1, -1):
        solutions[ligne_index] = (matrice_etendue[ligne_index, -1] - np.dot(matrice_etendue[ligne_index, ligne_index + 1:], solutions[ligne_index + 1:])) / matrice_etendue[ligne_index, pivot_index]

    return solutions

def gauss_sans_pivot(matrice_A, vecteur_B):
    nombre_equations = len(vecteur_B)
    matrice_etendue = np.hstack((matrice_A, vecteur_B.reshape(-1, 1)))

    for pivot_index in range(nombre_equations):
        if matrice_etendue[pivot_index, pivot_index] == 0:
            raise ValueError("Pas de solution unique.")

        for ligne_index in range(pivot_index + 1, nombre_equations):
            facteur = matrice_etendue[ligne_index, pivot_index] / matrice_etendue[pivot_index, pivot_index]
            matrice_etendue[ligne_index, pivot_index:] -= facteur * matrice_etendue[pivot_index, pivot_index:]

    solutions = np.zeros(nombre_equations)
    for ligne_index in range(nombre_equations - 1, -1, -1):
        solutions[ligne_index] = (matrice_etendue[ligne_index, -1] - np.dot(matrice_etendue[ligne_index, ligne_index + 1:], solutions[ligne_index + 1:])) / matrice_etendue[ligne_index, pivot_index]

    return solutions

def gauss_jordan(matrice_A, vecteur_B):
    nombre_equations = len(vecteur_B)
    matrice_etendue = np.hstack((matrice_A, vecteur_B.reshape(-1, 1)))

    for pivot_index in range(nombre_equations):
        if matrice_etendue[pivot_index, pivot_index] == 0:
            raise ValueError("Pas de solution unique.")
        matrice_etendue[pivot_index] = matrice_etendue[pivot_index] / matrice_etendue[pivot_index, pivot_index]

        for ligne_index in range(nombre_equations):
            if ligne_index != pivot_index:
                matrice_etendue[ligne_index] -= matrice_etendue[ligne_index, pivot_index] * matrice_etendue[pivot_index]

    return matrice_etendue[:, -1]

def decomposition_lu_doolittle(matrice_A):
    nombre_equations = matrice_A.shape[0]
    matrice_L = np.eye(nombre_equations)
    matrice_U = np.zeros_like(matrice_A)

    for pivot_index in range(nombre_equations):
        for colonne_index in range(pivot_index, nombre_equations):
            matrice_U[pivot_index, colonne_index] = matrice_A[pivot_index, colonne_index] - np.dot(matrice_L[pivot_index, :pivot_index], matrice_U[:pivot_index, colonne_index])
        for ligne_index in range(pivot_index + 1, nombre_equations):
            matrice_L[ligne_index, pivot_index] = (matrice_A[ligne_index, pivot_index] - np.dot(matrice_L[ligne_index, :pivot_index], matrice_U[:pivot_index, pivot_index])) / matrice_U[pivot_index, pivot_index]

    return matrice_L, matrice_U

def decomposition_lu_crout(matrice_A):
    nombre_equations = matrice_A.shape[0]
    matrice_L = np.zeros_like(matrice_A)
    matrice_U = np.eye(nombre_equations)

    for pivot_index in range(nombre_equations):
        for colonne_index in range(pivot_index, nombre_equations):
            matrice_L[colonne_index, pivot_index] = matrice_A[colonne_index, pivot_index] - np.dot(matrice_L[colonne_index, :pivot_index], matrice_U[:pivot_index, pivot_index])
        for ligne_index in range(pivot_index + 1, nombre_equations):
            matrice_U[pivot_index, ligne_index] = (matrice_A[pivot_index, ligne_index] - np.dot(matrice_L[pivot_index, :pivot_index], matrice_U[:pivot_index, ligne_index])) / matrice_L[pivot_index, pivot_index]

    return matrice_L, matrice_U

def menu():
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    historique = []

    while True:
        print("\n================= MENU PRINCIPAL =================")
        print("1. Résolution par la méthode de Gauss avec pivot")
        print("2. Résolution par la méthode de Gauss sans pivot")
        print("3. Résolution par la méthode de Gauss-Jordan")
        print("4. Décomposition LU (Doolittle)")
        print("5. Décomposition LU (Crout)")
        print("6. Afficher l'historique des calculs")
        print("7. Quitter")
        print("=================================================")

        choix = input("Entrez votre choix : ")

        if choix == "7":
            print("Au revoir !")
            break

        if choix == "6":
            print("\n======== HISTORIQUE DES CALCULS ========")
            for index, (matrice_A, vecteur_B, resultat, methode) in enumerate(historique, 1):
                print(f"\nCalcul {index} :")
                afficher_resultats(matrice_A, vecteur_B, resultat, methode)
            continue

        if choix not in {"1", "2", "3", "4", "5"}:
            print("Choix invalide. Veuillez entrer un numéro valide.")
            continue

        matrice_A, vecteur_B = saisir_matrice_parametres()
