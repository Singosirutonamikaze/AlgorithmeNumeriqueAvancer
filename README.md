# AlgorithmeNumeriqueAvancer

# Recherche de Racines - Méthodes Numériques

Ce projet implémente plusieurs méthodes numériques pour résoudre des équations en trouvant les racines de fonctions. Les méthodes incluent :

- La **Méthode de Dichotomie** (ou Bisection)
- La **Méthode de la Sécante**
- La **Méthode de Newton-Raphson**
- La **Méthode du Point Fixe**
- La **Méthode de Balayage**

## Table des Matières

- [Introduction](#introduction)
- [Méthodes Implémentées](#méthodes-implémentées)
  - [Méthode de Dichotomie](#méthode-de-dichotomie)
  - [Méthode de la Sécante](#méthode-de-la-sécante)
  - [Méthode de Newton-Raphson](#méthode-de-newton-raphson)
  - [Méthode du Point Fixe](#méthode-du-point-fixe)
  - [Méthode de Balayage](#méthode-de-balayage)
- [Exemples d'Utilisation](#exemples-dutilisation)
- [Contributions](#contributions)
- [Licence](#licence)

## Introduction

Ce projet propose un ensemble de méthodes pour trouver des racines d'une fonction réelle. Il est conçu pour résoudre des équations de la forme \( f(x) = 0 \) où \( f(x) \) est une fonction continue, en utilisant différentes techniques d'approximation. Ces méthodes peuvent être appliquées à des fonctions complexes et fournissent des approximations de la racine avec un certain niveau de précision.

## Méthodes Implémentées

### Méthode de Dichotomie

La **méthode de dichotomie** (ou bisection) consiste à diviser un intervalle en deux et à sélectionner la sous-partie de l'intervalle où la fonction change de signe. Cette méthode est garantie de converger si la fonction est continue et si les bornes de l'intervalle ont des valeurs de signe opposé.

**Entrées** :

- `fonction`: La fonction à laquelle on cherche une racine.
- `borne_inferieure`: La borne inférieure de l'intervalle.
- `borne_superieure`: La borne supérieure de l'intervalle.
- `tolerance`: La tolérance acceptée pour l'erreur.
- `nombre_max_iterations`: Le nombre maximal d'itérations.

**Retour** :

- La racine approximée si trouvée, ou un message d'erreur si les bornes ne sont pas adéquates.

### Méthode de la Sécante

La **méthode de la sécante** est une approche itérative qui utilise deux points pour estimer la racine. Chaque itération est basée sur la ligne sécante passant par ces deux points. Contrairement à la méthode de Newton-Raphson, elle n'a pas besoin de calculer la dérivée de la fonction.

**Entrées** :

- `fonction`: La fonction à laquelle on cherche une racine.
- `borne_inferieure`: La borne inférieure de l'intervalle.
- `borne_superieure`: La borne supérieure de l'intervalle.
- `tolerance`: La tolérance acceptée pour l'erreur.
- `nombre_max_iterations`: Le nombre maximal d'itérations.

**Retour** :

- La racine approximée si trouvée, ou `None` si aucune racine n'a été trouvée.

### Méthode de Newton-Raphson

La **méthode de Newton-Raphson** est une méthode itérative qui utilise la dérivée de la fonction pour affiner l'estimation de la racine. Elle est très rapide si une bonne estimation initiale est donnée, mais peut échouer si la dérivée est proche de zéro.

**Entrées** :

- `fonction`: La fonction à laquelle on cherche une racine.
- `derivee_fonction`: La dérivée de la fonction.
- `x_initiale`: L'estimation initiale de la racine.
- `tolerance`: La tolérance acceptée pour l'erreur.
- `nombre_max_iterations`: Le nombre maximal d'itérations.

**Retour** :

- La racine approximée si trouvée, ou `None` si la méthode échoue.

### Méthode du Point Fixe

La **méthode du point fixe** repose sur la transformation de l'équation \( f(x) = 0 \) en une forme \( x = \phi(x) \). Elle itère en utilisant \( x = \phi(x) \) jusqu'à ce que la différence entre \( x \) et \( \phi(x) \) soit inférieure à une tolérance spécifiée.

**Entrées** :

- `phi`: La fonction de transformation.
- `x_initiale`: L'estimation initiale de la racine.
- `tolerance`: La tolérance acceptée pour l'erreur.
- `nombre_max_iterations`: Le nombre maximal d'itérations.

**Retour** :

- La racine approximée si trouvée, ou `None` si aucune solution n'a été trouvée.

### Méthode de Balayage

La **méthode de balayage** divise l'intervalle en sous-intervalles, puis applique la méthode de dichotomie sur chaque sous-intervalle où la fonction change de signe. Cela permet de localiser une racine avant de la raffiner avec une autre méthode.

**Entrées** :

- `fonction`: La fonction à laquelle on cherche une racine.
- `borne_inferieure`: La borne inférieure de l'intervalle.
- `borne_superieure`: La borne supérieure de l'intervalle.
- `pas`: Le pas de balayage entre les sous-intervalles.
- `tolerance`: La tolérance acceptée pour l'erreur.

**Retour** :

- La racine approximée si trouvée, ou un message indiquant qu'aucune racine n'a été trouvée.

## Exemples d'Utilisation

Voici un exemple d'utilisation de ces méthodes pour résoudre \( f(x) = x^2 - 4 \), c'est-à-dire trouver les racines de l'équation \( x^2 = 4 \).

```python
import math

# Définition de la fonction à résoudre
def ma_fonction(x):
    return x**2 - 4

# Exemple d'appel de la méthode de Dichotomie
resultat = methode_de_dichotomie(ma_fonction, 0, 3, 1e-6, 100)
print(f"Racine trouvée par Dichotomie : {resultat}")

# Exemple d'appel de la méthode de la Sécante
resultat = methode_de_la_secante(ma_fonction, 0, 3, 1e-6, 100)
print(f"Racine trouvée par Sécante : {resultat}")

# Exemple d'appel de la méthode de Newton-Raphson
def derivee_ma_fonction(x):
    return 2*x

resultat = methode_de_newton_raphson(ma_fonction, derivee_ma_fonction, 1.0, 1e-6, 100)
print(f"Racine trouvée par Newton-Raphson : {resultat}")
```

## Contributions

Les contributions sont les bienvenues! Si vous avez des améliorations ou des suggestions pour ce projet, n'hésitez pas à les proposer en ouvrant une **pull request**.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

# Résolution de systèmes linéaires par factorisation LU avec pivot

## Introduction

Ce module Python implémente la factorisation LU avec pivot partiel pour résoudre des systèmes d'équations linéaires de la forme `AX = B`. Il fournit également des fonctions pour résoudre des systèmes triangulaires inférieurs et supérieurs.

## Installation

Pour utiliser ce module, assurez-vous d'avoir installé NumPy :

```bash
pip install numpy
```

## Utilisation

```python
import numpy as np
from lu_solver import resoudre_systeme_avec_lu, saisir_matrice_et_vecteur

# Saisie de la matrice A et du vecteur B
A, B = saisir_matrice_et_vecteur()

# Résolution du système
solution = resoudre_systeme_avec_lu(A, B)

# Affichage de la solution
print("Solution du système AX = B :")
print(solution)
```

## Fonctionnalités

* **Factorisation LU avec pivot partiel:** Décompose une matrice carrée en un produit de matrices triangulaires inférieure et supérieure, en utilisant un pivot partiel pour améliorer la stabilité numérique.
* **Résolution de systèmes triangulaires:** Résout efficacement des systèmes linéaires avec des matrices triangulaires inférieures ou supérieures.
* **Résolution de systèmes généraux:** Combine la factorisation LU et la résolution de systèmes triangulaires pour résoudre des systèmes linéaires généraux.
* **Interface utilisateur:** Permet à l'utilisateur de saisir la matrice et le vecteur de manière interactive.
* **Gestion des erreurs:** Vérifie la validité des entrées et lève des exceptions en cas d'erreur (matrice singulière, dimensions incompatibles).

## Structure du code

Le code est organisé en plusieurs fonctions :

* `factorisation_lu_avec_pivot`: Effectue la factorisation LU avec pivot.
* `resoudre_triangulaire_inferieure`: Résout un système triangulaire inférieur.
* `resoudre_triangulaire_superieure`: Résout un système triangulaire supérieur.
* `resoudre_systeme_avec_lu`: Résout un système linéaire général en utilisant la factorisation LU.
* `saisir_matrice_et_vecteur`: Permet à l'utilisateur de saisir la matrice et le vecteur.

## Améliorations futures

* **Tests unitaires:** Implémentation de tests unitaires pour vérifier la correction du code.
* **Optimisations:** Recherche d'optimisations possibles pour améliorer les performances.
* **Documentation:** Élargissement de la documentation pour couvrir tous les aspects du code.
* **Généralisations:** Extension à des matrices rectangulaires ou à d'autres types de factorisations (Cholesky, QR).

## Contributions

Les contributions à ce projet sont les bienvenues. N'hésitez pas à créer des issues ou à soumettre des pull requests.

**Note:** 
* **Tests unitaires:** Il est fortement recommandé d'ajouter des tests unitaires pour vérifier le bon fonctionnement de chaque fonction.
* **Optimisations:** Vous pouvez explorer des optimisations telles que l'utilisation de fonctions vectorisées de NumPy ou l'algorithme de résolution de systèmes triangulaires de Crout.
* **Documentation:** Une documentation claire et détaillée est essentielle pour faciliter l'utilisation et la maintenance du code.

En suivant ces recommandations, vous pouvez améliorer encore davantage ce module de résolution de systèmes linéaires.

