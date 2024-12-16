def rendu_monnaie_mem(P, X):
    # Création du tableau de mémorisation
    mem = [float('inf')] * (X + 1)  # Initialisation avec une valeur infinie
    mem[0] = 0  # Il faut 0 pièces pour rendre 0
    return rendu_monnaie_mem_c(P, X, mem)

def rendu_monnaie_mem_c(P, X, m):
    if m[X] != float('inf'):  # Si la valeur est déjà calculée, on la renvoie
        return m[X]
    
    mini = float('inf')  # Initialisation avec une valeur infinie
    for i in range(len(P)):
        if P[i] <= X:
            nb = 1 + rendu_monnaie_mem_c(P, X - P[i], m)  # On ajoute une pièce à la solution
            if nb < mini:
                mini = nb
    
    m[X] = mini  # On mémorise la valeur calculée
    return mini

pieces = (2, 5, 10, 50, 100)
montant = 67  # Exemple de montant à rendre
resultat = rendu_monnaie_mem(pieces, montant)

if resultat == float('inf'):
    print(f"Il est impossible de rendre exactement {montant} avec les pièces disponibles.")
else:
    print(f"Le nombre minimal de pièces pour rendre {montant} est : {resultat}")
