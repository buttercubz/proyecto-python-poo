import threading
import time
from playsound import playsound
# def contar():
#     '''Contar hasta cien'''
#     contador = 0
#     while contador < 100:
#         contador+=1
#         print('Hilo:',
#               threading.current_thread().getName(),
#               'con identificador:',
#               threading.current_thread().ident,
#               'Contador:', contador)

# hilo1 = threading.Thread(target=contar)
# hilo2 = threading.Thread(target=contar)
# hilo1.start()
# hilo2.start()
# def musica():
#     playsound('Mac Miller - Good News.mp3')

def slep():
    conut = 0
    while conut <= 5000:
        conut += 1
        print(conut)
def sleps():
    playsound('Mac Miller - Good News.mp3')




hilo1 = threading.Thread(target = slep)
hilo2 = threading.Thread(target = sleps)


hilo2.start()
hilo1.start()