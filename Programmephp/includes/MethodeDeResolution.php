<?php
include '/../includes/fonctionsTableaux.php';
include '/../includes/MethodeDeResolution.php';
include '/../includes/AcccueilEtMenus.php';

function methode_de_balayage($fonction, $borneInferieure, $borneSuperieure, $pas, $tolerance) {
    // Tableau pour stocker les intervalles
    $tableauIntervals = [];
    $variableX = $borneInferieure;

    echo "Début du balayage :\n";

    // Parcours de l'intervalle
    while ($variableX <= $borneSuperieure) {
        // Calcul des bornes
        $borneInf = $variableX;
        $borneSup = $variableX + $pas;
        $fBorneInf = $fonction($borneInf);
        $fBorneSup = $fonction($borneSup);

        // Vérifie si la fonction change de signe entre les deux bornes
        $changementSigne = $fBorneInf * $fBorneSup < 0;

        // Affiche l'intervalle en cours et la détection du changement de signe
        echo "Intervalle [$borneInf, $borneSup] : f(borne_inferieure) = " . round($fBorneInf, 6) . 
             ", f(borne_superieure) = " . round($fBorneSup, 6) . "\n";
        echo "Changement de signe : " . ($changementSigne ? 'Oui' : 'Non') . "\n";

        // Enregistre les informations dans le tableau
        $tableauIntervals[] = [
            'intervalle' => "[$borneInf, $borneSup]",
            'borne_inferieure' => $borneInf,
            'borne_superieure' => $borneSup,
            'f(borne_inferieure)' => round($fBorneInf, 6),
            'f(borne_superieure)' => round($fBorneSup, 6),
            'changement_de_signe' => $changementSigne ? "Oui" : "Non"
        ];

        // Si un changement de signe est détecté, applique la méthode de dichotomie pour trouver la racine
        if ($changementSigne) {
            echo "Changement de signe détecté dans l'intervalle [$borneInf, $borneSup]\n";
            $racine = methode_de_dichotomie($fonction, $borneInf, $borneSup, $tolerance, 100);
            echo "Racine trouvée : $racine\n";
            return [$racine, $tableauIntervals];
        }

        // Passe à l'intervalle suivant
        $variableX += $pas;
    }

    echo "Aucune racine trouvée dans l'intervalle donné.\n";
    return null;
}

function methode_de_dichotomie($fonction, $borneInferieure, $borneSuperieure, $tolerance, $nombreMaxIterations) {
    $tableauInteractions = [];

    // Vérification si la racine est encadrée
    if ($fonction($borneInferieure) * $fonction($borneSuperieure) > 0) {
        echo "La racine n'est pas encadrée entre [{$borneInferieure}, {$borneSuperieure}].\n";
        return null;
    }

    for ($iteration = 1; $iteration <= $nombreMaxIterations; $iteration++) {
        $pointMilieu = ($borneInferieure + $borneSuperieure) / 2;
        $valeurMilieu = $fonction($pointMilieu);

        $tableauInteractions[] = [
            'iteration' => $iteration,
            'borneInferieure' => $borneInferieure,
            'borneSuperieure' => $borneSuperieure,
            'pointMilieu' => $pointMilieu,
            'valeurMilieu' => $valeurMilieu
        ];

        echo "Iteration {$iteration}: Intervalle actuel = [{$borneInferieure}, {$borneSuperieure}]\n";

        if (abs($valeurMilieu) <= $tolerance || abs($borneSuperieure - $borneInferieure) < $tolerance) {
            echo "Solution trouvée : x = {$pointMilieu} après {$iteration} itérations\n";
            return [$pointMilieu, $tableauInteractions];
        }

        if ($valeurMilieu * $fonction($borneSuperieure) < 0) {
            $borneInferieure = $pointMilieu;
        } else {
            $borneSuperieure = $pointMilieu;
        }
    }

    return [($borneInferieure + $borneSuperieure) / 2, $tableauInteractions];
}

function methode_de_la_secante($fonction, $borneInferieure, $borneSuperieure, $tolerance, $nombreMaxIterations) {
    $tableauInteractions = [];

    for ($iteration = 1; $iteration <= $nombreMaxIterations; $iteration++) {
        $valeurInferieure = $fonction($borneInferieure);
        $valeurSuperieure = $fonction($borneSuperieure);

        if (abs($valeurSuperieure - $valeurInferieure) < 1e-10) {
            echo "Division par zéro évitée dans la méthode de la sécante.\n";
            return null;
        }

        $estimation = $borneInferieure - $valeurInferieure * ($borneSuperieure - $borneInferieure) / ($valeurSuperieure - $valeurInferieure);
        $valeurEstimation = $fonction($estimation);

        $tableauInteractions[] = [
            'iteration' => $iteration,
            'borneInferieure' => $borneInferieure,
            'borneSuperieure' => $borneSuperieure,
            'estimation' => $estimation,
            'valeurEstimation' => $valeurEstimation
        ];

        echo "Iteration {$iteration}: Estimation = {$estimation}, Valeur = {$valeurEstimation}\n";

        if (abs($valeurEstimation) <= $tolerance) {
            echo "Solution trouvée : x = {$estimation} après {$iteration} itérations\n";
            return [$estimation, $tableauInteractions];
        }

        if ($valeurEstimation * $valeurSuperieure < 0) {
            $borneInferieure = $estimation;
        } else {
            $borneSuperieure = $estimation;
        }
    }

    return [$borneInferieure, $tableauInteractions];
}

function methode_de_newton_raphson($fonction, $derivee, $xInitiale, $tolerance, $nombreMaxIterations) {
    $x = $xInitiale;

    for ($iteration = 1; $iteration <= $nombreMaxIterations; $iteration++) {
        $valeur = $fonction($x);
        $valeurDerivee = $derivee($x);

        if (abs($valeurDerivee) < 1e-10) {
            echo "La dérivée est nulle. Échec de la méthode de Newton-Raphson.\n";
            return null;
        }

        $x -= $valeur / $valeurDerivee;

        echo "Iteration {$iteration}: x = {$x}, Valeur = {$valeur}\n";

        if (abs($valeur) <= $tolerance) {
            echo "Solution trouvée : x = {$x} après {$iteration} itérations\n";
            return $x;
        }
    }

    echo "Pas de convergence après {$nombreMaxIterations} itérations.\n";
    return null;
}

function methodeDuPointFixe($phi, $xInitiale, $tolerance, $nombreMaxIterations) {
    $x = $xInitiale;
    $tableauInteractions = [];

    for ($iteration = 1; $iteration <= $nombreMaxIterations; $iteration++) {
        $phiX = $phi($x);

        $tableauInteractions[] = [
            'iteration' => $iteration,
            'x' => $x,
            'phiX' => $phiX,
            'difference' => abs($phiX - $x)
        ];

        echo "Iteration {$iteration}: x = {$x}, phi(x) = {$phiX}, Différence = " . abs($phiX - $x) . "\n";

        if (abs($phiX - $x) <= $tolerance) {
            echo "Convergence atteinte : x = {$phiX} après {$iteration} itérations\n";
            return [$phiX, $tableauInteractions];
        }

        $x = $phiX;
    }

    echo "Pas de convergence après {$nombreMaxIterations} itérations.\n";
    return null;
}


function balayageNewton($fonction, $deriveeFonction, $borneInferieure, $borneSuperieure, $tolerance, $nombreMaxIterations) {
    $pasDeBalayage = ($borneSuperieure - $borneInferieure) / 5;
    $xInitiale = $borneInferieure;

    echo "Balayage pour trouver une valeur initiale convenable pour Newton-Raphson\n";

    // Essai de différentes valeurs initiales pour Newton-Raphson
    while ($xInitiale <= $borneSuperieure) {
        echo "Essai avec x_initiale = $xInitiale\n";
        $solution = methode_de_newton_raphson($fonction, $deriveeFonction, $xInitiale, $tolerance, $nombreMaxIterations);
        if ($solution !== null) {
            echo "Solution trouvée avec x_initiale = $xInitiale: x = $solution\n";
            return $solution;
        }
        $xInitiale += $pasDeBalayage;
    }

    echo "Aucune solution trouvée pour Newton-Raphson avec le balayage.\n";
    return null;
}

function ensembleDeDefinition($fonctionStr) {
    echo "Cette fonctionnalité nécessite une bibliothèque tierce pour évaluer les ensembles de définition en PHP.\n";
    // Optionnel : implémentation avec MathPHP ou autre bibliothèque.
    return null;
}
