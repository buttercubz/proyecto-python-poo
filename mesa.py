from dominoes import all_Dominoes
import os
class Table:
    #   tokens son las fichas de domino
    def __init__(self, tokens):
        self.tokens = tokens
        self.empty = []
        self.cache = ' '
        self.data = None
#   show dominoes desplega todos los dominos en la mesa
    def show_dominoes(self, test = False):#el parametro test es para desplegar todo el domino
            for i in self.empty:
                self.data = self.cache.join(self.empty)
            print(self.data)
    def get_hand(self):
        return type(self.data)
    def append_tokens(self, tokens_per_players, place):
        if place == 2:
            self.empty.append(tokens_per_players)
            return self.empty
        elif place == 1:
            self.empty.insert(0, tokens_per_players)
            return self.empty
        print(self.empty)
    def get_points(self, hand):
        first_step = hand.replace("-", "+")
        return first_step

nueva_mesa = Table(all_Dominoes)
while True:
    nueva_mesa.append_tokens(input('choose your dominoes: '), int(input('choose your place: ')))
    os.system('clear')
    nueva_mesa.show_dominoes()
    print(nueva_mesa.get_points(nueva_mesa.get_hand()))

# a=['hola' , 'estoy' , 'haciendo' , 'un' , 'programa']
# cadena = " ".join(a)


# print(cadena)