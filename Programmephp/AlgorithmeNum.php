<?php

include '/../includes/fonctionsTableaux.php';
include '/../includes/MethodeDeResolution.php';
include '/../includes/AcccueilEtMenus.php';

function main() {
    //Fonction principale qui gère le programme.
    $action = true;

    rectangle_bienvenue_complexe();

    while ($action) {
        $choix = print_method_name($choix);
        methode_resolution();
        [$fonction, $fonction_expr] = saisir_fonction_et_ensemble_definition(); // $fonction contient la fonction, $fonction_expr contient la fonction expr
        if($fonction == null){
            continue;
        }
        [$borne_inferieure, $borne_superieure] = saisir_bornes_si_necessaire($choix, $fonction_expr);
       
        echo("Votre intervalle est : [$borne_inferieure, $borne_superieure]");
        [$tolerance, $nombre_max_iterations] = saisir_tolerance_et_iterations();
        $racine = appliquer_methode($choix, $fonction, $fonction_expr, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
        $action = demander_recommencer();
    }
}

main();
