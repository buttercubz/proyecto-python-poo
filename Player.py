from dominoes import all_Dominoes
from mesa import Table
class Player(object):
    def __init__(self,name):
        self.hand = []
        self.name = name
    def take_hand(self,tokens,tokens_per_player = 7): #tomas las fichas para la mano del jugador
        for _ in range(tokens_per_player):
            self.hand.append(tokens.pop())
            # print(self.hand)
        return tokens
    def show_hand(self): #muestra la mano del jugador
        print(self.hand)
    def discard_cards(self):
        z = int(input('Choose one to put in table: '))
        for i in range(8):
            if z == i:
                mesa.append_tokens(self.hand.pop(i - 1), int(input('choose your place: ')))

player = Player(input('introduce your name here: '))
player.take_hand(all_Dominoes)
player.show_hand()
mesa = Table(all_Dominoes)
for a in range(10):
    player.discard_cards()
    player.show_hand()
    mesa.show_dominoes()
    print(mesa.return_points())
