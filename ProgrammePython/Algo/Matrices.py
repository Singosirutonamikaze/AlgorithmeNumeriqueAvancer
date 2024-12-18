import numpy as np
import time
import matplotlib.pyplot as plt

# Fonction pour ajuster les matrices à la taille la plus proche d'une puissance de 2
def pad_matrix(matrix, new_size):
    padded_matrix = np.zeros((new_size, new_size))
    original_size = matrix.shape[0]
    padded_matrix[:original_size, :original_size] = matrix
    return padded_matrix

# Algorithme de Strassen pour la multiplication de matrices
def strassen_matrix_multiply(A, B):
    n = len(A)
    if n == 1:
        return A * B
    else:
        mid = n // 2
        A11 = A[:mid, :mid]
        A12 = A[:mid, mid:]
        A21 = A[mid:, :mid]
        A22 = A[mid:, mid:]
        B11 = B[:mid, :mid]
        B12 = B[:mid, mid:]
        B21 = B[mid:, :mid]
        B22 = B[mid:, mid:]

        M1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
        M2 = strassen_matrix_multiply(A21 + A22, B11)
        M3 = strassen_matrix_multiply(A11, B12 - B22)
        M4 = strassen_matrix_multiply(A22, B21 - B11)
        M5 = strassen_matrix_multiply(A11 + A12, B22)
        M6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
        M7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        # Combiner les sous-matrices en une seule matrice
        C = np.zeros((n, n))
        C[:mid, :mid] = C11
        C[:mid, mid:] = C12
        C[mid:, :mid] = C21
        C[mid:, mid:] = C22
        return C

# Fonction pour ajuster la taille des matrices et appliquer Strassen
def strassen_wrapper(A, B):
    n = A.shape[0]
    m = 1 << (n - 1).bit_length()  # Trouver la puissance de 2 la plus proche
    A_padded = pad_matrix(A, m)
    B_padded = pad_matrix(B, m)
    C_padded = strassen_matrix_multiply(A_padded, B_padded)
    return C_padded[:n, :n]  # Retourner la matrice de taille originale

# Multiplication directe de matrices
def naive_matrix_multiplication(A, B):
    return np.dot(A, B)

# Fonction pour évaluer le temps d'exécution de la multiplication de matrices
def measure_execution_time(mult_func, A, B):
    start_time = time.time()
    result = mult_func(A, B)
    execution_time = time.time() - start_time
    return execution_time, result

# Fonction principale pour comparer les algorithmes de multiplication de matrices
def compare_matrix_multiplication(max_size, step):
    sizes = list(range(step, max_size + 1, step))
    naive_times = []
    strassen_times = []

    for size in sizes:
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)

        # Mesurer le temps pour multiplication naïve
        naive_time, _ = measure_execution_time(naive_matrix_multiplication, A, B)
        naive_times.append(naive_time)

        # Mesurer le temps pour Strassen
        strassen_time, _ = measure_execution_time(strassen_wrapper, A, B)
        strassen_times.append(strassen_time)

    return sizes, naive_times, strassen_times

# Tracer les résultats
def plot_results(sizes, naive_times, strassen_times):
    plt.figure(figsize=(12, 6))
    plt.plot(sizes, naive_times, label='Multiplication Naïve', marker='o')
    plt.plot(sizes, strassen_times, label='Multiplication de Strassen', marker='x')
    plt.xlabel('Taille des Matrices (n x n)')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison des Algorithmes de Multiplication de Matrices')
    plt.legend()
    plt.grid()
    plt.show()

# Main
if __name__ == "__main__":
    max_matrix_size = 256  # Taille maximale des matrices
    step_size = 16  # Incrémente de 32 à chaque étape
    sizes, naive_times, strassen_times = compare_matrix_multiplication(max_matrix_size, step_size)
    plot_results(sizes, naive_times, strassen_times)
