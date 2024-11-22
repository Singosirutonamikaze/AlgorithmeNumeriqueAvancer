from fonctionsDuMain import *  # Importation des fonctions principales du programme, comme choisir_methode, saisir_fonction, appliquer_methode, etc.
from AccueilEtMenus import rectangle_bienvenue_complexe  # Importation de la fonction pour afficher l'écran de bienvenue

def main():
    # Fonction principale qui gère le programme.
    # Cette fonction orchestre l'exécution du programme en appelant les différentes étapes : 
    # affichage du menu, saisie de la fonction, choix de la méthode, résolution et affichage du résultat.
    
    action = True  # Initialisation de la variable pour contrôler si l'utilisateur souhaite recommencer ou quitter.
    
    # Affichage de l'écran de bienvenue en utilisant la fonction rectangle_bienvenue_complexe.
    rectangle_bienvenue_complexe()

    # Boucle principale qui permet à l'utilisateur de choisir une méthode et d'exécuter le programme.
    while action:
        # Appel de la fonction choisir_methode pour afficher le menu et demander à l'utilisateur de choisir une méthode de résolution.
        choix = choisir_methode()

        # Appel de la fonction print_method_name pour afficher le nom de la méthode choisie (par exemple, Méthode de Dichotomie).
        print_method_name(choix)

        # Appel de la fonction saisir_fonction_et_ensemble_definition pour demander à l'utilisateur de saisir une fonction et afficher son ensemble de définition.
        fonction, fonction_expr = saisir_fonction_et_ensemble_definition()
        
        # Si la fonction n'est pas valide (fonction == None), la boucle continue et redemande la saisie de la fonction.
        if fonction is None:
            continue

        # Appel de la fonction saisir_bornes_si_necessaire pour demander les bornes si la méthode choisie en nécessite (comme la méthode de Dichotomie, Sécante, ou Balayage).
        borne_inferieure, borne_superieure = saisir_bornes_si_necessaire(choix, fonction_expr)
        
        # Affichage des bornes choisies par l'utilisateur.
        print(f"Votre intervalle est : [{borne_inferieure}, {borne_superieure}]")

        # Appel de la fonction saisir_tolerance_et_iterations_de_resolution pour demander à l'utilisateur la tolérance et le nombre maximal d'itérations.
        tolerance, nombre_max_iterations = saisir_tolerance_et_iterations_de_resolution()

        # Appel de la fonction appliquer_methode pour exécuter la méthode choisie (comme la méthode de Dichotomie, Sécante, etc.) avec les paramètres nécessaires.
        racine = appliquer_methode(choix, fonction, fonction_expr, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        
        # Appel de la fonction afficher_racine pour afficher la racine trouvée (ou un message si aucune racine n'a été trouvée).
        afficher_racine(racine)

        # Demander à l'utilisateur s'il souhaite recommencer ou quitter en appelant la fonction demander_recommencer.
        action = demander_recommencer()

# Condition pour exécuter la fonction main seulement si le fichier est exécuté directement (pas importé comme module).
if __name__ == "__main__":
    main()  # Appel de la fonction principale pour démarrer le programme
