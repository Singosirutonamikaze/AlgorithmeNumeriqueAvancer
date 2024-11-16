<?php
// Importation des fichiers nécessaires pour les méthodes de résolution et les fonctions d'accueil/menus.
include '/../includes/MethodeDeResolution.php';
include '/../includes/AccueilEtMenus.php'; // correction du nom du fichier

// Fonction principale pour gérer le menu et les choix de l'utilisateur
function main() {
    // Initialisation de la variable pour contrôler si l'utilisateur veut continuer ou non.
    $choix_recommencer_Terminer = "";
    $action = true;

    // Appel de la fonction pour afficher un message de bienvenue complexe avec une bordure.
    rectangle_bienvenue_complexe();

    // Boucle principale permettant à l'utilisateur de recommencer l'opération ou de quitter.
    while ($action) {
        // Affichage du menu principal contenant les différentes méthodes de résolution.
        methode_resolution();

        // Boucle pour garantir que l'utilisateur entre un choix valide (1 à 4).
        while (true) {
            $choix = readline("Entrez le numéro de la méthode (1-4) : ");
            $choix = intval($choix); // Conversion en entier pour s'assurer que l'entrée est un nombre

            // Vérification de la validité du choix
            if ($choix < 1 || $choix > 4) {
                echo "Erreur : le numéro doit être un entier compris entre 1 et 4.\n";
            } else {
                break; // Sortie de la boucle si le choix est valide
            }
        }

        // Affichage de la méthode choisie par l'utilisateur
        echo "Vous avez choisi la méthode numéro $choix.\n";
        switch ($choix) {
            case 1:
                echo "***************MÉTHODE DE DICHOTOMIE***************\n";
                break;
            case 2:
                echo "***************MÉTHODE DE LA SECANTE***************\n";
                break;
            case 3:
                echo "***************MÉTHODE DE NEWTON-RAPHSON***************\n";
                break;
            case 4:
                echo "***************MÉTHODE DU POINT FIXE***************\n";
                break;
        }

        // Saisie de la fonction mathématique par l'utilisateur sous forme de chaîne de caractères
        $fonction_str = saisir_fonction();
        $fonction = create_function_from_string($fonction_str); // Conversion en fonction exécutable

        // Vérification si la méthode choisie nécessite des bornes d'intervalle
        if (in_array($choix, [1, 2])) {
            // Boucle pour garantir des bornes d'intervalle valides
            while (true) {
                $borne_inferieure = readline("Entrez la borne inférieure de l'intervalle : ");
                $borne_superieure = readline("Entrez la borne supérieure de l'intervalle : ");

                // Vérification que les bornes sont bien des nombres et que la borne inférieure est plus petite
                if (is_numeric($borne_inferieure) && is_numeric($borne_superieure) && $borne_inferieure < $borne_superieure) {
                    break; // Sortie de la boucle si les bornes sont valides
                } else {
                    echo "Erreur : Veuillez entrer des nombres valides pour les bornes.\n";
                }
            }
            echo "Votre intervalle est : [$borne_inferieure, $borne_superieure]\n";
        }

        // Saisie de la tolérance et du nombre maximal d'itérations pour la méthode choisie
        while (true) {
            $tolerance = readline("Entrez la tolérance souhaitée (ex: 0.0001) : ");
            $nombre_max_iterations = readline("Entrez le nombre maximal d'itérations (ex: 100) : ");

            // Vérification que la tolérance et le nombre d'itérations sont valides et positifs
            if (is_numeric($tolerance) && $tolerance > 0 && is_numeric($nombre_max_iterations) && $nombre_max_iterations > 0) {
                break; // Sortie de la boucle si les valeurs sont valides
            } else {
                echo "Erreur : les valeurs de tolérance et d'itérations doivent être supérieures à zéro.\n";
            }
        }

        // Affichage des paramètres saisis pour la résolution
        echo "Tolérance : $tolerance, Nombre maximal d'itérations : $nombre_max_iterations\n";

        // Exécution de la méthode choisie en fonction du choix de l'utilisateur
        $racine = null;
        switch ($choix) {
            case 1:
                $racine = methode_de_dichotomie($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 2:
                $racine = methode_de_la_secante($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 3:
                // Pour la méthode de Newton-Raphson, une estimation initiale est demandée
                $x_initiale = readline("Entrez une estimation initiale de la racine : ");
                $derivee_fonction_str = readline("Entrez la dérivée de la fonction : ");
                $derivee_fonction = create_function_from_string($derivee_fonction_str);
                $racine = methode_de_newton_raphson($fonction, $derivee_fonction, $x_initiale, $tolerance, $nombre_max_iterations);
                break;
            case 4:
                // Pour la méthode du Point Fixe, une estimation initiale est également demandée
                $x_initiale = readline("Entrez une estimation initiale de la racine : ");
                $racine = methode_du_point_fixe($fonction, $x_initiale, $tolerance, $nombre_max_iterations);
                break;
        }

        // Affichage de la racine trouvée ou d'un message si aucune racine n'a été trouvée
        if ($racine !== null) {
            echo "La racine trouvée est : $racine\n";
        } else {
            echo "Aucune racine n'a été trouvée.\n";
        }

        // Demande à l'utilisateur s'il souhaite recommencer ou terminer
        $choix_recommencer_Terminer = strtolower(readline("Souhaitez-vous recommencer ? (oui/non) : "));
        $action = ($choix_recommencer_Terminer === "oui"); // Continue si "oui", termine si "non"
    }
}

// Fonction pour créer une fonction exécutable à partir d'une chaîne de caractères
function create_function_from_string($fonction_str) {
    // Remplacement de l'opérateur exponentiel ** par ^ pour compatibilité
    $fonction_str = str_replace("**", "^", $fonction_str);
    return function($x) use ($fonction_str) {
        $result = null; // Define the variable $result
        eval($result .'='. $fonction_str . ';'); // Exécution de la fonction avec eval()

        return $result;
    };
}

// Appel de la fonction principale pour démarrer le programme
main();

