#Importation des modules necessaires
from sympy import symbols, sympify, sin, cos, tan, log, sqrt
import re
import math

# Fonction pour afficher un message de bienvenue avec un cadre de texte
def rectangle_bienvenue_complexe():
    # Définir la phrase à afficher et calculer la largeur du rectangle
    phrase = "      BIENVENUE DANS LA RESOLUTION D'EQUATION F(x) = 0     "  # Texte à afficher
    largeur = len(phrase) + 6  # Largeur du rectangle (avec une marge de 3 caractères de chaque côté)
    hauteur = 5  # Hauteur du rectangle (fixée à 5 lignes)

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
    print("*******************Choisissez la méthode de résolution *******************\n")
    print("                     1. La méthode de Dichotomie")
    print("                     2. La méthode de la Sécante")  
    print("                     3. La méthode de Newton-raphson")
    print("                     4. La méthode du Point Fixe")
    print("                     5. La méthode de Balayage\n")

# Initialisation de 'x' pour pouvoir l'utiliser comme symbole dans les expressions mathématiques
x = symbols('x')

def saisir_fonction():
    # Affichage du menu pour choisir le type de fonction
    print("\n******************* Menu de choix de fonction *******************\n")
    print("Choisissez le type de fonction que vous souhaitez entrer :\n")
    print("     1. Polynôme (ex: x**2 + 3*x - 8)")
    print("     2. Trigonométrique (ex:  cos(x) + x)")
    print("     3. Logarithmique (ex:  log(x) + x**2)")
    print("     4. Racine carrée (ex: sqrt(x) + x/2)")
    print("     5. Rationnelle (ex: (x + 1) / (x - 2))")
    print("     6. Fonction générale (ex: (x**3 - sin(x) + log(x))/(x**2 + 1))\n")

    # Dictionnaire contenant les types de fonction disponibles avec des exemples
    types_fonction = {
        "1": "Polynôme",
        "2": "Trigonométrique",
        "3": "Logarithmique",
        "4": "Racine carrée",
        "5": "Rationnelle",
        "6": "Fonction générale"
    }
    
  

   # Dictionnaire des expressions régulières pour chaque type de fonction
    regex_patterns = { 
        "1": r"^(x|sin|cos|tan|sec|csc|cot|-exp|log|ln|sqrt|abs)?\(?[0-9xX\+\-\*/\^\(\)\s]+(\*\*[0-9xXexp(1/x)\+\-\*/\^\(\)\s]*)?\)?$", # Polynôme
        "2": r"^(sin|cos|tan|sec|csc|cot|exp|log|ln|sqrt|abs)?\([xX0-9\+\-\*/\s]+\)[\+\-\*/xX0-9\(\)\s]*$",# Trigonométrique 
        "3": r"^(sin|cos|tan|exp|ln|sqrt|abs|log|)?\([xX0-9\+\-\*/\s\^\.\,\(]+\)([\+\-\*/\^xX0-9\(\)\s]*(sin|cos|tan|exp|ln|sqrt|abs|log)?\([xX0-9\+\-\*/\s\^\.\,\(]+\))*$", # Logarithmique
        "4": r"^(sqrt|cbrt|root\d*|sin|cos|tan|sec|csc|cot|exp|ln|log)?\([xX0-9\+\-\*/\s]+\)|e\*\*[xX0-9\+\-\*/\s]+[\+\-\*/xX0-9\(\)\s]*$", # Racine carrée
        "5": r"^(\(.*[a-zA-Z0-9\+\-\*/\(\)\s]+\))?(\(sin|cos|tan|sec|csc|cot|exp|ln|log|e\*\*[xX0-9\+\-\*/\(\)\s]+\))?/\(.*[a-zA-Z0-9\+\-\*/\(\)\s]+\)$", # Rationnelle 
        "6": r"^(sin|cos|tan|sec|csc|cot|exp|ln|log|sqrt|cbrt|root\d*|e\*\*)?\([xX0-9\+\-\*/\(\)\s]+\)([\+\-\*/](sin|cos|tan|sec|csc|cot|exp|ln|log|sqrt|cbrt|root\d*|e\*\*)?\([xX0-9\+\-\*/\(\)\s]+\))*$" # Fonction générale 
    }

    # Boucle principale pour permettre à l'utilisateur de choisir un type de fonction
    while True:
        # Demander à l'utilisateur de choisir un type de fonction
        type_fonction = input("Entrez le numéro du type de fonction : ").strip()

        # Vérifier si le choix est valide
        if type_fonction not in types_fonction:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.\n")
            continue

        # Demander à l'utilisateur de saisir la fonction mathématique
        while True:
            # Supprimer les espaces inutiles et mettre tout en minuscules pour faciliter l'analyse
            fonction = input(f"Entrez votre fonction mathématique ({types_fonction[type_fonction]}) : ").replace(" ", "").lower()

            # Récupérer l'expression régulière correspondant au type de fonction choisi
            pattern = regex_patterns[type_fonction]

            # Vérification si la fonction correspond au modèle
            if re.fullmatch(pattern, fonction):
                try:
                    # Essayer de convertir la fonction en une expression sympy
                    fonction_sympy = sympify(fonction)
                    # Afficher un message de confirmation si la fonction est valide
                    print(f"Votre fonction saisie '{fonction}' est correcte.\n")
                    return fonction_sympy
                except Exception as e:
                    # En cas d'erreur de parsing, afficher un message d'erreur
                    print(f"Erreur : Impossible de parser la fonction. Veuillez vérifier votre saisie. ({e})\n")
            else:
                # Si la fonction ne correspond pas au modèle, afficher un message d'erreur
                print("Erreur : La fonction saisie n'est pas valide. Essayez à nouveau.\n")

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

def verifier_ensemble_de_definition(fonction, borne):
    """Vérifie si la borne est dans l'ensemble de définition de la fonction."""
    try:
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
                print(f"Erreur : Division par zéro pour x = {borne}.")
                return False

        return True  # La borne est valide dans l'ensemble de définition
    except Exception as e:
        print(f"Erreur lors de la vérification du domaine : {e}")
        return False

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
                print(f"Erreur : La valeur {borne} n'est pas dans l'ensemble de définition de la fonction.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
