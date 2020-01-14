from dominoes import all_Dominoes
#from mesa import Table
class bots(object):
    def __init__(self,name):
        self.hand = []
        self.name = name
        
    def take_hand(self,tokens,tokens_per_player = 7): 
        for i in range(tokens_per_player):
            self.hand.append(tokens.pop())
    def game(self):
        posit = str(input("Que ficha quieres jugar: "))
        self.hand.remove(posit)
    
    def show_hand(self): 
        print(self.hand,"\n") 


Bot = bots("juancito") 
Bot.take_hand(all_Dominoes) 
while True:    
    print("Estas son tus fichas")      
    Bot.show_hand()
    Bot.game()
    