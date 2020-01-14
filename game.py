from dominoes import all_Dominoes
from mesa import mesa
from Player import Player
from bots import bots
jugadores = []
while True:
    jugadores.append(input('nombre 1: '))
    jugadores.append(input('nombre 2: '))
    # jugadores.append(input('nombre 3: '))
    # jugadores.append(input('nombre 4: '))
    break
nuevo_jugador = Player('')
nuevo_bot = bots('')
nuevo_jugador.take_hand(all_Dominoes)
nuevo_bot.take_hand(all_Dominoes)

while True:
    print(jugadores[0])
    nuevo_jugador.show_hand()
    nuevo_jugador.discard_cards()
    mesa.show_dominoes()
    print(jugadores[1])
    nuevo_bot.show_hand()
    nuevo_bot.game()
    mesa.show_dominoes()