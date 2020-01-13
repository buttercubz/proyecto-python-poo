import random

class Domino(): #Clase para crear una pieza
    def __init__ (self, dominoFace1, dominoFace2):
        self.dominoFace1 = dominoFace1 # La parte izquierda de una ficha
        self.dominoFace2 = dominoFace2 # La parte derecha de la ficha
        self.dominoFace = str(dominoFace1) + "|" + str(dominoFace2) # La ficha completa

all_Dominoes = [] # Aquí se guardan todas las fichas

# Bucle que se encarga de rellenar el arreglo vacio.
for i in range(1, 6):
    for l in range(7):
        c = Domino(i, l)
        all_Dominoes.append(c.dominoFace)

# Remueve las piezas repetidas, ignoren el force v:
del all_Dominoes[2:6]
del all_Dominoes[6:9]

# Baraja las fichas
random.shuffle(all_Dominoes)