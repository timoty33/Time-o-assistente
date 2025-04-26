from comandosBasicos import *
from comandosIA import *
from time import sleep
import pygame
from plyer import notification
import threading

pygame.mixer.init()

pausas = True

def bomDia():
    sleep(4)
    falar("Bom dia mago! Como você dormiu hoje? Vamos começar o dia com uma música animada!")
    tocarMusicaAnimada()
    sleep(8)
    falar("Aqui vai a frase do dia: ")
    fraseMotivacional()
    hoje()
    clima()
    falar("Tomara que você tenha um ótimo dia mestre!")

def boaNoite():

    alternar_mudo()

    for i in range(4):
        diminuirBrilho()
    for i in range(3):
        diminuirVolume()

    alternar_mudo()

    falar("Ativando modo noite!")
    tocarLofi()

def hidratacao():
    falar("Lembretes de hidratação ativados!")
    def rotina_hidratacao():
        while pausas:
            sleep(20)  # Espera 35 minutos (2100 segundos)
            notification.notify(
                title="🏋️‍♂️🫗 Beba água",
                message="Faça uma pausa, você precisa beber água, descanse um pouco, aproveite o momento!",
                timeout=15
            )
            print("Faça uma pausa, se alongue um pouco!")

    # Criando e iniciando a thread dentro da função
    hidratacao_thread = threading.Thread(target=rotina_hidratacao)
    hidratacao_thread.daemon = True  # A thread é daemon, encerrará com o programa
    hidratacao_thread.start()


