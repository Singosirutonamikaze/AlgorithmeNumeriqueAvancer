<?php
// Fonction pour la méthode de dichotomie avec affichage des intervalles
function methode_de_dichotomie($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations)
{
    // On évalue la fonction f à la borne inférieure
    $valeur_borne_inferieure = $fonction($borne_inferieure);

    // Si f(a) est proche de 0, a est la racine
    if (abs($valeur_borne_inferieure) <= $tolerance) {
        return $borne_inferieure;
    }

    // On évalue la fonction f à la borne supérieure
    $valeur_borne_superieure = $fonction($borne_superieure);

    // Si f(b) est proche de 0, b est la racine
    if (abs($valeur_borne_superieure) <= $tolerance) {
        return $borne_superieure;
    }

    // Vérifie si la fonction a une racine entre a et b
    if ($valeur_borne_inferieure * $valeur_borne_superieure > 0.0) {
        echo ("La racine n'est pas encadrée entre [" . $borne_inferieure . ";" . $borne_superieure . "]\n");
        exit(0);
    }

    // Calcul du nombre maximum d'itérations nécessaires
    $nombre_iterations = (int) ceil(log(abs($borne_superieure - $borne_inferieure) / $tolerance) / log(2.0));

    // On effectue la dichotomie
    for ($i = 0; $i < min($nombre_iterations + 1, $nombre_max_iterations); $i++) {
        $point_milieu = ($borne_inferieure + $borne_superieure) / 2.0;  // Point milieu
        $valeur_point_milieu = $fonction($point_milieu);  // Valeur de f au point milieu

        // Affichage de l'intervalle actuel
        echo ("Iteration {$i}: Intervalle actuel = [" . $borne_inferieure . ", " . $borne_superieure . "]\n");

        // Si f(c) est proche de 0, c est la racine
        if ($valeur_point_milieu === 0.0 || ($borne_superieure - $borne_inferieure) < $tolerance) {
            echo ("La solution trouvée : x = $point_milieu après $i iterations\n");
            return $point_milieu;
        }

        // Mise à jour des bornes a ou b selon le signe de f(c)
        if ($valeur_point_milieu * $valeur_borne_inferieure < 0.0) {
            $borne_inferieure = $point_milieu;
            $valeur_borne_inferieure = $valeur_point_milieu;
        } else {
            $borne_superieure = $point_milieu;
            $valeur_borne_superieure = $valeur_point_milieu;
        }
    }
    // Retourne la moyenne des bornes a et b comme approximation de la racine
    return (($borne_inferieure + $borne_superieure) / 2.0);
}

// Fonction pour la méthode de la sécante
function methode_de_la_secante($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations)
{
    // Évaluation de la fonction à la borne inférieure
    $valeur_borne_inferieure = $fonction($borne_inferieure);

    // Si f(a) est proche de 0, a est la racine
    if(abs($valeur_borne_inferieure) <= $tolerance) {
        return $borne_inferieure;
    }

    // Évaluation de la fonction à la borne supérieure
    $valeur_borne_superieure = $fonction($borne_superieure);

    // Si f(b) est proche de 0, b est la racine
    if(abs($valeur_borne_superieure) <= $tolerance) {
        return $borne_superieure;
    }

    for ($i = 0; $i < $nombre_max_iterations; $i++) {
        // Calcul de la nouvelle approximation en utilisant la formule de la sécante
        $nouveau = $borne_superieure - $valeur_borne_superieure * ($borne_superieure - $borne_inferieure) / ($valeur_borne_superieure - $valeur_borne_inferieure);

        // Vérification si la solution est trouvée
        if (abs($fonction($nouveau)) < $tolerance) {
            echo ("Solution trouvée : x = $nouveau après $i iterations\n");
            return $nouveau;
        }

        // Mise à jour des bornes pour l'itération suivante
        $borne_inferieure = $borne_superieure;
        $borne_superieure = $nouveau;
        $valeur_borne_inferieure = $valeur_borne_superieure;
        $valeur_borne_superieure = $fonction($borne_superieure);
    }
    echo ("Solution non trouvée après le nombre maximal d'itérations.\n");
    return null;
}

// Fonction pour la méthode de Newton-Raphson
function methode_de_newton_raphson($fonction, $derivee_fonction, $initial, $tolerance, $nombre_max_iterations)
{
    $x = $initial; // Point initial
    for ($i = 0; $i < $nombre_max_iterations; $i++) {
        $valeur_fonction = $fonction($x);
        $valeur_derivee = $derivee_fonction($x);

        // Vérification si la dérivée est nulle (division par zéro)
        if ($valeur_derivee == 0) {
            echo ("Dérivée nulle à x = $x. La méthode ne peut pas continuer.\n");
            return null;
        }

        // Calcul de la nouvelle approximation
        $nouveau_x = $x - $valeur_fonction / $valeur_derivee;

        // Vérification de la tolérance
        if (abs($nouveau_x - $x) < $tolerance) {
            echo ("Solution trouvée : x = $nouveau_x après $i iterations\n");
            return $nouveau_x;
        }

        $x = $nouveau_x; // Mise à jour de x pour la prochaine itération
    }
    echo ("Solution non trouvée après le nombre maximal d'itérations.\n");
    return null;
}

// Fonction pour la méthode du point fixe
function methode_du_point_fixe($g_fonction, $initial, $tolerance, $nombre_max_iterations)
{
    $x = $initial; // Point initial
    for ($i = 0; $i < $nombre_max_iterations; $i++) {
        $nouveau_x = $g_fonction($x);

        // Vérification de la tolérance
        if (abs($nouveau_x - $x) < $tolerance) {
            echo ("Solution trouvée : x = $nouveau_x après $i iterations\n");
            return $nouveau_x;
        }

        $x = $nouveau_x; // Mise à jour de x pour la prochaine itération
    }
    echo ("Solution non trouvée après le nombre maximal d'itérations.\n");
    return null;
}

