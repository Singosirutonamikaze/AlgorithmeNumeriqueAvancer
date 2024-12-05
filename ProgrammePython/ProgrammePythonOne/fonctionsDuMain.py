# Importation des modules nécessaires
from sympy import lambdify, sympify, symbols  # Importation de sympy pour manipuler des expressions mathématiques symboliques
from MethodeDeResolution import methode_de_balayage, methode_de_la_secante, methode_de_dichotomie, methode_de_newton_raphson, methode_du_point_fixe, ensemble_de_definition, creer_phi  # Importation des différentes méthodes de résolution
from AccueilEtMenus import   methode_resolution, saisir_fonction, saisir_tolerance_et_iterations, demander_bornes # Importation des fonctions liées aux menus et saisies
from fonctionsTableaux import afficher_tableau_balayage, afficher_tableau_secante, afficher_tableau_dichotomie, afficher_tableau_point_fixe
import pickle
import os

# Fonction pour choisir la méthode de résolution
def choisir_methode():
    """
    Affiche le menu pour choisir la méthode de résolution et gère la saisie de l'utilisateur.
    """
    methode_resolution()  # Afficher le menu des méthodes

    # Boucle pour s'assurer que l'utilisateur saisit un choix valide entre 1 et 5
    while True:
        try:
            choix = int(input("Entrez le numéro de la méthode (1-5) : "))
            if 1 <= choix <= 5:
                return choix  # Retourner le choix de l'utilisateur si valide
            else:
                print("Erreur : le numéro doit être un entier compris entre 1 et 5.\n")
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.\n")

x = symbols('x')
# Fonction pour saisir la fonction et afficher son ensemble de définition
def saisir_fonction_et_ensemble_definition():
    """
    Demande à l'utilisateur de saisir la fonction et affiche l'ensemble de définition.
    """
    fonction_str = saisir_fonction()  # Demander à l'utilisateur de saisir une fonction sous forme de chaîne de caractères
    try:
        # Convertir la chaîne de caractères en une expression mathématique que sympy peut traiter
        fonction_expr = sympify(fonction_str)
        # Convertir l'expression sympy en une fonction lambda utilisable par Python
        fonction = lambdify(x, fonction_expr, 'math')
        print(f"Fonction interprétée : f(x) = {fonction_expr}")
        ensemble_de_definition(fonction_str)  # Afficher l'ensemble de définition de la fonction
        return fonction, fonction_expr
    except Exception as e:
        print(f"Erreur lors de l'interprétation de la fonction : {e}")
        return None, None  # Retourner None si une erreur se produit


# Fonction pour saisir les bornes nécessaires selon la méthode choisie
def saisir_bornes_si_necessaire(choix, fonction_str):
    """
    Demande les bornes nécessaires en fonction de la méthode choisie.
    """
    # Si la méthode nécessite des bornes (Dichotomie, Sécante ou Balayage), on les demande
    if choix in [1, 2, 5]:
        return demander_bornes(fonction_str)  # Appel à la fonction demander_bornes pour obtenir les bornes
    return None, None  # Retourner None si les bornes ne sont pas nécessaires pour cette méthode



# Fonction pour saisir la tolérance et le nombre d'itérations
def saisir_tolerance_et_iterations_de_resolution():
    """
    Demande à l'utilisateur la tolérance et le nombre d'itérations.
    """
    return saisir_tolerance_et_iterations()  # Appel à la fonction saisir_tolerance_et_iterations pour obtenir ces informations

# Fonction pour appliquer la méthode choisie pour résoudre l'équation
def appliquer_methode(choix, fonction, fonction_expr, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    """
    Applique la méthode choisie pour résoudre l'équation.
    """
    racine = None  # Initialiser la variable racine
    tableau = None  # Initialiser la variable tableau

    # Appliquer la méthode choisie selon le numéro de méthode (choix)
    try:
        if choix == 1:
            racine, tableau = methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif choix == 2:
            racine, tableau = methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif choix == 3:
            derivee_fonction = lambdify(x, fonction_expr.diff(x), 'math')
            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "))
            racine = methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations)
        elif choix == 4:
            phi_str = input("Entrez l'expression de phi(x) (exemple : sqrt(2*x - 1)) : ")
            phi = creer_phi(phi_str)
            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "))
            racine, tableau = methode_du_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations)
        elif choix == 5:
            pas = float(input("Entrez le pas pour le balayage (exemple: 0.1) : "))
            racine, tableau = methode_de_balayage(fonction, borne_inferieure, borne_superieure, pas, tolerance)

        if tableau is not None:
            afficher_tableau(choix, tableau)
            enregistrer_tableau(choix, tableau)
    except ValueError as e:
        print(f"Erreur : {e}. Veuillez réessayer.")  # Gestion d'erreur si la saisie est incorrecte

    return racine  # Retourner la racine trouvée par la méthode

def afficher_tableau(choix, tableau):
    """
    Affiche le tableau des itérations en fonction de la méthode choisie.
    """
    if choix == 1:
        afficher_tableau_dichotomie(tableau)
    elif choix == 2:
        afficher_tableau_secante(tableau)
    elif choix == 4:
        afficher_tableau_point_fixe(tableau)
    elif choix == 5:
        afficher_tableau_balayage(tableau)

def enregistrer_tableau(methode_choisie, tableau):
    """
    Enregistre le tableau des itérations dans un fichier.
    """
    nom_fichier = f"{methode_choisie}_tableau.txt"
    try:
        with open(nom_fichier, 'wb') as f:
            pickle.dump(tableau, f)
        print(f"Le tableau des itérations a été enregistré dans le fichier {nom_fichier}.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Erreur lors de l'enregistrement du tableau : {e}")
    except pickle.PickleError as e:
        print(f"Erreur de sérialisation du tableau : {e}")

def afficher_tableau_enregistre(nom_fichier):
    """
    Affiche le tableau des itérations à partir d'un fichier.
    """
    if os.path.exists(nom_fichier):
        try:
            with open(nom_fichier, 'rb') as f:
                tableau_enregistre = pickle.load(f)
            print(f"Tableau des itérations :")
            for it in tableau_enregistre:
                print(it)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Erreur lors de la lecture du fichier : {e}")
        except pickle.PickleError as e:
            print(f"Erreur de désérialisation du tableau : {e}")
    else:
        print(f"Le fichier {nom_fichier} n'existe pas.")


# Fonction pour afficher la racine trouvée
def afficher_racine(racine):
    """
    Affiche la racine trouvée.
    """
    if racine is not None:
        print(f"La racine trouvée est : {racine}")  # Affichage si une racine a été trouvée
    else:
        print("Aucune racine n'a été trouvée.")  # Message d'erreur si aucune racine n'est trouvée

# Fonction pour demander à l'utilisateur s'il souhaite recommencer
def demander_recommencer():
    """
    Demande à l'utilisateur s'il souhaite recommencer ou quitter.
    """
    return input("Souhaitez-vous recommencer ? (oui/non) : ").lower() == "oui"  # Vérifier la réponse de l'utilisateur

# Fonction pour afficher le nom de la méthode choisie
def print_method_name(choix):
    """
    Affiche le nom de la méthode choisie.
    """
    # Dictionnaire associant chaque méthode à son nom
    methods = {
        1: "METHODE DE DICHOTOMIE",
        2: "METHODE DE LA SECANTE",
        3: "METHODE DE NEWTON-RAPHSON",
        4: "METHODE DU POINT FIXE",
        5: "METHODE DE BALAYAGE"
    }
    # Affichage du nom de la méthode choisie
    print(f"***************{methods[choix]}***************\n")
