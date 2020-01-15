from dominoes import all_Dominoes
from mesa import mesa
from Player import Player
# from bots import bots
jugadores = []
while True:
    jugadores.append(input('nombre 1: '))
    jugadores.append(input('nombre 2: '))
    jugadores.append(input('nombre 3: '))
    jugadores.append(input('nombre 4: '))
    break
jugador1 = Player(jugadores[0])
jugador2 = Player(jugadores[1])
jugador3 = Player(jugadores[2])
jugador4 = Player(jugadores[3])

jugador1.take_hand(all_Dominoes)
jugador2.take_hand(all_Dominoes)
jugador3.take_hand(all_Dominoes)
jugador4.take_hand(all_Dominoes)

while True:
    print(jugadores[0])
    jugador1.show_hand()
    jugador1.discard_cards()
    mesa.show_dominoes()
    print(jugadores[1])
    jugador2.show_hand()
    jugador2.discard_cards()
    mesa.show_dominoes()
    print(jugadores[2])
    jugador3.show_hand()
    jugador3.discard_cards()
    mesa.show_dominoes()
    print(jugadores[3])
    jugador4.show_hand()
    jugador4.discard_cards()
    mesa.show_dominoes()