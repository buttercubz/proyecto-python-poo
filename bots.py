from dominoes import all_Dominoes

class bots(object):
    def __int__(self,name):
        self.Hand = []
        self.name = name
        
    def takeFicha(self,tokens,tokens_per_player = 7): #tomas las fichas para la mano del jugador
        for _ in range(tokens_per_player):
            self.Hand.append(tokens.pop())
        return self
    

    def game(self, Hand):#juega una ficha de la que tiene en su mano
        pass

    def show(self):#muetra las fichas que tiene
        print(self.Hand)

    def takeFichaTable(self):#toma una ficha de la mesa cuando no tiene una para jugar
        pass
        #if canTakeToken:
     
player = bots("juan") 
player.takeFicha(all_Dominoes)


