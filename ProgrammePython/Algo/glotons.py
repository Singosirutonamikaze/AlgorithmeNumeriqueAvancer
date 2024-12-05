# -*- coding: utf-8 -*-
"""
Mise en oeuvre d'un algorithme glouton pour le sac à dos
"""
# Masse maximum pouvant être emportée dans le sac
masse_max_sac = 30
# Définition du système d'objets : liste de sous-listes
# Sous-liste : ["Nom_objet",valeur_objet,masse_objet,valeur_objet/masse_objet]
systeme_objets=[["Objet1",70,13,70/13],["Objet2",40,12,40/12],["Objet3",30,8,
30/8],["Objet4",30,10,30/10]]
# Tri du système d'objets par valeurs décroissantes de
# la masse de chaque objet
# Utilisation de key et d'une fonction lambda pour faire porter le tri sur le
# dernier élément de chaque sous-liste
systeme_objets.sort(key=lambda colonne:colonne[-1],reverse = True)
# Définition de la fonction gloutonne
def sac_a_dos(masse_max_sac, systeme_objets):
    '''Fonction gloutonne'''
    # Initialisation de la masse temporaire
    masse = 0
    # Initialisation de la liste d'objets à sélectionner
    liste_objets = []
    for i in range(len(systeme_objets)):
        if masse + systeme_objets[i][-2] <= masse_max_sac:
            masse = masse + systeme_objets[i][-2]
            liste_objets.append(systeme_objets[i])
    return liste_objets
print(sac_a_dos(30, systeme_objets))