
import time
import numpy as np
import matplotlib.pyplot as plt

#Fonctionpourrésoudreleproblèmedusacàdosaveclaprogrammationdynamique
def knapsack(weights,values,capacity):
    n=len(weights)
    #Créationd'untableaupourstockerlavaleurmaximaleàatteindre
    dp= np.zeros((n+1,capacity+1))

    #Remplissagedutableaudemanièreitérative
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(dp[i-1][w],dp[i-1][w-weights[i-1]]+values[i-1])
            else:
                dp[i][w]=dp[i-1][w]

    return dp[n][capacity]#Retournelavaleurmaximale

#Fonctionpourgénérerdespoidsetdesvaleursaléatoires
def generate_random_items(num_items,max_weight,max_value):
    weights=np.random.randint(1,max_weight+1,num_items)
    values=np.random.randint(1,max_value+1,num_items)
    return weights,values

#Fonctionpourmesurerletempsd'exécutiondel'algorithmedesacàdos
def measure_knapsack_performance(num_items,capacity):
    weights,values=generate_random_items(num_items,20,100)

    start_time = time.time()
    knapsack(weights,values,capacity)
    execution_time = time.time()-start_time

    return execution_time

#Variablespourstockerlestempsd'exécution
num_items_list=range(1,101,5)#De1à100objets
knapsack_times=[]

#Exécutiondestestsdeperformance
capacity=200#Définirunecapacitéfixepourtouteslesexécutions
for num_items in num_items_list:
    exec_time=measure_knapsack_performance(num_items,capacity)
    knapsack_times.append(exec_time)

#Tracédesrésultats
plt.figure(figsize=(10,6))
plt.plot(num_items_list,knapsack_times,label='SacàDos(DP)',marker='o')
plt.xlabel('Nombred\'Objets')
plt.ylabel('Tempsd\'exécution(secondes)')
plt.title('Performancedel\'algorithmedeSacàDosenprogrammationdynamique')
plt.legend()
plt.grid()
plt.show()

