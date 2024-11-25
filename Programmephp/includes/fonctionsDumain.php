<?php

include '/../includes/fonctionsTableaux.php';
include '/../includes/MethodeDeResolution.php';
include '/../includes/AccueilEtMenus.php';

function choisir_methode() {
    // Affiche le menu pour choisir la méthode de résolution et gère la saisie de l'utilisateur.
    methode_resolution();

    while (true) {
        try {
            echo "Entrez le numéro de la méthode souhaitée : ";
            $choix = intval(trim(fgets(STDIN)));
            if ($choix >= 1 && $choix <= 5) {
                return $choix;
            } else {
                echo "Erreur : Le numéro doit être un entier compris entre 1 et 5.\n";
            }
        } catch (Exception $e) {
            echo "Erreur : Veuillez entrer un nombre entier. ({$e->getMessage()})\n";
        }
    }
}

function saisir_fonction_et_ensemble_definition() {
    // Demande à l'utilisateur de saisir la fonction et affiche l'ensemble de définition.
    $fonction_str = saisir_fonction();

    try {
        // Crée une fonction PHP interprétable à partir de l'entrée utilisateur
        $fonction = function ($x) use ($fonction_str) {
            eval("\$result = $fonction_str;");
            return $result;
        };

        echo "Fonction interprétée : f(x) = {$fonction_str}\n";
        ensemble_de_definition($fonction_str); // Affiche l'ensemble de définition
        return [$fonction, $fonction_str];
    } catch (Exception $e) {
        echo "Erreur lors de l'interprétation de la fonction : {$e->getMessage()}\n";
        return [null, null];
    }
}

function saisir_bornes_si_necessaire($choix) {
    // Demande des bornes nécessaires selon la méthode choisie
    if (in_array($choix, [1, 2, 5])) {
        return demander_bornes();
    }
    return [null, null];
}

function saisir_tolerance_et_max_iterations() {
    // Demande la tolérance et le nombre maximal d'itérations
    return demander_tolerance_et_max_iterations();
}

function appliquer_methode($choix, $fonction, $fonction_expr, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations) {
    // Appliquer la méthode choisie pour résoudre l'équation
    $racine = null;
    $tableau = null;

    try {
        switch ($choix) {
            case 1:
                [$racine, $tableau] = methode_de_dichotomie($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 2:
                [$racine, $tableau] = methode_de_la_secante($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 3:
                $derivee_fonction = diff($fonction_expr);
                echo "Entrez une valeur initiale pour x : ";
                $x_initiale = floatval(trim(fgets(STDIN)));
                [$racine, $tableau] = methode_de_newton($fonction, $derivee_fonction, $x_initiale, $tolerance, $nombre_max_iterations);
                break;
            case 4:
                echo "Entrez la fonction de récurrence φ(x) : ";
                $phi_str = trim(fgets(STDIN));
                $phi = function ($x) use ($phi_str) {
                    eval("\$result = $phi_str;");
                    return $result;
                };
                echo "Entrez une valeur initiale pour x : ";
                $x_initiale = floatval(trim(fgets(STDIN)));
                [$racine, $tableau] = methode_du_point_fixe($phi, $x_initiale, $tolerance, $nombre_max_iterations);
                break;
            case 5:
                echo "Entrez la valeur du pas : ";
                $pas = floatval(trim(fgets(STDIN)));
                [$racine, $tableau] = methode_de_balayage($fonction, $borne_inferieure, $borne_superieure, $pas, $tolerance);
                break;
            default:
                echo "Erreur : Méthode de résolution inconnue.\n";
                break;
        }

        if ($tableau !== null) {
            afficher_tableau($choix, $tableau);
            enregistrer_tableau($tableau);
        }
    } catch (Exception $e) {
        echo "Erreur : {$e->getMessage()}. Veuillez réessayer.\n";
    }

    return $racine;
}

function afficher_tableau($choix, $tableau) {
    // Affiche le tableau des itérations en fonction de la méthode choisie
    if (in_array($choix, [1, 2, 3, 4])) {
        afficher_tableau_dichotomie($tableau);
    } else {
        echo "Aucune méthode spécifique pour afficher le tableau.\n";
    }
}

function afficher_racine($racine) {
    // Affiche la racine trouvée
    if ($racine !== null) {
        echo "La racine trouvée est : {$racine}\n";
    } else {
        echo "Aucune racine trouvée.\n";
    }
}

function demander_recommencer() {
    // Demande à l'utilisateur s'il souhaite recommencer ou quitter
    echo "Souhaitez-vous recommencer ? (oui/non) : ";
    $reponse = strtolower(trim(fgets(STDIN)));
    return $reponse === "oui";
}

function print_method_name($choix) {
    // Associe chaque méthode à son nom
    $methods = [
        1 => "METHODE DE DICHOTOMIE",
        2 => "METHODE DE LA SECANTE",
        3 => "METHODE DE NEWTON-RAPHSON",
        4 => "METHODE DU POINT FIXE",
        5 => "METHODE DE BALAYAGE",
    ];

    echo "*************** {$methods[$choix]} ***************\n";
}
