import random

class Domino(): #Clase para crear una pieza
    def __init__ (self, dominoFace1, dominoFace2):
        self.dominoFace1 = dominoFace1 # La parte izquierda de una ficha
        self.dominoFace2 = dominoFace2 # La parte derecha de la ficha
        self.dominoFace = str(dominoFace1) + "|" + str(dominoFace2) # La ficha completa

all_Dominoes = [] # Aquí se guardan todas las fichas

# Bucle que se encarga de rellenar el arreglo vacio.
f = 0
for i in range(7):
    for l in range(f, 7):
        c = Domino(i, l)
        all_Dominoes.append(c.dominoFace)
    f += 1

# Baraja las fichas
random.shuffle(all_Dominoes)