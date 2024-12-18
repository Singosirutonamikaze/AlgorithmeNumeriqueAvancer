import time
import matplotlib.pyplot as plt

# Fonction Fibonacci récursive simple
def fibonacci_recursif(n):
    if n <= 1:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

# Fonction Fibonacci avec mémoïsation
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Comparer les temps d'exécution pour différentes valeurs de n
n_values = range(1, 36)  # Limiter à 35 pour éviter des temps excessifs pour la version récursive
times_recursif = []
times_memo = []

for n in n_values:
    # Temps pour la fonction récursive simple
    start = time.time()
    fibonacci_recursif(n)  # Calcul sans affichage
    end = time.time()
    times_recursif.append(end - start)
    
    # Temps pour la fonction avec mémoïsation
    start = time.time()
    fibonacci_memo(n)  # Calcul sans affichage
    end = time.time()
    times_memo.append(end - start)

# Tracer les courbes
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_recursif, label="Récursif simple", color="red")
plt.plot(n_values, times_memo, label="Avec mémoïsation", color="blue")
plt.xlabel("n")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Comparaison des temps d'exécution : Récursif vs Mémoïsation")
plt.legend()
plt.grid()
plt.show()
