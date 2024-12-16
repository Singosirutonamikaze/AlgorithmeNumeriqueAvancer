import numpy as np
import time
import matplotlib.pyplot as plt

#Multiplicationdirectedematrices
def naive_matrix_multiplication(A,B):
 return np.dot(A,B)

#AlgorithmedeStrassenpourlamultiplicationdematrices
def strassen_matrix_multiply(A,B):
    if len(A)==1:
        return A*B
    else:
        mid=len(A)//2
        A11=A[:mid,:mid]
        A12=A[:mid,mid:]
        A21=A[mid:,:mid]
        A22=A[mid:,mid:]
        B11=B[:mid,:mid]
        B12=B[:mid,mid:]
        B21=B[mid:,:mid]
        B22=B[mid:,mid:]

        M1=strassen_matrix_multiply(A11+A22,B11+B22)
        M2=strassen_matrix_multiply(A21+A22,B11)
        M3=strassen_matrix_multiply(A11,B12-B22)
        M4=strassen_matrix_multiply(A22,B21-B11)
        M5=strassen_matrix_multiply(A11+A12,B22)
        M6=strassen_matrix_multiply(A21-A11,B11+B12)
        M7=strassen_matrix_multiply(A12-A22,B21+B22)

        C11=M1+M4-M5+M7
        C12=M3+M5
        C21=M2+M4
        C22=M1-M2+M3+M6

        C = np.empty((len(A),len(B)))
        C[:mid,:mid]=C11
        C[:mid,mid:]=C12
        C[mid:,:mid]=C21
        C[mid:,mid:]=C22
    return C

#Fonctionpourévaluerletempsd'exécutiondelamultiplicationdematrices
def measure_execution_time(mult_func,A,B):
    start_time=time.time()
    result=mult_func(A,B)
    execution_time=time.time()-start_time
    return execution_time,result

#Fonctionprincipalepourcomparerlesalgorithmesdemultiplicationdematrices
def compare_matrix_multiplication(max_size,step):
    sizes=list(range(step,max_size+1,step))
    naive_times=[]
    strassen_times=[]

    for size in sizes:
        A=np.random.rand(size,size)
        B=np.random.rand(size,size)

    #Mesurerletempspourmultiplicationnaïve
    naive_time,_= measure_execution_time(naive_matrix_multiplication,A,B)
    naive_times.append(naive_time)

    #MesurerletempspourStrassen
    strassen_time,_= measure_execution_time(strassen_matrix_multiply,A,B)
    strassen_times.append(strassen_time)

    return sizes,naive_times,strassen_times

#Tracerlesrésultats
def plot_results(sizes,naive_times,strassen_times):
    plt.figure(figsize=(12,6))
    plt.plot(sizes,naive_times,label='MultiplicationNaïve',marker='o')
    plt.plot(sizes,strassen_times,label='MultiplicationdeStrassen',marker='x')
    plt.xlabel('TailledesMatrices(nxn)')
    plt.ylabel('Tempsd\'exécution(secondes)')
    plt.title('ComparaisondesAlgorithmesdeMultiplicationdeMatrices')
    plt.legend()
    plt.grid()
    plt.show()

#Main
if __name__=="__main__":
    max_matrix_size=512#Taillemaximaledesmatrices
    step_size=32#Incrémentede32àchaqueétape
    sizes,naive_times,strassen_times=compare_matrix_multiplication(max_matrix_size,step_size)
    plot_results(sizes,naive_times,strassen_times)