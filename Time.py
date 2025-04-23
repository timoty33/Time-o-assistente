import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
from time import sleep, time
import re
from comandosBasicos import horas, data, abrirGPT, tocarLofi, cronometro, lembrete, aumentar_volume, diminuir_volume, ver_dia_da_semana

engine = pyttsx3.init()

voices = engine.getProperty('voices')
    
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_PAULO_11.0')

engine.setProperty('rate', 250)

engine.setProperty('volume', 0.6)

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

while True:
    comando = input("Digite o comando: ").lower().strip() #ouvir()
    #if comando != "":
        #print("Comando detectado:", comando)
            
    if "time" in comando or "timi" in comando:

        if "horas" in comando or "hora" in comando or "horário" in comando or "horario" in comando:
            horas()

        elif "data" in comando or "dia" in comando or "hoje" in comando:
            data()

        elif "dia" in comando and "semana" in comando:
            ver_dia_da_semana

        elif "gpt" in comando or "GPT" in comando: 
            abrirGPT()

        elif "musica" in comando or "música" in comando or "lofi" in comando or "calma" in comando or "relaxante" in comando:
            tocarLofi()

        elif "cronometro" in comando or "crônometro" in comando:
            cronometro()

        elif "lembrete" in comando or "lembre" in comando:
            lembrete(comando)

        elif "aumentar" in comando or "mais" in comando and "volume" in comando or "som" in comando:
            aumentar_volume()

        elif "diminuir" in comando or "menos" in comando and "volume" in comando or "som" in comando:
            diminuir_volume()

        elif "sair" in comando:
            falar("Encerrando assistente...")
            break
    #else:
        # Não faz nada se não entendeu, apenas continua ouvindo
        #pass
