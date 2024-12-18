def fibonacci_recursif(n):
    if n <= 1:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

# Exemple d'appel
n = 10
print(f"Fibonacci récursif pour n={n} : {fibonacci_recursif(n)}")
