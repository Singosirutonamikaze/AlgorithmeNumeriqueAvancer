<?php
// Fonction pour afficher un message de bienvenue encadré
function rectangle_bienvenue_complexe()
{
    // Définir la phrase de bienvenue et la largeur du rectangle
    $phrase = " BIENVENUE ";
    $largeur = strlen($phrase) + 6; // Largeur avec marges supplémentaires pour le cadre
    $hauteur = 5; // Hauteur du rectangle

    // Dessiner la première ligne (double bordure d'étoiles)
    echo str_repeat('*', $largeur) . "\n";

    // Ligne avec bordure interne et espace
    echo '*' . str_repeat(' ', $largeur - 2) . "*\n";

    // Ligne du milieu avec la phrase entourée de marges et bordure interne
    echo '* ' . $phrase . ' *' . "\n";

    // Ligne avec bordure interne et espace
    echo '*' . str_repeat(' ', $largeur - 2) . "*\n";

    // Dernière ligne (double bordure d'étoiles)
    echo str_repeat('*', $largeur) . "\n";
}

// Fonction permettant le choix de la méthode de résolution
function methode_resolution()
{
    echo "Choisissez une méthode de résolution :\n";
    echo "      1. Méthode de dichotomie\n";
    echo "      2. Méthode de la sécante\n";
    echo "      3. Méthode de Newton-Raphson\n";
    echo "      4. Méthode du point fixe\n";
}

// Fonction pour la saisie de la fonction mathématique
function saisir_fonction()
{
    // Affichage des options de type de fonction à l'utilisateur
    echo "******************* Menu de choix de fonction *******************\n";
    echo "Choisissez le type de fonction que vous souhaitez entrer :\n";
    echo "     1. Polynôme (ex: x**2 + 3*x - 8)\n";
    echo "     2. Trigonométrique (ex: sin(x), cos(x) + x)\n";
    echo "     3. Logarithmique (ex: ln(x), log(x) + x**2)\n";
    echo "     4. Racine carrée (ex: sqrt(x) + x/2)\n";
    echo "     5. Rationnelle (ex: (x + 1) / (x - 2))\n";
    echo "\n";

    // Boucle principale pour choisir le type de fonction
    while (true) {
        // Demande à l'utilisateur de saisir le numéro correspondant au type de fonction
        $type_fonction = readline("Entrez le numéro du type de fonction : ");

        // Vérification que le choix est bien un numéro entre 1 et 5
        if ($type_fonction >= 1 && $type_fonction <= 5) {
            break;
        } else {
            echo "Choix invalide. Veuillez entrer un nombre entre 1 et 5.\n";
        }
    }

    // Boucle pour demander à l'utilisateur de saisir la fonction mathématique
    while (true) {
        // Demande de la fonction mathématique
        $fonction = readline("Entrez votre fonction mathématique : ");

        // Définition de l'expression régulière et du message d'erreur selon le type de fonction
        switch ($type_fonction) {
            case 1: // Polynôme
                $pattern = '/^[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction polynomiale.";
                break;
            case 2: // Trigonométrique
                $pattern = '/^[-+]?(\d+)?(sin|cos|tan|asin|acos|atan)(\(\s*x\s*\))([+\-*/]?\d*(sin|cos|tan|asin|acos|atan)(\(\s*x\s*\))?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction trigonométrique.";
                break;
            case 3: // Logarithmique
                $pattern = '/^[-+]?(\d+)?(ln|log)(\(\s*x\s*\))([+\-*/]?\d*(ln|log)(\(\s*x\s*\))?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction logarithmique.";
                break;
            case 4: // Racine carrée
                $pattern = '/^[-+]?(\d+)?(sqrt)(\(\s*x\s*\))([+\-*/]?\d*(sqrt)(\(\s*x\s*\))?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction racine carrée.";
                break;
            case 5: // Rationnelle
                $pattern = '/^[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*\/[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction rationnelle.";
                break;
        }

        // Vérification de la validité de la fonction mathématique
        if (preg_match($pattern, str_replace(' ', '', strtolower($fonction)))) {
            return $fonction; // Retourne la fonction valide
        } else {
            echo $message . "\n"; // Affiche un message d'erreur si la fonction n'est pas valide
        }
    }
}
