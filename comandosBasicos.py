import speech_recognition as sr
import pyttsx3 
import webbrowser
from datetime import datetime
import os
from time import time, sleep
import re
import requests
import random
from plyer import notification
import threading
import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import estado
import keyboard

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

engine = pyttsx3.init()
engine.setProperty("rate", estado.velocidadeFala)
engine.setProperty("volume", estado.volumeFala)

def falar(texto):
    engine.say(texto)
    print(texto)
    engine.runAndWait()

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=3)
        print("Ouvindo...")

        try:
            audio = reconhecedor.listen(source, timeout=5, phrase_time_limit=6)
            texto = reconhecedor.recognize_google(audio, language='pt-BR').lower()
            texto = texto.lower()
            print(f"Você disse: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("Não entendi.")
        except sr.WaitTimeoutError:
            print("Tempo esgotado.")
        except sr.RequestError:
            print("Erro ao acessar serviço de reconhecimento.")
        return ""

executado = ""

# COMANDOS
def aumentarVelocidade():
    rate = engine.getProperty('rate')

    # Aumenta a velocidade (por exemplo, para 250 palavras por minuto)
    engine.setProperty('rate', rate + 50)
    falar("Agora eu falo mais rápido, o que achou?")
    executado = True

def diminuirVelocidade():
    rate = engine.getProperty('rate')

    # Aumenta a velocidade (por exemplo, para 250 palavras por minuto)
    engine.setProperty('rate', rate - 50)
    falar("Agora eu falo menos rápido, o que achou?")
    executado = True

def horas():
    #horas
    agora = datetime.now().strftime("%H:%M")
    falar(f"Agora são {agora}")
    executado = True

def aumentarVolume(passo=0.1):

    volume_atual = volume.GetMasterVolumeLevelScalar()  # valor entre 0.0 e 1.0
    novo_volume = min(volume_atual + passo, 1.0)  # máximo 1.0
    volume.SetMasterVolumeLevelScalar(novo_volume, None)

    falar(f"Volume aumentado para: {int(novo_volume * 100)}%")

    executado = True

def diminuirVolume(passo=0.1):

    volume_atual = volume.GetMasterVolumeLevelScalar()  # valor entre 0.0 e 1.0
    novo_volume = min(volume_atual - passo, 1.0)  # máximo 1.0
    volume.SetMasterVolumeLevelScalar(novo_volume, None)

    falar(f"Volume diminuido para: {int(novo_volume * 100)}%")
    executado = True

def alternar_mudo():

    estado_atual = volume.GetMute()
    volume.SetMute(not estado_atual, None)

    if not estado_atual:
        print("🔇 Som mutado.")
        falar("Som mutado")
    else:
        print("🔊 Som desmutado.")
        falar("Som desmutado")
    executado = True
    
def aumentarBrilho():
    sbc.set_brightness('+10')
    falar("Brilho aumentado")
    executado = True

def diminuirBrilho():
    sbc.set_brightness('-10')
    falar("Brilho diminuido")
    executado = True

def ver_dia_da_semana():
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    hoje = datetime.now()
    dia_da_semana = dias[hoje.weekday()]  # weekday() retorna 0 (segunda) até 6 (domingo)
    return dia_da_semana
    executado = True    

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

def tocarMusicaAnimada():
    
    musicas = [
        "https://www.youtube.com/watch?v=ru0K8uYEZWw&autoplay=1",
        "https://www.youtube.com/watch?v=OPf0YbXqDm0&autoplay=1",
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs&autoplay=1"
        ]
    musica = random.choice(musicas)
    webbrowser.open(musica)
    falar("Tocando música animada!")
    executado = True

API_KEY_CLIMA = "b1c447602ac1733630ac465ec871d141"
cityname = "brasília" #piçarras, joinville, rio de janeiro, são paulo
linkClima = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY_CLIMA}&units=metric&lang=pt_br"
linkPrevisao = f"http://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={API_KEY_CLIMA}&units=metric&lang=pt_br"

def clima():

    resposta = requests.get(linkPrevisao)
    dados = resposta.json()

    requisicao = requests.get(linkClima) 
    requisicao_dic = requisicao.json()

    tempo = requisicao_dic["weather"][0]["main"]

    sensacao = requisicao_dic["main"]["feels_like"]

    max_temperatura = requisicao_dic["main"]["temp_max"]

    min_temperatura = requisicao_dic["main"]["temp_min"]

    umidade = requisicao_dic["main"]["humidity"]

    for previsao in dados["list"][:5]:  # próximas 24h (3h x 5)
        hora_completa = previsao["dt_txt"]  # exemplo: '2025-04-25 15:00:00'
        hora_obj = datetime.strptime(hora_completa, "%Y-%m-%d %H:%M:%S")
        hora_formatada = f"{hora_obj.hour}h"

        clima = previsao["weather"][0]["description"]
        chuva = previsao.get("rain", {}).get("3h", 0)

        falar(f"{hora_formatada}: {clima} | Chuva: {chuva} mm")

    fala = f"O clima em {cityname} é: {tempo},\nsensação térmica: {sensacao:.1f} graus\na temperatura máxima será de: {max_temperatura:.1f} graus célsius,\ne a mínima de : {min_temperatura:.1f} graus,\na umidade está em: {umidade}%".replace(".", ",")

    falar(fala)
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

        def lembrar():
            sleep(segundos / 2)
            notification.notify(
                title="⏰ Lembrete do Assistente",
                message=f"Já passou metade do tempo para: {mensagem}",
                timeout=10
            )
            
            sleep(segundos / 2)
            notification.notify(
                title="⏰ Lembrete do Assistente",
                message=f"Seu lembrete para: {mensagem}",
                timeout=10
            )
            falar("Hora de", mensagem)

    else: 

        falar("Um lembrete para daqui a quantos minutos?")

        minutos = float(input(">> "))
        segundos = minutos * 60

        falar(f"Ok, vou te lembrar em {minutos:.1f} minutos!")

        def lembrar():
            sleep(segundos / 2)
            notification.notify(
                title="⏰ Lembrete do Assistente",
                message=f"Já passou metade do tempo para: {mensagem}",
                timeout=10
            )
            
            sleep(segundos / 2)
            notification.notify(
                title="⏰ Lembrete do Assistente",
                message=f"Seu lembrete para: {mensagem}",
                timeout=10
            )
            falar("Hora de", mensagem)
    
        executado = True

    # Cria e inicia a thread
    thread = threading.Thread(target=lembrar)
    thread.start()

def obrigado():
    #Obrigado
    falar("De nada, você é brabo!")
    executado = True

def comoEsta():
    falar("Estou bem, obrigado pela pergunta. E você?")

moeda = ["cara", "coroa"]
def jogarMoeda():

    falar("Vamos jogar cara ou coroa, você escolhe!")

    escolha = ouvir()
    
    jogada = random.choice(moeda)

    if escolha == jogada:
        falar(f"Caiu {jogada}, você ganhou!")

    else:
        falar(f"Caiu {jogada}, você perdeu!")

    executado = True


def naoEntendi():
    #Se não reconhecer
    if not executado:
        falar("Desculpe, não entendi o comando.")
