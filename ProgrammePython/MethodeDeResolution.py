import math
from operator import pos
import sys

# Fonction pour la méthode de dichotomie avec affichage des intervalles
def methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    # Évaluation de la fonction aux bornes initiales
    valeur_borne_inferieure = fonction(borne_inferieure)
    valeur_borne_superieure = fonction(borne_superieure)

    # Vérifie si les bornes sont déjà proches de la racine
    if math.fabs(valeur_borne_inferieure) <= tolerance:
        return borne_inferieure
    if math.fabs(valeur_borne_superieure) <= tolerance:
        return borne_superieure

    # Vérifie que la racine est bien encadrée entre les bornes
    if valeur_borne_inferieure * valeur_borne_superieure > 0.0:
        print(f"La racine n'est pas encadrée entre [{borne_inferieure}, {borne_superieure}].")
        sys.exit(0)

    # Calcul du nombre maximum d'itérations nécessaire en théorie (pour la précision)
    nombre_iterations = int(math.ceil(math.log(math.fabs(borne_superieure - borne_inferieure) / tolerance) / math.log(2.0)))

    for iteration in range(min(nombre_iterations + 1, nombre_max_iterations)):
        # Calcul du point milieu
        point_milieu = (borne_inferieure + borne_superieure) * 0.5
        # Évaluation de la fonction au point milieu
        valeur_point_milieu = fonction(point_milieu)

        # Affiche l'intervalle actuel à chaque itération
        print(f"Iteration {iteration + 1}: Intervalle actuel = [{borne_inferieure}, {borne_superieure}]")

        # Vérifie si le point milieu est proche de la racine (tolérance)
        if math.fabs(valeur_point_milieu) <= tolerance or (borne_superieure - borne_inferieure) < tolerance:
            print(f"Solution trouvée : x = {point_milieu} après {iteration + 1} itérations")
            return point_milieu

        # Met à jour les bornes en fonction de la position de la racine
        if valeur_point_milieu * valeur_borne_superieure < 0.0:
            borne_inferieure = point_milieu
            valeur_borne_inferieure = valeur_point_milieu
        else:
            borne_superieure = point_milieu
            valeur_borne_superieure = valeur_point_milieu

    # Retourne la moyenne des bornes comme approximation de la racine
    return (borne_inferieure + borne_superieure) * 0.5

# Fonction pour la méthode de la sécante
def methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    # Évaluation de la fonction aux bornes initiales
    valeur_borne_inferieure = fonction(borne_inferieure)
    valeur_borne_superieure = fonction(borne_superieure)

    # Vérifie si les bornes sont déjà proches de la racine
    if math.fabs(valeur_borne_inferieure) <= tolerance:
        return borne_inferieure
    if math.fabs(valeur_borne_superieure) <= tolerance:
        return borne_superieure

    # Vérifie que la racine est bien encadrée entre les bornes
    if valeur_borne_inferieure * valeur_borne_superieure > 0.0:
        print(f"La racine n'est pas encadrée entre [{borne_inferieure}, {borne_superieure}].")
        sys.exit(0)

    compteur_iterations = 0
    # La méthode de la sécante s'applique en itérant jusqu'à ce que la tolérance soit atteinte
    while (math.fabs(borne_superieure - borne_inferieure) > tolerance and compteur_iterations < nombre_max_iterations):
        compteur_iterations += 1
        # Calcul de la nouvelle estimation de la racine
        estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure)
        # Évaluation de la fonction à cette estimation
        valeur_estimation = fonction(estimation)

        # Si l'estimation est proche de la racine, on retourne cette estimation
        if math.fabs(valeur_estimation) <= tolerance:
            return estimation

        # Mise à jour des bornes en fonction du signe de f(estimation)
        if valeur_estimation * valeur_borne_superieure < 0.0:
            borne_inferieure = estimation
            valeur_borne_inferieure = valeur_estimation
        else:
            borne_superieure = estimation
            valeur_borne_superieure = valeur_estimation

    # Retourne l'estimation après l'itération
    return (borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure))

# Fonction pour la méthode de Newton-Raphson
def methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale
    # Évaluation de la fonction à la valeur initiale
    valeur_x = fonction(x)

    # La méthode de Newton-Raphson itère jusqu'à ce que la tolérance soit atteinte
    while math.fabs(valeur_x) > tolerance and compteur_iterations < nombre_max_iterations:
        # Calcul de la dérivée de la fonction en x
        valeur_derivee_x = derivee_fonction(x)

        # Vérifie si la dérivée est nulle (évite la division par zéro)
        if valeur_derivee_x == 0:
            print("La dérivée est nulle. L'implémentation de la méthode de Newton échoue.")
            return None

        # Mise à jour de la valeur de x selon la méthode de Newton-Raphson
        x -= valeur_x / valeur_derivee_x
        valeur_x = fonction(x)
        compteur_iterations += 1

    if compteur_iterations == nombre_max_iterations:
        print("Pas de convergence avec la méthode de Newton.")
        return None
    else:
        return x

# Fonction pour la méthode du point fixe
def methode_du_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale

    # La méthode du point fixe itère jusqu'à ce que la différence entre x et phi(x) soit inférieure à la tolérance
    while math.fabs(phi(x) - x) > tolerance and compteur_iterations < nombre_max_iterations:
        x = phi(x)
        compteur_iterations += 1

    # Vérification de la convergence
    if compteur_iterations == nombre_max_iterations:
        print("Pas de convergence avec la méthode du point fixe.")
        return None
    else:
        return x

# Méthode de balayage avec affichage des intervalles
def methode_de_balayage(fonction, borne_inferieure, borne_superieure, pas, tolerance):
    # Début de la variable à la borne inférieure
    variable_x = borne_inferieure
    print("Début du balayage :")
    
    # Parcours de l'intervalle
    while variable_x <= borne_superieure:
        print(f"Intervalle : [{variable_x}, {variable_x + pas}]")
        # Vérifie si la fonction change de signe entre les deux bornes
        if fonction(variable_x) * fonction(variable_x + pas) < 0:
            # Si oui, utilise la méthode de dichotomie pour trouver la racine
            racine = methode_de_dichotomie(fonction, variable_x, variable_x + pas, tolerance, 100)
            if racine is not None:
                return racine
        
        # On passe à l'intervalle suivant
        variable_x += pas

    print("Aucune racine trouvée dans l'intervalle donné.")
    return None

# Méthode de balayage pour Newton-Raphson
def balayage_newton(fonction, derivee_fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    # Calcul du pas de balayage
    pas_de_balayage = (borne_superieure - borne_inferieure) / 5
    # Initialisation de la valeur initiale de x
    x_initiale = borne_inferieure

    print("Balayage pour trouver une valeur initiale convenable pour Newton-Raphson")
    
    # Essai de différentes valeurs initiales pour Newton-Raphson
    while x_initiale <= borne_superieure:
        print(f"Essai avec x_initiale = {x_initiale}")
        # Applique la méthode de Newton-Raphson
        solution = methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations)
        if solution is not None:
            print(f"Solution trouvée avec x_initiale = {x_initiale}: x = {solution}")
            return solution
        # On passe à l'intervalle suivant
        x_initiale += pos

    print("Aucune solution trouvée pour Newton-Raphson avec le balayage.")
    return None