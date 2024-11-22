<?php

function choisir_methode(){
    //Affiche le menu pour choisir la méthode de résolution et gère la saisie de l'utilisateur.
    methode_resolution();

    while(true){
        try {
            $choix = readline("Entrez le numéro de la méthode (1 - 5) :");
            if(1 <= $choix <= 5){
                return $choix;
            }else{
                echo(" le numéro doit être un entier compris entre 1 et 5.\n");
            }
        } catch (ValueError $th) {
            echo("Erreur : veuillez entrer un nombre entier.($th)\n");
        }
    }
}
// Demander à l'utilisateur de saisir la fonction et affiche l'ensemble de:definition
function saisir_fonction_et_ensemble_definition(){
    //Demande à l'utilisateur de saisir la fonction et affiche l'ensemble de définition.
    $fonction_str = saisir_fonction();
    try{
        // Convertir la chaîne de caractères en une expression mathématique que sympy peut traiter
        $fonction_expr = sympify($fonction_str);
        //Convertir l'expression sympy en une fonction lambda utilisable par Python
        $fonction = eval("lambda x: $fonction_expr");
        echo("Fonction interprétée : f(x) =  $fonction_expr");
        ensemble_de_definition($fonction_str);  # Afficher l'ensemble de définition de la fonction
        return array($fonction, $fonction_expr);
    }catch(ValueError $e){
        echo("Erreur lors de l'interprétation de la fonction : $e");
        return array(null, null);
    }
}

//Fonction pour saisir les bornes nécéssaires selon la methode choisie
function saisir_bornes_si_necessaire($chois, $fonction_expr){
    // Demande des bornes necessaires selon la methode choisie
    if(in_array($choix,[1,2,3])){
        return demander_bornes();
    }   
    return(array(null,null));
}

//Fonction pour saisir la tolérance et la nombre maximal d'itérations
function saisir_tolerance_et_max_iterations(){
    // Demande de la tolérance et du nombre maximal d'itérations
    return saisir_tolerance_et_max_iterations();
}

//Fonction pour appliquer les methodes de resolution
function appliquer_methode($choix, $fonction, $fonction_expr, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations){
    //Appliquer la methode choisie pour reoudre l'équation
    $racine = null;
    $tableau = null;
    try {
        switch ($choix) {
            case 1:
                $racine, $tableau = methode_de_dichotomie($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 2: 
                $racine, $tableau = methode_de_la_secante($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 3:
                $derivee_fonction = diff($fonction_expr);
                $x_initiale = float(readline("Entrez l'estimation initiale de la racine (exemple: 2) : Xo = "));
                $racine, $tableau = methode_de_newton($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 4:
                $phi_str = readline("Entrez l'expression de phi(x) (exemple : sqrt(2*x - 1)) : ");
                $phi = creer_phi($phi_str);
                $x_initiale = float(readline("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "));
                $racine, $tableau = methode_de_bisection($phi, $x_initiale, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 5:
                pas = float(readline("Entrez le pas pour le balayage (exemple: 0.1) : "));
                $racine, $tableau = methode_de_balayage($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            default:
                echo("La méthode de résolution n'est pas encore fonctionnelle.\n");
                break;
        }
        if ($tableau != null){
            afficher_tableau($tableau);
            enregistrer_tableau($tableau);
        }
    } catch (ValueError $th) {
        echo("Erreur : $th. Veuillez réessayer.");// Gestion d'erreur si la saisie est incorrecte
    }
    return $racine;
}

function afficher_tableau($choix, $tableau){

    // Affiche le tableau des itérations en fonction de la méthode choisie.
 
   switch ($choix) {
    case 1:
        afficher_tableau_dichotomie($tableau);
        break;
    case 2:
        afficher_tableau_dichotomie($tableau);
        break;
    case 3:
        afficher_tableau_dichotomie($tableau);
        break;
    case 4:
        afficher_tableau_dichotomie($tableau);
        break;                        
    default:
        echo("La méthode de résolution n'est pas encore fonctionnelle.\n");
        break;
   }
}

//Fonction pour afficher la racine trouvée
function afficher_racine($racine){
    // Affiche la racine trouvée
    if($racine != null){
        echo("La racine trouvée est : $racine\n");
    }else{
        echo("Aucune racine trouvée.\n");
    }
}

// Fonction pour demander à l'utilisateur s'il souhaite recommencer
function demander_recommencer(){
    //Demande à l'utilisateur s'il souhaite recommencer ou quitter.
    return input("Souhaitez-vous recommencer ? (oui/non) : ").lower() == "oui";  // Vérifier la réponse de l'utilisateur
}

//Fonction pour afficher le nom de la méthode choisie
function print_method_name($choix){
    // Dictionnaire associant chaque méthode à son nom
    $methods = [
        1 => "METHODE DE DICHOTOMIE",
        2 =>  "METHODE DE LA SECANTE",
        3 =>  "METHODE DE NEWTON-RAPHSON",
        4 => "METHODE DU POINT FIXE",
        5 =>  "METHODE DE BALAYAGE"
    ];
    //Affichage du nom de la méthode choisie
    echo("***************{$methods[$choix]}***************\n");
}


//



