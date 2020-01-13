class Table:
#   tokens son las fichas de domino
    def __init__(self, tokens):
        self.tokens = tokens
#   show dominoes desplega todos los dominos en la mesa
    def show_dominoes(self):
        for i in self.tokens:
            print(i[0])

