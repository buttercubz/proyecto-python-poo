from dominoes import all_Dominoes
from mesa import mesa
class bots(object):
    def __init__(self,name):
        self.hand = []
        self.name = name
    def take_hand(self,tokens,tokens_per_player = 7):
        for i in range(tokens_per_player):
            self.hand.append(tokens.pop())
    def game(self):
        z = int(input('Choose one to put in table: '))
        for i in range(8):
            if z == i:
                mesa.append_tokens(self.hand.pop(i - 1), int(input('choose your place: ')))
    def show_hand(self):
        print(self.hand,"\n")
    def get_hand(self):
        return self.hand
    def discard_key(self):