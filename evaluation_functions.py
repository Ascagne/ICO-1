# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:22:06 2021

@author: Julien
"""

from constants import time_penalty, quantity_penalty, time_matrix, clients, truck_capacity

###############################################################################
##########################   fonctions d'évaluation  ##########################
###############################################################################


def track_evaluation(truck_track):
    t3=0
    trucks_time = []
    for track in truck_track:
        t=0
        q=truck_capacity
        for i in range(1,len(track)):
            
            # Evaluation fenêtre
            try :
                t2= time_matrix[track[i-1]][track[i]]
                if t+t2 <= clients[track[i]][2]: #Si arrivé du livreur avant la fin de la fenêtre
                    t+=t2
                    t+=+max(0,clients[track[i]][1]-t)  #ajout d'un temps d'attente si le livreur arrive avant le début de la fenêtre
                else :
                    t3+= (t+t2 - clients[track[i]][2])*time_penalty #ajout d'une pénalité si une fenêtre n'est pas respectée
                    t+=t2
                    
                    
                # Evaluation quantité
                
                if q >= clients[track[i]][0]:
                    q-=clients[track[i]][0]
                else : 
                    t3+=(clients[track[i]][0]-q)*quantity_penalty   #ajout d'une pénalité si une quantité n'est pas respectée
                    q=0

            except : 
                print("!!!!!!!!  PB  !!!!!!!!")
                print(truck_track)
                print(len(track))
                print(len(time_matrix[0]))
                t=3000
                
        trucks_time.append(t)
        t3+=t
#    print(track)
#    print(len(track))
#    print(len(time_matrix[0]))
    return t3,trucks_time
    
                

def population_evaluation(member):
    track=member[0]   


    cgt=[0]
    truck_track=[]
    
    for j in range(1,len(track)):
#        c1=max(0,track[j])
#        c2=max(0,track[j-1])

        if track[j] <= 0:           
            cgt.append(j)
            truck_track.append([0] + track[cgt[-2]+1:cgt[-1]] + [0])
            
    cgt.append(j)
    truck_track.append([0] + track[cgt[-2]+1:cgt[-1]+1] + [0])  
    
    
    t3,trucks_time=track_evaluation(truck_track)
        
    member[1]=t3
#    print(trucks_time)
    return member
        
#evaluation([generate()]+[10]) 
    
def circuit_camion(membre):
    circuit=membre[0]


    cgt=[0]
    circuit_truck=[]
    
    for j in range(1,len(circuit)):
#        c1=max(0,circuit[j])
#        c2=max(0,circuit[j-1])

        if circuit[j] <= 0:           
            cgt.append(j)
            circuit_truck.append([0] + circuit[cgt[-2]+1:cgt[-1]] + [0])
            
    cgt.append(j)
    circuit_truck.append([0] + circuit[cgt[-2]+1:cgt[-1]+1] + [0])  

    return circuit_truck


def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):        
        if gauche[index_gauche][1] <= droite[index_droite][1]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat
 
def tri_fusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))