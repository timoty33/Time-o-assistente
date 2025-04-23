import speech_recognition as sr
import pyttsx3 
import webbrowser
from datetime import datetime
import os
from time import sleep, time
import re
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import requests
import random

engine = pyttsx3.init()

def falar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        falar("Ouvindo...")
        audio = reconhecedor.listen(source)
        try:
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            falar("Você disse:", comando)
            return comando.lower()
        except:
            falar("Não entendi")
            return ""
        
executado = ""

def aumentarVelocidade():
    rate = engine.getProperty('rate')

    # Aumenta a velocidade (por exemplo, para 250 palavras por minuto)
    engine.setProperty('rate', rate + 50)
    falar("Agora eu falo mais rápido, o que achou?")

def diminuirVelocidade():
    rate = engine.getProperty('rate')

    # Aumenta a velocidade (por exemplo, para 250 palavras por minuto)
    engine.setProperty('rate', rate - 50)
    falar("Agora eu falo menos rápido, o que achou?")

def horas():
    #horas
    agora = datetime.now().strftime("%H:%M")
    falar(f"Agora são {agora}")
    executado = True

def ver_dia_da_semana():
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    hoje = datetime.now()
    dia_da_semana = dias[hoje.weekday()]  # weekday() retorna 0 (segunda) até 6 (domingo)
    return dia_da_semana

def hoje():
    # Data de Hoje
    data_atual = datetime.now().strftime("%d/%m/%y")  # Renomeando a variável
    falar(f"Hoje é {data_atual}, {ver_dia_da_semana()}")  # Usando a nova variável
    executado = True

def abrirGPT():
    #GPT
    webbrowser.open("https://chatgpt.com/")
    falar("Abrindo o GPT")
    executado = True

def tocarLofi():
    #Tocar lofi
    webbrowser.open("https://www.youtube.com/watch?v=28KRPhVzCus&autoplay=1")
    falar("Tocando música relaxante!")
    executado = True



def cronometro():
    #cronometro
    falar("Iniciando o cronômetro, diga 'parar' para parar")
    inicio = time()

    while True: 
        comando = input("Digite 'parar' para parar: ")

        if "pare" in comando or "parar" in comando:

            fim = time()
            tempo = fim - inicio
            tempo_formatado = f"{tempo:.0f}"

            falar(f"Foram {tempo_formatado} segundos")
            break
    executado = True

def lembrete(comando):
    #lembrete
    numeros = re.findall(r"\d+(?:\.\d+)?", comando)

    falar("Para que é o lembrete?")
    mensagem = ouvir()

    if numeros:

        minutos = float(numeros[0])
        segundos = minutos * 60

        falar(f"Ok, vou te lembrar em {minutos:.1f} minutos!")

        sleep(segundos / 2)

        print(segundos / 2)
        falar("Já se passou metade!")

        sleep(segundos / 2)
        falar(f"O tempo acabou. Esse é o seu lembrete para {mensagem}!")

    else: 

        falar("Um lembrete para daqui a quantos minutos?")

        minutos = float(input(">> "))
        segundos = minutos * 60

        falar(f"Ok, vou te lembrar em {minutos:.1f} minutos!")

        sleep(segundos / 2)

        print(segundos / 2)
        falar("Já se passou metade!")

        sleep(segundos / 2)
        falar(f"O tempo acabou. Este é seu lembrete para {mensagem}!")
        executado = True

def obrigado():
    #Obrigado
    falar("De nada, você é brabo!")
    executado = True

def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def aumentar_volume():
    volume = get_volume_interface()
    current_volume = volume.GetMasterVolumeLevelScalar()  # valor de 0.0 a 1.0
    novo_volume = min(current_volume + 0.1, 1.0)  # aumenta 10%, sem passar de 100%
    volume.SetMasterVolumeLevelScalar(novo_volume, None)
    print(f"Volume aumentado para {int(novo_volume * 100)}%")

def diminuir_volume():
    volume = get_volume_interface()
    current_volume = volume.GetMasterVolumeLevelScalar()
    novo_volume = max(current_volume - 0.1, 0.0)  # diminui 10%, sem ficar negativo
    volume.SetMasterVolumeLevelScalar(novo_volume, None)
    print(f"Volume diminuído para {int(novo_volume * 100)}%")

moeda = ["cara", "coroa"]
def jogarMoeda():

    falar("Vamos jogar cara ou coroa, você escolhe!")

    escolha = input("Digite: ['cara' ou 'coroa'] ")
    
    jogada = random.choice(moeda)

    if escolha == jogada:
        falar(f"Caiu {jogada}, você ganhou!")

    else:
        falar(f"Caiu {jogada}, você perdeu!")


def naoEntendi():
    #Se não reconhecer
    if not executado:
        falar("Desculpe, não entendi o comando.")
