
# Fonction pour afficher le tableau des intervalles de balayage
def afficher_tableau_balayage(tableau_intervals):
    # Affiche le tableau des intervalles de balayage.
    # Chaque ligne correspond à un intervalle exploré et affiche les informations associées.
    print("\nTableau des intervalles de balayage :")
    print("{:<20} {:<18} {:<18} {:<18} {:<18}".format('Intervalle', 'Borne Inf.', 'Borne Sup.', 'f(Borne Inf.)', 'f(Borne Sup.)'))
    print("-" * 90)

    for interval_data in tableau_intervals:
        print("{:<20} {:<18} {:<18} {:<18} {:<18}".format(
            interval_data['intervalle'],
            interval_data['borne_inferieure'],
            interval_data['borne_superieure'],
            interval_data['f(borne_inferieure)'],
            interval_data['f(borne_superieure)']
        ))


# Fonction pour afficher le tableau stylisé
def afficher_tableau_dichotomie(tableau):
    # Affichage de l'entête du tableau avec des bornes d'étoiles
    print("*" * 100)
    print(f"{'Iteration':<12}|{'Borne Inférieure':<20}|{'Borne Supérieure':<20}|{'f(Borne Inférieure)':<25}|{'f(Borne Supérieure)':<25}|{'f(borne inferieure) * f(borne superieure)':<25}")
    print("*" * 100)

    # Affichage des informations ligne par ligne
    for ligne in tableau:
        print(f"{ligne['iteration']:<12}{ligne['borne_inferieure']:<20}{ligne['borne_superieure']:<20}{ligne['signe_f(borne_inferieure)']:<25}{ligne['signe_f(borne_superieure)']:<25}{ligne['signe_(f(borne_inferieure)*f(borne_superieure))']:<25}")
    
    # Ligne de fermeture avec des étoiles
    print("*" * 100)


def afficher_tableau_secante(tableau_interactions):
    # Affiche le tableau des itérations de manière lisible.
    # Chaque ligne correspond à une itération et affiche les informations associées.

    print("\nTableau des itérations :")
    
    # Définition des en-têtes de colonnes
    en_tetes = ['Iteration', 'Borne Inf.', 'Borne Sup.', 'Estimation', 'f(Estimation)', 'Diff. Bornes']
    
    # Format de l'en-tête pour l'affichage
    print("{:<12} {:<18} {:<18} {:<18} {:<18} {:<18}".format(*en_tetes))
    
    # Ligne de séparation
    print("-" * 90)

    # Parcours des données dans le tableau des itérations
    for iteration_data in tableau_interactions:
        iteration_num = iteration_data['iteration']
        borne_inferieure = iteration_data['borne_inferieure']
        borne_superieure = iteration_data['borne_superieure']
        estimation = iteration_data['estimation']
        f_estimation = iteration_data['f(estimation)']
        diff_bornes = iteration_data['différence_bornes']
        
        # Formatage et affichage des données de l'itération
        print("{:<12} {:<18} {:<18} {:<18} {:<18} {:<18}".format(
            iteration_num,
            borne_inferieure,
            borne_superieure,
            estimation,
            f_estimation,
            diff_bornes
        ))


# Fonction pour afficher le tableau du point fixe
def afficher_tableau_point_fixe(tableau_interactions):
    """
    Affiche le tableau des itérations de manière lisible.
    Chaque ligne correspond à une itération et affiche les informations associées.
    """
    print("\nTableau des itérations :")
    print("{:<12} {:<18} {:<18} {:<18}".format('Iteration', 'x', 'phi(x)', 'Différence'))
    print("-" * 70)

    for iteration_data in tableau_interactions:
        iteration_num = iteration_data['iteration']
        x = iteration_data['x']
        phi_x = iteration_data['phi(x)']
        difference = iteration_data['différence']
        
        # Affichage des données de l'itération
        print("{:<12} {:<18} {:<18} {:<18}".format(
            iteration_num,
            x,
            phi_x,
            difference
        ))

    
