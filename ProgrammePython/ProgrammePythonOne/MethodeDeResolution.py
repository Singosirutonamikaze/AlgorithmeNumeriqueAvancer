#Importation des modules necessaires
import math
from fonctionsTableaux import *
from sympy import *
from sympy.calculus.util import *
from sympy.sets.sets import *

# Fonction pour la méthode de la dichotomie avec affichage des intervalles
def methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    tableau_interactions = []

    # Fonction pour vérifier que la fonction est correctement encadrée
    def est_encadree(fonction, borne_inferieure, borne_superieure):
        try:
            valeur_borne_inferieure = fonction(borne_inferieure)
            valeur_borne_superieure = fonction(borne_superieure)
            
            if valeur_borne_inferieure * valeur_borne_superieure > 0.0:
                print(f"La racine n'est pas encadrée entre [{borne_inferieure}, {borne_superieure}].")
                return False
            return True
        except Exception as e:
            print(f"Erreur lors de l'évaluation de la fonction : {e}")
            return False

    # Vérifie si les bornes sont déjà proches de la racine
    try:
        valeur_borne_inferieure = fonction(borne_inferieure)
        valeur_borne_superieure = fonction(borne_superieure)
    except Exception as e:
        print(f"Erreur dans l'évaluation de la fonction : {e}")
        return None

    if math.fabs(valeur_borne_inferieure) <= tolerance:
        return borne_inferieure, tableau_interactions
    if math.fabs(valeur_borne_superieure) <= tolerance:
        return borne_superieure, tableau_interactions

    # Si les bornes ne sont pas encadrées, redemander une nouvelle fonction et vérifier
    while not est_encadree(fonction, borne_inferieure, borne_superieure):
        print("Veuillez saisir une nouvelle fonction qui encadre bien la racine.")
        return None

    # Calcul du nombre maximum d'itérations nécessaire en théorie
    nombre_iterations = int(math.ceil(math.log(math.fabs(borne_superieure - borne_inferieure) / tolerance) / math.log(2.0)))

    for iteration in range(min(nombre_iterations + 1, nombre_max_iterations)):
        # Calcul du point milieu
        point_milieu = (borne_inferieure + borne_superieure) * 0.5
        try:
            # Chercher la valeur image du point milieu
            valeur_point_milieu = fonction(point_milieu)
        except Exception as e:
            print(f"Erreur lors de l'évaluation de la fonction au point milieu : {e}")
            return None, tableau_interactions

        # Affiche l'intervalle actuel à chaque itération
        print(f"Iteration {iteration + 1}: Intervalle actuel = [{borne_inferieure}, {borne_superieure}]")

        # Enregistre les informations dans le tableau
        tableau_interactions.append({
            'iteration': iteration + 1,
            'borne_inferieure': borne_inferieure,
            'borne_superieure': borne_superieure,
            'signe_f(borne_inferieure)': "Positif" if (valeur_borne_inferieure > 0) else "Négatif",
            'signe_f(borne_superieure)': "Positif" if (valeur_borne_superieure > 0) else "Négatif",
            'signe_(f(borne_inferieure)*f(borne_superieure))': "Positif" if (valeur_point_milieu > 0) else "Négatif"
        })

        # Vérifie si le point milieu est proche de la racine (tolérance)
        if math.fabs(valeur_point_milieu) <= tolerance or (borne_superieure - borne_inferieure) < tolerance:
            print(f"Solution trouvée : x = {point_milieu} après {iteration + 1} itérations")
            return point_milieu, tableau_interactions

        # Met à jour les bornes en fonction de la position de la racine
        if valeur_point_milieu * valeur_borne_superieure < 0.0:
            borne_inferieure = point_milieu
            valeur_borne_inferieure = valeur_point_milieu
        else:
            borne_superieure = point_milieu
            valeur_borne_superieure = valeur_point_milieu

    # Retourne le milieu final si la solution n'a pas été trouvée dans les itérations
    return (borne_inferieure + borne_superieure) * 0.5, tableau_interactions


# Fonction pour la méthode de la sécante avec amélioration par dichotomie
def methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    tableau_interactions = []

    # Si la racine est bien encadrée, continuer avec la méthode de la sécante
    valeur_borne_inferieure = fonction(borne_inferieure)
    valeur_borne_superieure = fonction(borne_superieure)

    compteur_iterations = 0
    while (math.fabs(borne_superieure - borne_inferieure) > tolerance and compteur_iterations < nombre_max_iterations):
        compteur_iterations += 1
        # Calcul de la nouvelle estimation de la racine
        estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure)
        # Évaluation de la fonction à cette estimation
        valeur_estimation = fonction(estimation)

        # Enregistrement des données dans le tableau des itérations
        tableau_interactions.append({
            'iteration': compteur_iterations,
            'borne_inferieure': borne_inferieure,
            'borne_superieure': borne_superieure,
            'estimation': estimation,
            'f(estimation)': valeur_estimation,
            'différence_bornes': math.fabs(borne_superieure - borne_inferieure),
        })

        # Si l'estimation est proche de la racine, on retourne cette estimation
        if math.fabs(valeur_estimation) <= tolerance:
            print(f"Solution trouvée : x = {estimation} après {compteur_iterations} itérations")
            return estimation, tableau_interactions

        # Mise à jour des bornes en fonction du signe de f(estimation)
        if valeur_estimation * valeur_borne_superieure < 0.0:
            borne_inferieure = estimation
            valeur_borne_inferieure = valeur_estimation
        else:
            borne_superieure = estimation
            valeur_borne_superieure = valeur_estimation

    print(f"Solution approximative trouvée : x = {borne_inferieure} après {compteur_iterations} itérations")
    return borne_inferieure, tableau_interactions

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
        print(f"Convergence atteinte après {compteur_iterations} itérations.")
        return x
    
    
# Générateur sécurisé de fonction phi(x)
def creer_phi(chaine_phi):
    # Vérification de base : la chaîne ne doit pas être vide
    if not chaine_phi.strip():
        raise ValueError("La fonction phi(x) ne peut pas être vide.")

    # Dictionnaire des fonctions autorisées
    fonctions_autorisees = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "log": math.log,
        "exp": math.exp,
        "pi": math.pi,
        "e": math.e,
    }

    # Fonction phi dynamique
    def phi(x):
        try:
            # Évalue la chaîne avec les fonctions autorisées
            return eval(chaine_phi, {"__builtins__": None}, {**fonctions_autorisees, "x": x})
        except NameError as e:
            raise ValueError(f"Nom invalide dans la fonction phi(x) : {e}")
        except SyntaxError as e:
            raise ValueError(f"Syntaxe invalide dans la fonction phi(x) : {e}")
        except Exception as e:
            raise ValueError(f"Erreur inconnue dans la fonction phi(x) : {e}")

    return phi

# Méthode du point fixe avec gestion des erreurs améliorée
def methode_du_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale
    tableau_interactions = []

    # La méthode du point fixe itère jusqu'à ce que la différence entre x et phi(x) soit inférieure à la tolérance
    while True:
        # Calcul de phi(x)
        try:
            phi_x = phi(x)
        except Exception as e:
            print(f"Erreur lors du calcul de phi(x) avec x = {x}: {e}")
            return None, tableau_interactions
        
        # Vérification de la convergence
        difference = math.fabs(phi_x - x)
        tableau_interactions.append({
            'iteration': compteur_iterations + 1,
            'x': x,
            'phi(x)': phi_x,
            'différence': difference
        })

        # Affichage des résultats intermédiaires
        print(f"Iteration {compteur_iterations + 1}: x = {x}, phi(x) = {phi_x}, Différence = {difference}")
        
        # Vérification de la convergence
        if difference <= tolerance:
            print(f"Convergence atteinte après {compteur_iterations + 1} itérations : x = {x}")
            return x, tableau_interactions
        
        # Mise à jour de x avec la nouvelle valeur de phi(x)
        x = phi_x
        compteur_iterations += 1

        # Si le nombre d'itérations atteint le maximum sans convergence, on arrête
        if compteur_iterations >= nombre_max_iterations:
            print("Pas de convergence avec la méthode du point fixe.")
            return None, tableau_interactions

def methode_de_balayage(fonction, borne_inferieure, borne_superieure, pas, tolerance):
    # Initialisation du tableau pour stocker les intervalles
    tableau_intervals = []
    variable_x = borne_inferieure

    print("Début du balayage :")

    # Parcours de l'intervalle
    while variable_x <= borne_superieure:
        # Calcul des bornes
        borne_inf = variable_x
        borne_sup = variable_x + pas
        f_borne_inf = fonction(borne_inf)
        f_borne_sup = fonction(borne_sup)

        # Vérifie si la fonction change de signe entre les deux bornes
        changement_signe = f_borne_inf * f_borne_sup < 0

        # Affiche l'intervalle en cours et la détection du changement de signe
        print(f"Intervalle [{borne_inf}, {borne_sup}] : f(borne_inferieure) = {round(f_borne_inf, 6)}, f(borne_superieure) = {round(f_borne_sup, 6)}")
        print(f"Changement de signe : {'Oui' if changement_signe else 'Non'}")

        # Enregistre les informations dans le tableau
        tableau_intervals.append({
            'intervalle': f"[{borne_inf}, {borne_sup}]",
            'borne_inferieure': borne_inf,
            'borne_superieure': borne_sup,
            'f(borne_inferieure)': round(f_borne_inf, 6),
            'f(borne_superieure)': round(f_borne_sup, 6),
            'changement_de_signe': "Oui" if changement_signe else "Non"
        })

        # Si un changement de signe est détecté, applique la méthode de dichotomie pour trouver la racine
        if changement_signe:
            print(f"Changement de signe détecté dans l'intervalle [{borne_inf}, {borne_sup}]")
            racine, _ = methode_de_dichotomie(fonction, borne_inf, borne_sup, tolerance, 100)
            print(f"Racine trouvée : {racine}")
            return racine, tableau_intervals
        
        # Passe à l'intervalle suivant
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
        x_initiale += pas_de_balayage

    print("Aucune solution trouvée pour Newton-Raphson avec le balayage.")
    return None

# Fonction pour calculer l'ensemble de définition d'une fonction
def ensemble_de_definition(fonction_str):
    # Définir le symbole utilisé dans la fonction
    x = symbols('x')
    
    try:
        # Convertir la chaîne de caractères en une expression sympy
        fonction_expr = sympify(fonction_str)
        
        # Calculer l'ensemble de définition en utilisant continuous_domain de sympy
        domaine = continuous_domain(fonction_expr, x, S.Reals)
        
        # Remplacer les bornes infinies et ajuster le format
        if isinstance(domaine, Interval):
            # Pour les intervalles, on peut formater de manière plus mathématique
            if domaine.start == -S.Infinity:
                start_str = "-∞"
            else:
                start_str = str(domaine.start)
            
            if domaine.end == S.Infinity:
                end_str = "+∞"
            else:
                end_str = str(domaine.end)

            # Formatage de l'intervalle : [start, end] ou (start, end)
            if domaine.left_open:
                start_str = f"({start_str}"
            else:
                start_str = f"[{start_str}"
            
            if domaine.right_open:
                end_str = f"{end_str})"
            else:
                end_str = f"{end_str}]"
            
            domaine_str = f"{start_str}, {end_str}"
        else:
            # Pour les unions d'intervalles, on affiche la notation standard
            domaine_str = str(domaine).replace('Union', '∪').replace('Interval', '[]')
        
        # Afficher l'ensemble de définition sous forme d'intervalle
        print(f"Ensemble de définition de la fonction : {domaine_str}")
        return domaine_str
    except Exception as e:
        print(f"Erreur lors du calcul de l'ensemble de définition : {e}")
        return None
