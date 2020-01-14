from dominoes import all_Dominoes
from mesa import mesa, os
class Player(object):
    def __init__(self,name):
        self.hand = []
        self.name = name
        os.system('clear')
    def take_hand(self,tokens,tokens_per_player = 7): #tomas las fichas para la mano del jugador
        for _ in range(tokens_per_player):
            self.hand.append(tokens.pop())
        return tokens
    def show_hand(self): #muestra la mano del jugador
        print(self.hand)
    def discard_cards(self):
        z = int(input('Choose one to put in table: '))
        for i in range(8):
            if z == i:
                mesa.append_tokens(self.hand.pop(i - 1), int(input('choose your place: ')))
            elif z > len(self.hand):
                print("Buen caballo esa ficha no se puede \n estas son tus fichas")
                self.show_hand()
                self.discard_cards()
                break
