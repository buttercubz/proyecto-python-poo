from dominoes import all_Dominoes

class Player(object):
    def __init__(self,name):
        self.hand = []
        self.name = name
        
    def take_hand(self,tokens,tokens_per_player = 7): #tomas las fichas para la mano del jugador
        for _ in range(tokens_per_player):
            self.hand.append(all_Dominoes.pop())
        return self
    
    def show_hand(self): #muestra la mano del jugador 
        print(self.hand)

        
player = Player(input('introduce your name here: ')) 
player.take_hand(all_Dominoes)
player.show_hand()

