from playsound import playsound 
from threading import Thread

def func1():
    print('Working')
    
def func2():
    playsound("music/CLASICO DE MARINO PEREZ MIX 1 COMPLETO..mp3")

Thread(target = func2).start()
Thread(target = func1).start()