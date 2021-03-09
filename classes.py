global liste_clients 
liste_clients=[]

class Client:
    

    
    def __init__(self, name, x, y, quantity, start, stop):
        self.name = name
        self.x = x
        self.y = y
        self.quantity = quantity
        self.start = start
        self.stop = stop
        self.delivered = False
        liste_clients.append([name, x, y, quantity, start, stop])

class Truck:
    
    def __init__(self, name, quantity_max, start, stop):
        self.name = name
        self.x = 0
        self.y = 0
        self.quantity_max = quantity_max
        self.start = start
        self.stop = stop
        self.remaining_quantity=quantity_max

    def delivery(self, client):
        self.x=client.x
        self.y=client.y
        if self.remaining_quantity >= client.quantity:
            self.remaining_quantity -= client.quantity
            client.delivered = True

def liste():
    return(liste_clients)
import numpy as np

def distance(C1, C2):
    return(np.sqrt((C1.y-C2.y)**2 + (C1.x - C2.x)**2))