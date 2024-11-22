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
double methode_de_dichotomie(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerence, int nombre_max_iterations) {
    double valeur_borne_inferieure;
    double valeur_borne_superieure;
    double point_milieu;

    valeur_borne_inferieure = fonction(borne_inferieure);
    valeur_borne_superieure = fonction(borne_superieure);

    if (fabs(valeur_borne_inferieure) <= tolerence) {
        return borne_inferieure;
    }
    if (fabs(valeur_borne_superieure) <= tolerence) {
        return borne_superieure;
    }
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0) {
        printf("La racine n'est pas encadrée entre %lf et %lf\n", borne_inferieure, borne_superieure);
        exit(0);
    }

    for (int i = 0; i < nombre_max_iterations; i++) {
        point_milieu = (borne_inferieure + borne_superieure) / 2.0;
        double valeur_point_milieu = fonction(point_milieu);

        if (fabs(valeur_point_milieu) <= tolerence || (borne_superieure - borne_inferieure) < tolerence) {
            return point_milieu;
        }

        if (valeur_point_milieu * valeur_borne_superieure < 0.0) {
            borne_inferieure = point_milieu;
            valeur_borne_inferieure = valeur_point_milieu;
        } else {
            borne_superieure = point_milieu;
            valeur_borne_superieure = valeur_point_milieu;
        }
    }
    return (borne_inferieure + borne_superieure) / 2.0;
}

double methode_de_la_secante(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerence, int nombre_max_iterations) {
    double valeur_borne_inferieure;
    double valeur_borne_superieure;
    double estimation;

    valeur_borne_inferieure = fonction(borne_inferieure);
    valeur_borne_superieure = fonction(borne_superieure);

    if (fabs(valeur_borne_inferieure) <= tolerence) {
        return borne_inferieure;
    }
    if (fabs(valeur_borne_superieure) <= tolerence) {
        return borne_superieure;
    }
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0) {
        printf("La racine n'est pas encadrée entre %lf et %lf\n", borne_inferieure, borne_superieure);
        exit(0);
    }

    for (int compteur_iterations = 0; compteur_iterations < nombre_max_iterations; compteur_iterations++) {
        estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure);
        double valeur_estimation = fonction(estimation);

        if (fabs(valeur_estimation) <= tolerence) {
            return estimation;
        }

        if (valeur_estimation * valeur_borne_superieure < 0.0) {
            borne_inferieure = estimation;
            valeur_borne_inferieure = valeur_estimation;
        } else {
            borne_superieure = estimation;
            valeur_borne_superieure = valeur_estimation;
        }
    }
    return borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure);
}

double methode_de_newton(double (*fonction)(double), double (*derivee_fonction)(double), double x_initiale, double tolerence, int nombre_max_iterations) {
    double x = x_initiale;

    for (int compteur_iterations = 0; compteur_iterations < nombre_max_iterations; compteur_iterations++) {
        double valeur_x = fonction(x);
        double valeur_derivee_x = derivee_fonction(x);

        if (valeur_derivee_x == 0) {
            printf("Dérivée nulle. Méthode de Newton échoue.\n");
            return NAN;
        }

        x = x - valeur_x / valeur_derivee_x;
        if (fabs(valeur_x) <= tolerence) {
            return x;
        }
    }
    printf("Pas de convergence avec la méthode de Newton.\n");
    return NAN;
}

double methode_du_point_fixe(double (*phi)(double), double x_initiale, double tolerence, int nombre_max_iterations) {
    double x = x_initiale;

    for (int compteur_iterations = 0; compteur_iterations < nombre_max_iterations; compteur_iterations++) {
        double x_suivant = phi(x);

        if (fabs(x_suivant - x) <= tolerence) {
            return x_suivant;
        }
        x = x_suivant;
    }
    printf("Pas de convergence avec la méthode du point fixe.\n");
    return NAN;
}

int main() {
    int choix;
    double borne_inferieure;
    double borne_superieure;
    double tolerence;
    int nombre_max_iterations;
    char expression[100];

    printf("Entrez l'expression de la fonction (ex: sin(x), x*x - 4): ");
    scanf("%s", expression);

    printf("Choisissez la méthode:\n");
    printf("1. Méthode de dichotomie\n");
    printf("2. Méthode de la sécante\n");
    printf("3. Méthode de Newton\n");
    printf("4. Méthode du point fixe\n");
    printf("Votre choix: ");
    scanf("%d", &choix);

    printf("Entrez la tolérance: ");
    scanf("%lf", &tolerence);
    printf("Entrez le nombre maximal d'itérations: ");
    scanf("%d", &nombre_max_iterations);

    switch (choix) {
        case 1:
            printf("Entrez la borne inférieure: ");
            scanf("%lf", &borne_inferieure);
            printf("Entrez la borne supérieure: ");
            scanf("%lf", &borne_superieure);
            printf("Racine trouvée (dichotomie): %lf\n", methode_de_dichotomie(evaluate_function(expression), borne_inferieure, borne_superieure, tolerence, nombre_max_iterations));
            break;
        case 2:
            printf("Entrez la borne inférieure: ");
            scanf("%lf", &borne_inferieure);
            printf("Entrez la borne supérieure: ");
            scanf("%lf", &borne_superieure);
            printf("Racine trouvée (sécante): %lf\n", methode_de_la_secante(evaluate_function(expression), borne_inferieure, borne_superieure, tolerence, nombre_max_iterations));
            break;
        case 3:
            printf("Entrez la valeur initiale x: ");
            double x_initiale;
            scanf("%lf", &x_initiale);
            double derivee_fonction(double x) {
                return 2 * x;
            }
            printf("Racine trouvée (Newton): %lf\n", methode_de_newton(evaluate_function(expression), derivee_fonction, x_initiale, tolerence, nombre_max_iterations));
            break;
        case 4:
            printf("Entrez la valeur initiale x: ");
            double x_init;
            scanf("%lf", &x_init);
            double phi(double x) {
                return sqrt(4 + x);
            }
            printf("Racine trouvée (point fixe): %lf\n", methode_du_point_fixe(phi, x_init, tolerence, nombre_max_iterations));
            break;
        default:
            printf("Choix invalide.\n");
    }

    return 0;
}
