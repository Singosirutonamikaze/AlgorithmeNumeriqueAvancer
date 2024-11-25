<?php

// Fonction pour afficher le tableau des intervalles de balayage
function afficher_tableau_balayage($tableau_intervals) {
    echo "\nTableau des intervalles de balayage :\n";
    echo str_pad("Intervalle", 20) . str_pad("Borne Inf.", 18) . str_pad("Borne Sup.", 18) . str_pad("f(Borne Inf.)", 18) . str_pad("f(Borne Sup.)", 18) . "\n";
    echo str_repeat("-", 90) . "\n";

    foreach ($tableau_intervals as $interval_data) {
        echo str_pad($interval_data['intervalle'], 20) .
             str_pad($interval_data['borne_inferieure'], 18) .
             str_pad($interval_data['borne_superieure'], 18) .
             str_pad($interval_data['f(borne_inferieure)'], 18) .
             str_pad($interval_data['f(borne_superieure)'], 18) . "\n";
    }
}

// Fonction pour afficher le tableau stylisé pour la dichotomie
function afficher_tableau_dichotomie($tableau) {
    echo str_repeat("*", 100) . "\n";
    echo str_pad("Iteration", 12) . "|" . str_pad("Borne Inférieure", 20) . "|" . str_pad("Borne Supérieure", 20) . "|" .
         str_pad("f(Borne Inférieure)", 25) . "|" . str_pad("f(Borne Supérieure)", 25) . "|" .
         str_pad("f(Borne Inf.) * f(Borne Sup.)", 25) . "\n";
    echo str_repeat("*", 100) . "\n";

    foreach ($tableau as $ligne) {
        echo str_pad($ligne['iteration'], 12) .
             str_pad($ligne['borne_inferieure'], 20) .
             str_pad($ligne['borne_superieure'], 20) .
             str_pad($ligne['signe_f(borne_inferieure)'], 25) .
             str_pad($ligne['signe_f(borne_superieure)'], 25) .
             str_pad($ligne['signe_(f(borne_inferieure)*f(borne_superieure))'], 25) . "\n";
    }

    echo str_repeat("*", 100) . "\n";
}

// Fonction pour afficher le tableau de la méthode de la sécante
function afficher_tableau_secante($tableau_interactions) {
    echo "\nTableau des itérations :\n";

    // En-têtes des colonnes
    $en_tetes = ['Iteration', 'Borne Inf.', 'Borne Sup.', 'Estimation', 'f(Estimation)', 'Diff. Bornes'];
    echo str_pad($en_tetes[0], 12) . str_pad($en_tetes[1], 18) . str_pad($en_tetes[2], 18) .
         str_pad($en_tetes[3], 18) . str_pad($en_tetes[4], 18) . str_pad($en_tetes[5], 18) . "\n";
    echo str_repeat("-", 90) . "\n";

    foreach ($tableau_interactions as $iteration_data) {
        echo str_pad($iteration_data['iteration'], 12) .
             str_pad($iteration_data['borne_inferieure'], 18) .
             str_pad($iteration_data['borne_superieure'], 18) .
             str_pad($iteration_data['estimation'], 18) .
             str_pad($iteration_data['f(estimation)'], 18) .
             str_pad($iteration_data['différence_bornes'], 18) . "\n";
    }
}

// Fonction pour afficher le tableau du point fixe
function afficher_tableau_point_fixe($tableau_interactions) {
    echo "\nTableau des itérations :\n";
    echo str_pad("Iteration", 12) . str_pad("x", 18) . str_pad("phi(x)", 18) . str_pad("Différence", 18) . "\n";
    echo str_repeat("-", 70) . "\n";

    foreach ($tableau_interactions as $iteration_data) {
        echo str_pad($iteration_data['iteration'], 12) .
             str_pad($iteration_data['x'], 18) .
             str_pad($iteration_data['phi(x)'], 18) .
             str_pad($iteration_data['différence'], 18) . "\n";
    }
}
