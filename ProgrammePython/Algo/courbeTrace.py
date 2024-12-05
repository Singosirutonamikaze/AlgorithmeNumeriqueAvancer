import matplotlib.pyplot as plt

# Données pour le premier tableau (Taille, nombre de comparaison)
tableau_1 = [
    (1000, 240726), (1500, 572650), (2000, 1005089), (2500, 1513541), 
    (3000, 2263050), (3500, 3037778), (4000, 3961292), (4500, 5108644), 
    (5000, 6372257), (5500, 7534139), (6000, 9082810), (6500, 10440419), 
    (7000, 12297672), (7500, 13835980), (8000, 16073822), (8500, 18253987), 
    (9000, 20401659), (9500, 22435761)
]

# Données pour le deuxième tableau (Taille, Temps en secondes)
tableau_2 = [
    (1000, 86.7452621459961), (1500, 163.9113426208496), (2000, 248.46458435058594), 
    (2500, 510.6935501098633), (3000, 581.97021484375), (3500, 661.5417003631592), 
    (4000, 787.5440120697021), (4500, 938.0621910095215), (5000, 1057.82151222229), 
    (5500, 1244.6846961975098), (6000, 1537.9142761230469), (6500, 2846.0657596588135), 
    (7000, 5340.20471572876), (7500, 8668.147563934326), (8000, 5253.371000289917), 
    (8500, 4047.515392303467), (9000, 6661.331415176392), (9500, 6809.062480926514)
]

# Séparer les valeurs pour les graphiques
taille_1, temps_1 = zip(*tableau_1)
taille_2, temps_2 = zip(*tableau_2)

# Tracer les graphiques
plt.figure(figsize=(12, 6))

# Graphique 1 : Temps en millisecondes
plt.subplot(1, 2, 1)
plt.plot(taille_1, temps_1, marker='o', color='b', label='Comparaison')
plt.title("Taille vs comparaison")
plt.xlabel("Taille")
plt.ylabel("Comparaison")
plt.grid(True)
plt.legend()

# Graphique 2 : Tcount
plt.subplot(1, 2, 2)
plt.plot(taille_2, temps_2, marker='s', color='r', label='Temps(S)')
plt.title("Taille vs Temps(s) ")
plt.xlabel("Taille")
plt.ylabel("Temps")
plt.grid(True)
plt.legend()

# Affichage des graphiques
plt.tight_layout()
plt.show()
