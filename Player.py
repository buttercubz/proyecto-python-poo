from dominoes import all_Dominoes
from mesa import mesa, os
class Player:
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
        z = input('Choose one to put in table, "if you want to pass the hand write pass": ')
        if z == 'pass':
            mesa.append_tokens('', None, None)
        try:
            z = int(z)
            for i in range(8):
                if z == i:
                    mesa.append_tokens(self.hand.pop(i - 1), int(input('choose your place, "if you want to pass the hand write pass": ')), input('do you want to rotate this tab "yes" or "no": '))
                elif z > len(self.hand):
                    if len(self.hand) <= 0:
                        os.system('clear')
                        print(f'{self.name} gano la partida con {168 - mesa.return_points()} puntos')
                        break
                    else:
                        mesa.show_dominoes()
                        print("Buen caballo esa ficha no se puede \n estas son tus fichas")
                        self.show_hand()
                        self.discard_cards()
                        break
        except:
            print('None')
