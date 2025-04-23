import speech_recognition as sr
import pyttsx3 
import webbrowser
from datetime import datetime
import os
from time import sleep, time
import re
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import requests
import random

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 40)

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
        
def ouvirMoeda():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        falar("Ouvindo...")
        audio = reconhecedor.listen(source)
        try:
            escolha = reconhecedor.recognize_google(audio, language='pt-BR')
            falar("Você disse:", comando)
            return escolha.lower()
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

API_KEY_CLIMA = "b1c447602ac1733630ac465ec871d141"
cityname = "brasília" #piçarras, joinville, rio de janeiro, são paulo
linkClima = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY_CLIMA}"

def clima():
    requisicao = requests.get(linkClima) 
    requisicao_dic = requisicao.json()

    tempo = requisicao_dic["weather"][0]["main"]

    sensacao = requisicao_dic["main"]["feels_like"]
    sensacao = sensacao - 273.15

    max_temperatura = requisicao_dic["main"]["temp_max"]
    max_temperatura = max_temperatura - 273.15

    min_temperatura = requisicao_dic["main"]["temp_min"]
    min_temperatura = min_temperatura - 273.15

    umidade = requisicao_dic["main"]["humidity"]


    fala = f"O tempo em {cityname} é: descrição: {tempo},\nsensação térmica: {sensacao:.1f} graus\na temperatura máxima será de: {max_temperatura:.1f} graus célsius,\ne a mínima de : {min_temperatura:.1f} graus,\na umidade está em: {umidade}%".replace(".", ",")

    falar(fala)

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

moeda = ["cara", "coroa"]
def jogarMoeda():

    falar("Vamos jogar cara ou coroa, você escolhe!")

    escolha = input("Digite a sua escolha ['cara' ou 'coroa']: ")
    
    jogada = random.choice(moeda)

    if escolha == jogada:
        falar(f"Caiu {jogada}, você ganhou!")

    else:
        falar(f"Caiu {jogada}, você perdeu!")


def naoEntendi():
    #Se não reconhecer
    if not executado:
        falar("Desculpe, não entendi o comando.")
