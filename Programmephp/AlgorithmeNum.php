<?php

include '/../includes/MethodeDeResolution.php';
include '/../includes/AccueilEtMenus.php';

function main() {
    //Fonction principale qui gère le programme.
    $action = true;

    rectangle_bienvenue_complexe();

    while ($action) {
        $choix = choisir_methode();
        echo_method_name($choix);
        $fonction, $fonction_expr = saisir_fonction_et_ensemble_definition(); // $fonction contient la fonction, $fonction_expr contient la fonction expr
        if($fonction == null){
            continue;
        }
        $borne_inferieure, $borne_superieure = saisir_bornes_si_necessaire($choix, $fonction_expr);
       
        echo("Votre intervalle est : [$borne_inferieure, $borne_superieure]");
        $tolerance, $nombre_max_iterations = saisir_tolerance_et_iterations_de_resolution();
        $racine = appliquer_methode($choix, $fonction, $fonction_expr, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
        $action = demander_recommencer();
    }
}

main();
