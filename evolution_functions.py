# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:34:59 2021

@author: Julien
"""


###############################################################################
##########################   fonctions d'évolution   ##########################
###############################################################################

from constants import elitism, clients, n_trucks, mutation_rate, nb_pop, best_pop
import random as rd
from evaluation_functions import population_evaluation, tri_fusion

rand=rd.random

Phenon=[i for i in range(len(clients))] +[-i for i in range(1,n_trucks)]
#Phenon = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, -1, -2, -3]
back_to_depot=[-i for i in range(n_trucks)]

nv=len(Phenon)

def generate():
    a=Phenon[1:]
    rd.shuffle(a)
    return [0]+a

#def taille_pop2():
#    pop = []
#    for i in range(taille_pop):
#        circuit2=generate()
#        distance=0
#        for j in range(1,nv):
#            distance+=dist[circuit2[j-1],circuit2[j]]
#        pop.append([circuit2,distance])
#    return pop
        
    

def crossover(parent1,parent2):
    """
    Utilisation d'un two points crossover
    Les points de départ et de fin sont choisis aléatoirement
    """
    
    parent1 = parent1[1:]
    parent2 = parent2[1:]
    nv=len(parent1)
    # On récupère une partie des critères du premier parent
    start_point=rd.randint(0,nv-1)
    end_point=rd.randint(0,nv-1)
    
    if start_point > end_point :
        start_point,end_point=end_point,start_point
    
    child=["False" for i in range(nv)]
    heritage_parent1=parent1[start_point:end_point+1]
    child[start_point:end_point+1]=heritage_parent1
    
    
    # On récupère ensuite le maximum de critères possibles du parent2 tout en conservant un enfant sans doublons
    m1=[]
    for i in range(nv):
        if i > end_point or i < start_point: 
            criteria=parent2[i]
            if criteria not in heritage_parent1:
                child[i]=criteria
            else:
                m1.append(i)
                
                
    # On complète par les critères manquants            
    m2=[]
#    print(enfant)
    for i in Phenon[1:]:

        
        if i not in child:
            m2.append(i)

    rd.shuffle(m2)
#    print(patrimoine_parent1)
#    print(parent2)
#    print(m2)
#    print(m1)
#    print(enfant)
    for i in range(len(m1)):
        child[m1[i]]=m2[i]
    
    #mutation
    if rd.random() < mutation_rate:
        a=rd.randint(0,len(child)-1)
        b=rd.randint(0,len(child)-1)   
        child[a], child[b] = child[b], child[a]
            
    return [0]+child 


def init_pop(n):
    pop=[]
    for i in range(n):
        track=generate()
        pop.append(population_evaluation([track,0]))
    pop=tri_fusion(pop)
    return pop



def next_gen(population):
  
    new_gen=[]
    
    if elitism == True:
        elite=population[:best_pop]
    else:
        elite=[]
        

    nb_child=(nb_pop//2)
    
    couples=[i for i in range(nb_child*2)]

    rd.shuffle(couples)
    

    for i in range(nb_child//2):
        
        

        child=crossover(population[couples[i]][0],population[couples[nb_pop//2+i]][0])
        
        new_gen.append(population_evaluation([child,0]))
    
    new_gen=new_gen+elite
    
    new_gen= new_gen + init_pop(nb_pop-len(new_gen))
    
    population=tri_fusion(new_gen[:])
    
    return(population)
    
    
