class Domino():
    def __init__ (self, dominoFace1, dominoFace2):
        self.dominoFace1 = dominoFace1 #la parte izquierda de una ficha
        self.dominoFace2 = dominoFace2 #la parte derecha de la ficha
        self.dominoFace = str(dominoFace1) + " | " + str(dominoFace2) + '|' #la ficha completa
        self.value = dominoFace1 + dominoFace2 #el valor de la ficha

all_Dominoes = [] #Todas las fichas

for i in range(7):
    for l in range(7):
        c = Domino(i, l)
        all_Dominoes.append([c.dominoFace])