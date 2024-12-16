import random
import time
import matplotlib.pyplot as plt
import numpy as np

#AlgorithmedeBellman-Ford
def bellman_ford(graph,start):
    #Initialisationdesdistances
    distances={vertex:float('infinity')for vertex in graph}
    distances[start]=0

    #Relaxationdesarêtes
    for _ in range(len(graph)-1):
        for u in graph:
            for v,weight in graph[u]:
                if distances[u]+weight<distances[v]:
                    distances[v]=distances[u]+weight

    return distances

#AlgorithmedeDijkstra
def dijkstra(graph,start):
    #Initialisationdesdistances
    distances={vertex:float('infinity')for vertex in graph}
    distances[start]=0
    unvisited=list(graph.keys())

    while unvisited:
        #Choisirlesommetavecladistanceminimale
        current_vertex=min(unvisited,key=lambda vertex:distances[vertex])
        unvisited.remove(current_vertex)

        for neighbor,weight in graph[current_vertex]:
            distance=distances[current_vertex]+weight
            if distance<distances[neighbor]:
             distances[neighbor]=distance

    return distances

#Fonctionpourgénérerungraphealéatoire
def generate_random_graph(num_vertices,edge_probability):
    graph = {i:[]for i in range(num_vertices)}
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u!=v and random.random()<edge_probability:
                weight=random.randint(1,10)#Poidsaléatoires
                graph[u].append((v,weight))
    return graph

#Fonctionpourcomparerlesalgorithmes
def compare_algorithms(num_vertices,edge_probability):
    graph=generate_random_graph(num_vertices,edge_probability)

    #MesurerletempsdeBellman-Ford
    start_time=time.time()
    bellman_ford(graph,0)
    bellman_ford_time=time.time()-start_time

    #MesurerletempsdeDijkstra
    start_time=time.time()
    dijkstra(graph,0)
    dijkstra_time=time.time()-start_time

    return bellman_ford_time,dijkstra_time

#Variablespourstockerlestempsdechaquealgorithme
num_vertices_list=range(5,100,5)#De5à100sommets
bellman_times=[]
dijkstra_times=[]

#Exécutiondestestsdeperformance
for num_vertices in num_vertices_list:
    bf_time,d_time=compare_algorithms(num_vertices,0.3)
    bellman_times.append(bf_time)
    dijkstra_times.append(d_time)

#Tracédesrésultats
plt.figure(figsize=(10,6))
plt.plot(num_vertices_list,bellman_times,label='Bellman-Ford',marker='o')
plt.plot(num_vertices_list,dijkstra_times,label='Dijkstra',marker='x')
plt.xlabel('NombredeSommets')
plt.ylabel('Tempsd\'exécution(secondes)')
plt.title('ComparaisondesalgorithmesBellman-FordetDijkstra')
plt.legend()
plt.grid()
plt.show()
