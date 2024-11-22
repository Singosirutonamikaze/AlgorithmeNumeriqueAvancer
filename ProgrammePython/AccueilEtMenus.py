#Importation des modules necessaires
from sympy import symbols, sympify, SympifyError

# Fonction pour afficher un message de bienvenue avec un cadre de texte
def rectangle_bienvenue_complexe():
    # Définir la phrase à afficher et calculer la largeur du rectangle
    phrase = "      BIENVENUE DANS LA RESOLUTION D'EQUATION F(x) = 0     "  # Texte à afficher
    largeur = len(phrase) + 6  # Largeur du rectangle (avec une marge de 3 caractères de chaque côté)
    # Dessiner la première ligne du rectangle (bordure supérieure avec des étoiles)
    print('*' * largeur)
    # Ligne avec une bordure interne et des espaces à l'intérieur
    print('*' + ' ' * (largeur - 2) + '*')
    # Ligne du milieu avec le texte "BIENVENUE" centré
    print('* *' + phrase.center(largeur - 6) + '* *')
    # Ligne avec une bordure interne et des espaces à l'intérieur
    print('*' + ' ' * (largeur - 2) + '*')
    # Dernière ligne (bordure inférieure avec des étoiles)
    print('*' * largeur)


# Fonction permettant de choisir la méthode de résolution parmi plusieurs options
def methode_resolution():
    # Affiche le menu pour choisir la méthode de résolution.
    print("*******************Choisissez la méthode de résolution *******************\n")
    print("                     1. La méthode de Dichotomie")
    print("                     2. La méthode de la Sécante")  
    print("                     3. La méthode de Newton-raphson")
    print("                     4. La méthode du Point Fixe")
    print("                     5. La méthode de Balayage\n")

# Initialisation de 'x' pour pouvoir l'utiliser comme symbole dans les expressions mathématiques
x = symbols('x')

def afficher_menu():
    # Affiche le menu pour choisir le type de fonction.
    
    print("\n******************* Menu de choix de fonction *******************\n")
    print("Choisissez le type de fonction que vous souhaitez entrer :\n")
    print("     1. Polynôme (ex: x**2 + 3*x - 8)")
    print("     2. Trigonométrique (ex: cos(x) + x)")
    print("     3. Logarithmique (ex: log(x) + x**2)")
    print("     4. Racine carrée (ex: sqrt(x) + x/2)")
    print("     5. Rationnelle (ex: (x + 1) / (x - 2))")
    print("     6. Fonction générale (ex: (x**3 - sin(x) + log(x))/(x**2 + 1))\n")

def saisir_fonction():
    # Permet à l'utilisateur de choisir un type de fonction et de saisir une fonction mathématique.
    # Valide la saisie en la convertissant en une expression `sympy`.
    # Retourne l'expression sympy si elle est correcte.
    
    afficher_menu()

    # Dictionnaire contenant les types de fonction disponibles avec des descriptions
    types_fonction = {
        "1": "Polynôme",
        "2": "Trigonométrique",
        "3": "Logarithmique",
        "4": "Racine carrée",
        "5": "Rationnelle",
        "6": "Fonction générale"
    }

    while True:
        # Demander à l'utilisateur de choisir un type de fonction
        type_fonction = input("Entrez le numéro du type de fonction : ").strip()

        # Vérifier que le choix est valide
        if type_fonction not in types_fonction:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.\n")
            continue

        # Afficher un message pour guider l'utilisateur dans la saisie de sa fonction
        print(f"\nVous avez choisi : {types_fonction[type_fonction]}\n")
        print(f"Veuillez entrer votre fonction en respectant la syntaxe d'une fonction mathématique de type  {types_fonction[type_fonction]}.\n")

        while True:
            # Demander à l'utilisateur de saisir sa fonction mathématique
            fonction = input(f"Entrez votre fonction mathématique ({types_fonction[type_fonction]}): ").strip()

            try:
                # Tenter de convertir la fonction en une expression sympy
                fonction_sympy = sympify(fonction)

                # Si la conversion réussit, afficher un message de confirmation
                print(f"\nVotre fonction saisie '{fonction}' a été validée avec succès.\n")
                return fonction_sympy
            except SympifyError:
                # Si une erreur survient, demander à l'utilisateur de réessayer
                print("\nErreur : La fonction saisie est invalide ou contient une erreur de syntaxe.\n")
                print("Vérifiez votre saisie et essayez à nouveau.\n")


# Fonction pour demander la tolérance et le nombre d'itérations
def saisir_tolerance_et_iterations():
    while True:
        try:
            # Demander la tolérance avec prise en charge des notations scientifiques
            tolerance_input = input("Entrez la tolérance souhaitée (ex: 0.0001, 1.0e-5, 1e-6) : \n")
            # Convertir l'entrée en nombre flottant
            tolerance = float(tolerance_input)

            # Demander le nombre maximal d'itérations
            nombre_max_iterations = int(input("Entrez le nombre maximal d'itérations (ex: 100) : \n"))
            
            # Vérifier que la tolérance et le nombre d'itérations sont valides (supérieurs à zéro)
            if tolerance > 0 and nombre_max_iterations > 0:
                print(f"Votre tolérance est : {tolerance}")
                print(f"Votre nombre maximal d'itérations est : {nombre_max_iterations}\n")
                return tolerance, nombre_max_iterations
            else:
                print("Erreur : la tolérance et le nombre d'itérations doivent être supérieurs à zéro.")
        
        except ValueError:
            print("Erreur : veuillez entrer des valeurs numériques valides pour la tolérance (flottant) et un entier pour le nombre d'itérations.")

# Fonction pour vérifier si la borne est dans l'ensemble de définition de la fonction
def verifier_ensemble_de_definition(fonction, borne):
    #Vérifie si la borne est dans l'ensemble de définition de la fonction.
    try:
        # Vérification des logarithmes (log(x)) : log(x) est défini uniquement pour x > 0
        if 'log' in str(fonction) and borne <= 0:
            print(f"Erreur : Logarithme non défini pour x = {borne}. La borne doit être strictement positive (NB: la fonction log(x) est définie pour x > 0 et x != 0).\n ")
            return False

        # Vérification des racines carrées (si la fonction en contient)
        if 'sqrt' in str(fonction):
            expr_sqrt = fonction.subs(x, borne)
            if expr_sqrt < 0:
                print(f"Erreur : L'expression sous la racine carrée est négative pour x = {borne}.")
                return False

        # Vérification des dénominateurs pour les fonctions rationnelles
        if '/' in str(fonction):
            expr_denominateur = fonction.as_numer_denom()[1].subs(x, borne)
            if expr_denominateur == 0:
                print(f"Erreur : Division par zéro pour x = {borne}.\n")
                return False

        return True  # La borne est valide dans l'ensemble de définition
    except Exception as e:
        print(f"Erreur lors de la vérification du domaine : {e}")
        return False

# Fonction pour demander des bornes inférieure et supérieure
def demander_bornes(fonction_str):
    """Demande à l'utilisateur de saisir les bornes inférieure et supérieure de l'intervalle."""
    while True:
        try:
            # Demander la saisie de la borne inférieure
            borne_inferieure = demander_borne(fonction_str, "Entrez la borne inférieure de l'intervalle : ")
            
            # Demander la saisie de la borne supérieure
            borne_superieure = demander_borne(fonction_str, "Entrez la borne supérieure de l'intervalle : ")

            # Vérifier que la borne inférieure est bien inférieure à la borne supérieure
            if borne_inferieure < borne_superieure:
                return borne_inferieure, borne_superieure
            else:
                print("Erreur : la borne inférieure doit être inférieure à la borne supérieure.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre réel valide pour chaque borne.")

# Fonction pour demander une borne
def demander_borne(fonction_str, message):
    """Demande à l'utilisateur de saisir une borne et vérifie si elle est dans l'ensemble de définition de la fonction."""
    while True:
        try:
            # Demande à l'utilisateur de saisir une valeur
            borne = float(input(message))
            
            # Vérifie si la borne est dans l'ensemble de définition
            if verifier_ensemble_de_definition(fonction_str, borne):
                return borne
            else:
                print(f"Erreur : La valeur {borne} n'est pas dans l'ensemble de définition de la fonction.\n")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
