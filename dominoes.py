class Domino():
    def __init__ (self, dominoFace1, dominoFace2):
        self.dominoFace1 = dominoFace1
        self.dominoFace2 = dominoFace2
        self.dominoFace = str(dominoFace1) + " | " + str(dominoFace2)
        self.value = dominoFace1 + dominoFace2
        # self.value = set(self.value)

f = []
for i in range(7):
    for l in range(7):
        c = Domino(i, l)
        f.append(c.dominoFace)