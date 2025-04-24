from comandosBasicos import *
from comandosIA import *
import time
import pygame

pygame.mixer.init()

def bomDia():
    pygame.mixer.music.load("audios/galo_cantando.mp3")
    pygame.mixer.music.play()
    time.sleep(4)
    falar("Bom dia mago! Como você dormiu hoje? Vamos começar o dia com uma música animada!")
    tocarMusicaAnimada()
    time.sleep(8)
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
