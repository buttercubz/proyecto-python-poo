from dominoes import all_Dominoes

class Player(object):
    def __init__(self,name):
        self.hand = []
        self.name = name
        
    def take_hand(self,tokens,tokens_per_player = 7): #tomas las fichas para la mano del jugador
        for _ in range(tokens_per_player):
            self.hand.append(all_Dominoes)
            
    def show_hand(self): #muestra la mano del jugador 
        print ("{}'s hand".format(self.name))
        for c in self.hand:
            print("{}".format(self.hand))

        
player = Player('rivier') 
player.take_hand(all_Dominoes)
player.show_hand()
  