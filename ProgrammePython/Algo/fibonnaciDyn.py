def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Exemple d'appel
n = 10
print(f"Fibonacci avec mémoïsation pour n={n} : {fibonacci_memo(n)}")
