#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "muParser.h"  // Inclure la bibliothèque muParser pour l'évaluation des expressions mathématiques

// Prototypes des fonctions
double evaluate_function(const char* expression, double x);
double methode_de_dichotomie(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerence, int nombre_max_iterations);
double methode_de_la_secante(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerence, int nombre_max_iterations);
double methode_de_newton(double (*fonction)(double), double (*derivee_fonction)(double), double x_initiale, double tolerence, int nombre_max_iterations);
double methode_du_point_fixe(double (*phi)(double), double x_initiale, double tolerence, int nombre_max_iterations);

// Fonction pour évaluer la fonction utilisateur avec muParser
double evaluate_function(const char* expression, double x) {
    mu::Parser p;  // Création d'un objet muParser
    p.DefineVar("x", &x);  // Définition de la variable x
    p.SetExpr(expression);  // Définition de l'expression à évaluer
    return p.Eval();  // Évaluation et retour de la valeur
}

// Méthode de dichotomie
double methode_de_dichotomie(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerence, int nombre_max_iterations) {
    double valeur_borne_inferieure;  // Valeur de la fonction à la borne inférieure
    double valeur_borne_superieure;   // Valeur de la fonction à la borne supérieure
    double point_milieu;              // Point milieu de l'intervalle

    // Évaluation des bornes
    valeur_borne_inferieure = fonction(borne_inferieure);
    valeur_borne_superieure = fonction(borne_superieure);

    // Vérification si la racine est à la borne inférieure
    if (fabs(valeur_borne_inferieure) <= tolerence) {
        return borne_inferieure;
    }
    // Vérification si la racine est à la borne supérieure
    if (fabs(valeur_borne_superieure) <= tolerence) {
        return borne_superieure;
    }
    // Vérification que la racine est encadrée
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0) {
        printf("La racine n'est pas encadrée entre %lf et %lf\n", borne_inferieure, borne_superieure);
        exit(0);
    }

    // Itérations pour la méthode de dichotomie
    for (int i = 0; i < nombre_max_iterations; i++) {
        point_milieu = (borne_inferieure + borne_superieure) / 2.0;  // Calcul du point milieu
        double valeur_point_milieu = fonction(point_milieu);  // Évaluation de la fonction au point milieu

        // Vérification si le point milieu est la racine
        if (fabs(valeur_point_milieu) <= tolerence || (borne_superieure - borne_inferieure) < tolerence) {
            return point_milieu;
        }

        // Mise à jour des bornes en fonction du signe de la fonction
        if (valeur_point_milieu * valeur_borne_superieure < 0.0) {
            borne_inferieure = point_milieu;
            valeur_borne_inferieure = valeur_point_milieu;
        } else {
            borne_superieure = point_milieu;
            valeur_borne_superieure = valeur_point_milieu;
        }
    }
    return (borne_inferieure + borne_superieure) / 2.0;  // Retourne le milieu comme approximation
}

// Méthode de la sécante
double methode_de_la_secante(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerence, int nombre_max_iterations) {
    double valeur_borne_inferieure;  // Valeur de la fonction à la borne inférieure
    double valeur_borne_superieure;   // Valeur de la fonction à la borne supérieure
    double estimation;                 // Estimation de la racine

    // Évaluation des bornes
    valeur_borne_inferieure = fonction(borne_inferieure);
    valeur_borne_superieure = fonction(borne_superieure);

    // Vérification si la racine est à la borne inférieure
    if (fabs(valeur_borne_inferieure) <= tolerence) {
        return borne_inferieure;
    }
    // Vérification si la racine est à la borne supérieure
    if (fabs(valeur_borne_superieure) <= tolerence) {
        return borne_superieure;
    }
    // Vérification que la racine est encadrée
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0) {
        printf("La racine n'est pas encadrée entre %lf et %lf\n", borne_inferieure, borne_superieure);
        exit(0);
    }

    // Itérations pour la méthode de la sécante
    for (int compteur_iterations = 0; compteur_iterations < nombre_max_iterations; compteur_iterations++) {
        estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure);  // Estimation de la nouvelle valeur
        double valeur_estimation = fonction(estimation);  // Évaluation de la fonction à l'estimation

        // Vérification si l'estimation est la racine
        if (fabs(valeur_estimation) <= tolerence) {
            return estimation;
        }

        // Mise à jour des bornes
        if (valeur_estimation * valeur_borne_superieure < 0.0) {
            borne_inferieure = estimation;
            valeur_borne_inferieure = valeur_estimation;
        } else {
            borne_superieure = estimation;
            valeur_borne_superieure = valeur_estimation;
        }
    }
    return borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure);  // Retourne la dernière estimation
}

// Méthode de Newton
double methode_de_newton(double (*fonction)(double), double (*derivee_fonction)(double), double x_initiale, double tolerence, int nombre_max_iterations) {
    double x = x_initiale;  // Initialisation du point de départ

    // Itérations pour la méthode de Newton
    for (int compteur_iterations = 0; compteur_iterations < nombre_max_iterations; compteur_iterations++) {
        double valeur_x = fonction(x);  // Évaluation de la fonction au point x
        double valeur_derivee_x = derivee_fonction(x);  // Évaluation de la dérivée au point x

        // Vérification si la dérivée est nulle
        if (valeur_derivee_x == 0) {
            printf("Dérivée nulle. Méthode de Newton échoue.\n");
            return NAN;  // Retourne une valeur non valide
        }

        x = x - valeur_x / valeur_derivee_x;  // Mise à jour du point x
        // Vérification de la convergence
        if (fabs(valeur_x) <= tolerence) {
            return x;
        }
    }
    printf("Pas de convergence avec la méthode de Newton.\n");
    return NAN;  // Retourne une valeur non valide si pas de convergence
}

// Méthode du point fixe
double methode_du_point_fixe(double (*phi)(double), double x_initiale, double tolerence, int nombre_max_iterations) {
    double x = x_initiale;  // Initialisation du point de départ

    // Itérations pour la méthode du point fixe
    for (int compteur_iterations = 0; compteur_iterations < nombre_max_iterations; compteur_iterations++) {
        double x_suivant = phi(x);  // Calcul de la prochaine valeur
        // Vérification de la convergence
        if (fabs(x_suivant - x) <= tolerence) {
            return x_suivant;
        }
        x = x_suivant;  // Mise à jour de x pour la prochaine itération
    }
    printf("Pas de convergence avec la méthode du point fixe.\n");
    return NAN;  // Retourne une valeur non valide si pas de convergence
}

// Fonction principale
int main() {
    // Variables pour la saisie de l'utilisateur
    int choix;  // Choix de la méthode
    double borne_inferieure;  // Borne inférieure pour les méthodes nécessitant des bornes
    double borne_superieure;  // Borne supérieure pour les méthodes nécessitant des bornes
    double tolerence;  // Tolérance pour la convergence
    int nombre_max_iterations;  // Nombre maximal d'itérations
    char expression[100];  // Expression de la fonction à évaluer

    // Saisie de l'expression de la fonction
    printf("Entrez l'expression de la fonction (ex: sin(x), x*x - 4): ");
    scanf("%s", expression);  // Lecture de l'expression

    // Affichage du menu pour le choix de la méthode
    printf("Choisissez la méthode:\n");
    printf("1. Méthode de dichotomie\n");
    printf("2. Méthode de la sécante\n");
    printf("3. Méthode de Newton\n");
    printf("4. Méthode du point fixe\n");
    printf("Votre choix: ");
    scanf("%d", &choix);  // Lecture du choix de l'utilisateur

    // Demande de la tolérance et du nombre maximal d'itérations
    printf("Entrez la tolérance: ");
    scanf("%lf", &tolerence);  // Lecture de la tolérance
    printf("Entrez le nombre maximal d'itérations: ");
    scanf("%d", &nombre_max_iterations);  // Lecture du nombre d'itérations

    // Exécution en fonction du choix de l'utilisateur
    switch (choix) {
        case 1:  // Méthode de dichotomie
            printf("Entrez la borne inférieure: ");
            scanf("%lf", &borne_inferieure);  // Lecture de la borne inférieure
            printf("Entrez la borne supérieure: ");
            scanf("%lf", &borne_superieure);  // Lecture de la borne supérieure
            printf("Racine trouvée (dichotomie): %lf\n", methode_de_dichotomie(evaluate_function(expression), borne_inferieure, borne_superieure, tolerence, nombre_max_iterations));
            break;
        case 2:  // Méthode de la sécante
            printf("Entrez la borne inférieure: ");
            scanf("%lf", &borne_inferieure);  // Lecture de la borne inférieure
            printf("Entrez la borne supérieure: ");
            scanf("%lf", &borne_superieure);  // Lecture de la borne supérieure
            printf("Racine trouvée (sécante): %lf\n", methode_de_la_secante(evaluate_function(expression), borne_inferieure, borne_superieure, tolerence, nombre_max_iterations));
            break;
        case 3:  // Méthode de Newton
            printf("Entrez la valeur initiale x: ");
            double x_initiale;  // Valeur initiale pour Newton
            scanf("%lf", &x_initiale);  // Lecture de la valeur initiale
            // Définir la dérivée de la fonction (cette fonction doit être définie pour Newton)
            double derivee_fonction(double x) {
                // Exemple de dérivée, cela doit être modifié en fonction de l'expression de la fonction
                return 2 * x;  // Dérivée de x^2 - 4 est 2x
            }
            printf("Racine trouvée (Newton): %lf\n", methode_de_newton(evaluate_function(expression), derivee_fonction, x_initiale, tolerence, nombre_max_iterations));
            break;
        case 4:  // Méthode du point fixe
            printf("Entrez la valeur initiale x: ");
            double x_init;  // Valeur initiale pour le point fixe
            scanf("%lf", &x_init);  // Lecture de la valeur initiale
            // Définir la fonction phi(x) (doit être fournie pour le point fixe)
            double phi(double x) {
                // Exemple de transformation, cela doit être modifié en fonction de l'expression
                return sqrt(4 + x);  // Exemple d'équation
            }
            printf("Racine trouvée (point fixe): %lf\n", methode_du_point_fixe(phi, x_init, tolerence, nombre_max_iterations));
            break;
        default:
            printf("Choix invalide.\n");  // Gestion d'un choix invalide
    }

    return 0;  // Fin du programme
}
