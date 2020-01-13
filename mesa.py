from dominoes import all_Dominoes
class Table:
    #   tokens son las fichas de domino
    def __init__(self, tokens):
        self.tokens = tokens
        self.empty = []
        self.cache = ''
#   show dominoes desplega todos los dominos en la mesa
    def show_dominoes(self, test = False):
        if test:
            for i in self.tokens:
                print(i[0])
        else:
            for i in self.empty:
                for j in i:
                    self.cache += j
            print(self.cache)
    def append_tokens(self, tokens_per_players, place):
        if place == 2:
            self.empty.append(tokens_per_players)
            return self.empty
        elif place == 1:
            self.empty.insert(0, tokens_per_players)
            return self.empty
        print(self.empty)


# print(all_Dominoes)



nueva_mesa = Table(all_Dominoes)
while True:
    nueva_mesa.append_tokens([input('fichas: ')], int(input('choose your place: ')))
    nueva_mesa.show_dominoes(True)

