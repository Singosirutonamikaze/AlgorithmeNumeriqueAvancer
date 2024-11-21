from sympy import symbols, sympify, lambdify

# Importation des méthodes de résolution
from MethodeDeResolution import methode_de_dichotomie, methode_de_la_secante, methode_de_newton_raphson, ensemble_de_definition
from MethodeDeResolution import methode_du_point_fixe, methode_de_balayage, creer_phi, afficher_tableau_dichotomie
# Importation des menus d'accueil et des fonctions auxiliaires
from AccueilEtMenus import rectangle_bienvenue_complexe, methode_resolution, saisir_fonction, saisir_tolerance_et_iterations, demander_bornes


# Définition du symbole 'x' qui sera utilisé dans les fonctions mathématiques
x = symbols('x')
def main():
    action = True  # Variable pour contrôler si l'utilisateur souhaite recommencer ou quitter

    # Présentation du programme
    rectangle_bienvenue_complexe()

    # Boucle principale pour recommencer ou terminer
    while action:
        # Affichage du menu principal pour choisir la méthode de résolution
        methode_resolution()

        # Boucle pour s'assurer que l'utilisateur saisit un entier valide entre 1 et 5 pour choisir la méthode
        while True:
            try:
                choix = int(input("Entrez le numéro de la méthode (1-5) : "))  # Demander à l'utilisateur de choisir une méthode
                if 1 <= choix <= 5:  # Vérifier que le choix est entre 1 et 5
                    break  # Sortir de la boucle si le choix est valide
                else:
                    print("Erreur : le numéro doit être un entier compris entre 1 et 5.\n")  # Si le choix n'est pas valide
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier.\n")  # Si l'entrée n'est pas un entier

        # Affichage de la méthode choisie
        if choix == 1:
            print("***************METHODE DE DICHOTOMIE***************\n")
        elif choix == 2:
            print("***************METHODE DE LA SECANTE***************\n")
        elif choix == 3:
            print("***************METHODE DE NEWTON-RAPHSON***************\n")
        elif choix == 4:
            print("***************METHODE DU POINT FIXE***************\n")
        elif choix == 5:
            print("***************METHODE DE BALAYAGE***************\n")

        # Demander à l'utilisateur de saisir la fonction à résoudre
        fonction_str = saisir_fonction()

        try:
            # Convertir la fonction sous forme de chaîne en une expression sympy
            fonction_expr = sympify(fonction_str)
            fonction = lambdify(x, fonction_expr, 'math')  # Transformer la fonction sympy en fonction mathématique Python
            print("Fonction interprétée : f(x) =", fonction_expr)  # Afficher la fonction interprétée
            ensemble_de_definition(fonction_str)#Afficher l'ensemble de definition
        except Exception as e:
            print(f"Erreur lors de l'interprétation de la fonction : {e}")  # Si la fonction est invalide, afficher l'erreur
            continue  # Demander à nouveau la fonction si une erreur survient

        # Si la méthode choisie nécessite des bornes (Méthode de Dichotomie, Sécante ou Balayage)
        if choix in [1, 2, 5]:  # Vérifier si le choix est 1, 2 ou 5
            borne_inferieure, borne_superieure = demander_bornes(fonction_str)  # Demander les bornes
            print(f"Votre intervalle est : [{borne_inferieure}, {borne_superieure}]")  # Afficher l'intervalle choisi

        # Définir la tolérance et le nombre maximal d'itérations
        tolerance, nombre_max_iterations = saisir_tolerance_et_iterations()  # Saisie de la tolérance et des itérations

        # Exécution de la méthode choisie par l'utilisateur
        racine = None  # Initialisation de la variable racine

        if choix == 1:
            # Résolution avec la méthode de dichotomie
                racine, tableau = methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)

                # Affichage du tableau stylisé
                afficher_tableau_dichotomie(tableau)

        elif choix == 2:
            # Résolution avec  la méthode de la sécante
            racine = methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)

        elif choix == 3:
            # Résolution avec  la méthode de Newton-Raphson
            derivee_fonction = lambdify(x, fonction_expr.diff(x), 'math')  # Calcul de la dérivée de la fonction
            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "))
            racine = methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations)

        elif choix == 4:
            # Résolution avec  la méthode du point fixe avec validation des entrées
            while True:
                try:
                    # Boucle pour demander une fonction phi(x) correcte
                    while True:
                        try:
                            chaine_phi = input("Entrez la fonction phi(x) (exemple : sqrt(2*x - 1)) : ")
                            phi = creer_phi(chaine_phi)  # Crée la fonction phi(x)
                            break  # Sortir si la fonction est correcte
                        except ValueError as e:
                            print(f"Erreur : {e}. Veuillez réessayer.")

                    # Boucle pour demander un Xo valide
                    while True:
                        try:
                            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "))
                            break  # Si la saisie est correcte, sortir de la boucle
                        except ValueError:
                            print("Veuillez entrer une valeur numérique valide pour Xo.")
                    
                    # Appel de la méthode du point fixe
                    racine = methode_du_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations)
                    if racine is not None:
                        print(f"La racine approximative trouvée est : {racine}")
                    else:
                        print("Aucune racine n'a été trouvée.")
                    break  # Terminer après l'exécution réussie

                except Exception as e:
                    print(f"Une erreur inattendue s'est produite : {e}")


        elif choix == 5:
            # Résolution avec la méthode de balayage
            pas = float(input("Entrez le pas pour le balayage (exemple: 0.1) : "))
            racine = methode_de_balayage(fonction, borne_inferieure, borne_superieure, pas, tolerance)


        # Affichage de la racine trouvée
        if racine is not None:
            print(f"La racine trouvée est : {racine}")  # Afficher la racine si elle a été trouvée
        else:
            print("Aucune racine n'a été trouvée.")  # Si aucune racine n'a été trouvée

        # Demander à l'utilisateur s'il veut recommencer ou quitter
        choix_recommencer_Terminer = input("Souhaitez-vous recommencer ? (oui/non) : ").lower()
        
        if choix_recommencer_Terminer == "oui":
            action = True  # Continuer si l'utilisateur veut recommencer
        else:
            action = False  # Quitter si l'utilisateur ne veut pas recommencer



# Appel de la fonction principale pour démarrer le programme
if __name__ == "__main__":
    main()  # Lancer le programme
