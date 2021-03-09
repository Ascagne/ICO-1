# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:18:36 2021

@author: Julien
"""

from evolution_functions import next_gen, init_pop
from constants import nb_generations, nb_pop, n_trucks, truck_capacity, mutation_rate
from evaluation_functions import circuit_camion
from classes import liste

import matplotlib.pyplot as plt

###############################################################################
#######################   génération de la population  ########################
###############################################################################
population=init_pop(nb_pop)

X=[1]
Y=[population[0][1]]

for i in range(2,nb_generations+1):
    population = next_gen(population)
    X.append(i)
    Y.append(population[0][1])
plt.plot(X,Y)
plt.xlabel('génération')
plt.ylabel("Score")
plt.title("Score : "+str(population[0][1])+" | "+str(n_trucks)+" camions d'une capacité de " + str(truck_capacity)+"\nTaux de mutation : "+str(mutation_rate)+" | Taile de la population : "+str(nb_pop) )    
#    if i%100 == 0: 
#        print(population[0][1])
    
plt.savefig(str(population[0][1])+'_distance.png', format='png')    





liste_clients = liste()

circuit=circuit_camion(population[0])

 #on genere une carte représentant notre solution
y = [0]
z = [0]
infos = ["Entrepot"]
for i in range(1,len(liste_clients)):

    X.append(liste_clients[i][1])
    Y.append(liste_clients[i][2])
    txt = "Client n°"+str(liste_clients[i][0])+"\n"+str(liste_clients[i][3])+" - ["+str(liste_clients[i][4])+", "+str(liste_clients[i][5])+"]"
    infos.append(txt)


n = infos

X=[]
Y=[]

plt.figure(figsize=(20,20))
plt.grid()
for i in range(n_trucks):
    X2=[]
    Y2=[]
    for j in circuit[i]:
        X2.append(liste_clients[j][1])
        Y2.append(liste_clients[j][2])
        
    X.append(X2)
    Y.append(Y2)
    plt.plot(X2,Y2)
    
    

for i, txt in enumerate(n):
    print(txt)
    print(i)
    plt.annotate(txt, (liste_clients[i][1], liste_clients[i][2]))
plt.title("Score : "+str(population[0][1])+" | "+str(n_trucks)+" camions d'une capacité de " + str(truck_capacity) )

plt.savefig(str(population[0][1])+'_chemin.png', format='png') 



