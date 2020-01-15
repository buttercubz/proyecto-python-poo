from dominoes import all_Dominoes
import os
class Table:
    #   tokens son las fichas de domino
    def __init__(self, tokens):
        self.tokens = tokens
        self.empty = []
        self.cache = ' '
        self.data = None
        self.points = 0
        self.place = None
#   show dominoes desplega todos los dominos en la mesa
    def show_dominoes(self, test = False):
        if test:#el parametro test es para desplegar todo el domino
            for j in self.tokens:
                print(j)
        for i in self.empty:
            self.data = self.cache.join(self.empty)
        print(self.data)
    def append_tokens(self, tokens_per_players, place, reverse):
        self.place = place
        if place == 2:
            if reverse == 'yes':
                self.empty.append(tokens_per_players[::-1])
                os.system('clear')
                return self.empty
            else:
                self.empty.append(tokens_per_players)
                os.system('clear')
                return self.empty
        elif place == 1:
            if reverse == 'yes':
                self.empty.insert(0,tokens_per_players[::-1])
                os.system('clear')
                return self.empty
            else:
                self.empty.insert(0, tokens_per_players)
                os.system('clear')
                return self.empty
    def return_points(self):
        self.points = self.data.replace('|', '+').replace(' ', '+')
        points = eval(self.points)
        return int(points)

mesa = Table(all_Dominoes)