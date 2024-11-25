<?php
// Importation des modules necessaires
require 'vendor/autoload.php'; // Si vous utilisez une bibliotheque comme symfony/maths
use MathPHP\Functions\Special;

// Fonction pour afficher un message de bienvenue avec un cadre de texte
function rectangle_bienvenue_complexe() {
    $phrase = "      BIENVENUE DANS LA RESOLUTION D'EQUATION F(x) = 0     ";
    $largeur = strlen($phrase) + 6;

    echo str_repeat("*", $largeur) . "\n";
    echo "*" . str_repeat(" ", $largeur - 2) . "*\n";
    echo "* *" . str_pad($phrase, $largeur - 6, " ", STR_PAD_BOTH) . "* *\n";
    echo "*" . str_repeat(" ", $largeur - 2) . "*\n";
    echo str_repeat("*", $largeur) . "\n";
}

// Fonction permettant de choisir la méthode de résolution parmi plusieurs options
function methode_resolution() {
    echo "*******************Choisissez la méthode de résolution *******************\n\n";
    echo "                     1. La méthode de Dichotomie\n";
    echo "                     2. La méthode de la Sécante\n";
    echo "                     3. La méthode de Newton-Raphson\n";
    echo "                     4. La méthode du Point Fixe\n";
    echo "                     5. La méthode de Balayage\n\n";
}

// Fonction pour afficher le menu de choix de fonction
function afficher_menu() {
    echo "\n******************* Menu de choix de fonction *******************\n\n";
    echo "Choisissez le type de fonction que vous souhaitez entrer :\n\n";
    echo "     1. Polynôme (ex: x^2 + 3*x - 8)\n";
    echo "     2. Trigonométrique (ex: cos(x) + x)\n";
    echo "     3. Logarithmique (ex: log(x) + x^2)\n";
    echo "     4. Racine carrée (ex: sqrt(x) + x/2)\n";
    echo "     5. Rationnelle (ex: (x + 1) / (x - 2))\n";
    echo "     6. Fonction générale (ex: (x^3 - sin(x) + log(x))/(x^2 + 1))\n\n";
}

// Fonction pour saisir une fonction mathématique
function saisir_fonction() {
    afficher_menu();

    $types_fonction = [
        "1" => "Polynôme",
        "2" => "Trigonométrique",
        "3" => "Logarithmique",
        "4" => "Racine carrée",
        "5" => "Rationnelle",
        "6" => "Fonction générale"
    ];

    while (true) {
        $type_fonction = readline("Entrez le numéro du type de fonction : ");

        if (!array_key_exists($type_fonction, $types_fonction)) {
            echo "Choix invalide. Veuillez entrer un nombre entre 1 et 6.\n\n";
            continue;
        }

        echo "\nVous avez choisi : " . $types_fonction[$type_fonction] . "\n";
        echo "Veuillez entrer votre fonction mathématique (par exemple, x^2 + 3*x - 8) : \n";

        $fonction = readline("Entrez votre fonction mathématique ({$types_fonction[$type_fonction]}): ");

        try {
            // Valider la fonction ici (en PHP, vous pourriez utiliser des expressions personnalisées ou une bibliothèque de calcul symbolique)
            // Pour l'instant, nous acceptons la saisie directement
            echo "\nVotre fonction saisie '$fonction' a été validée avec succès.\n";
            return $fonction;
        } catch (Exception $e) {
            echo "\nErreur : La fonction saisie est invalide ou contient une erreur de syntaxe.\n";
            echo "Vérifiez votre saisie et essayez à nouveau.\n";
        }
    }
}

// Fonction pour saisir la tolérance et le nombre d'itérations
function saisir_tolerance_et_iterations() {
    while (true) {
        try {
            $tolerance = (float) readline("Entrez la tolérance souhaitée (ex: 0.0001, 1.0e-5) : \n");
            $iterations = (int) readline("Entrez le nombre maximal d'itérations : \n");

            if ($tolerance > 0 && $iterations > 0) {
                echo "Votre tolérance est : $tolerance\n";
                echo "Votre nombre maximal d'itérations est : $iterations\n";
                return [$tolerance, $iterations];
            } else {
                echo "Erreur : La tolérance et le nombre d'itérations doivent être supérieurs à zéro.\n";
            }
        } catch (Exception $e) {
            echo "Erreur : Veuillez entrer des valeurs valides.\n";
        }
    }
}

// Fonction pour valider une borne
function verifier_ensemble_de_definition($fonction, $borne) {
    try {
        // Implémentez ici les vérifications spécifiques à votre besoin (logarithmes, racines carrées, etc.)
        return true; // Placeholder pour indiquer que tout va bien
    } catch (Exception $e) {
        echo "Erreur lors de la vérification de l'ensemble de définition : " . $e->getMessage() . "\n";
        return false;
    }
}
