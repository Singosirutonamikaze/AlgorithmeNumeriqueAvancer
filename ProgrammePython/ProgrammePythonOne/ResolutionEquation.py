from fonctionsDuMain import choisir_methode,saisir_tolerance_et_iterations_de_resolution  # Importation des fonctions principales du programme, comme choisir_methode, saisir_fonction, appliquer_methode, etc.
from AccueilEtMenus import  rectangle_bienvenue_complexe, choisir_methode, print_method_name, saisir_fonction_et_ensemble_definition, saisir_bornes_si_necessaire, appliquer_methode, afficher_racine, demander_recommencer # Importation de la fonction pour afficher l'écran de bienvenue

def main():
    # Fonction principale qui gère le programme.
    action = True  # Initialisation de la variable pour contrôler si l'utilisateur souhaite recommencer ou quitter.
    # Affichage de l'écran de bienvenue en utilisant la fonction rectangle_bienvenue_complexe.
    rectangle_bienvenue_complexe()
    # Boucle principale qui permet à l'utilisateur de choisir une méthode et d'exécuter le programme.
    while action:
        choix = choisir_methode()  # Affiche le menu et demande à l'utilisateur de choisir une méthode de résolution.
        print_method_name(choix)  # Affiche le nom de la méthode choisie.
        fonction, fonction_expr = saisir_fonction_et_ensemble_definition()  # Demande à l'utilisateur de saisir une fonction et son ensemble de définition.
        if fonction is None:  # Si la fonction est invalide, on redemande la saisie.
            continue
        borne_inferieure, borne_superieure = saisir_bornes_si_necessaire(choix, fonction_expr)  # Demande les bornes si nécessaire.
        print(f"Votre intervalle est : [{borne_inferieure}, {borne_superieure}]")
        tolerance, nombre_max_iterations = saisir_tolerance_et_iterations_de_resolution()  # Demande la tolérance et le nombre d'itérations.
        racine = appliquer_methode(choix, fonction, fonction_expr, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)  # Applique la méthode choisie.
        afficher_racine(racine)  # Affiche la racine trouvée.
    action = demander_recommencer()  # Demande à l'utilisateur s'il souhaite recommencer ou quitter.

# Condition pour exécuter la fonction main seulement si le fichier est exécuté directement (pas importé comme module).
if __name__ == "__main__":
    main()  # Appel de la fonction principale pour démarrer le programme
