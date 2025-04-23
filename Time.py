import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
from time import sleep, time
import re

engine = pyttsx3.init()

def falar(texto):
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
        
def executar_comando(comando):

    if "time" in comando:

        #horas
        if "horas" in comando or "horario" in comando or "horário" in comando:
            agora = datetime.now().strftime("%H:%M")
            falar(f"Agora são {agora}")
            executado = True

        #Data de Hoje
        if "data" in comando:
            data = datetime.now().strftime("%d/%m/%y")
            falar(f"Hoje é {data}")
            executado = True

        #GPT
        elif "gpt" in comando:
            webbrowser.open("https://chatgpt.com/")
            falar("Abrindo o GPT")
            executado = True

        #Tocar lofi
        elif "música" in comando or "musica" in comando and "relaxante" in comando or "calma" in comando:
            webbrowser.open("https://www.youtube.com/watch?v=28KRPhVzCus")
            falar("Tocando música relaxante!")
            executado = True

        #cronometro
        elif "cronometro" in comando or "crônometro" in comando:

            falar("Iniciando o cronômetro, diga 'parar' para parar")
            inicio = time()

            while True: 
                comando = input("Digite 'pare' para parar o cronômetro: ").lower().strip()

                if "pare" in comando or "parar" in comando:

                    fim = time()
                    tempo = fim - inicio
                    tempo_formatado = f"{tempo:.0f}"

                    falar(f"Foram {tempo_formatado} segundos")
                    break
                executado = True

        #lembrete
        elif "lembrete" in comando or "lembre" in comando:

            numeros = re.findall(r"\d+(?:\.\d+)?", comando)

            falar("Para que é o lembrete?")
            mensagem = input("Para que é o lembrete: ")

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

        elif "obrigado" in comando:
            falar("De nada, você é brabo!")
            executado = True

        #Não entedi
        if not executado:
            falar("Desculpe, não entendi o comando.")

while True:        
    comando = input("Digite o comando: ").strip().lower()
    executar_comando(comando)
    sleep(2)


#while True: 
#   comando = ouvir()
#   if comando = "":
#       continue
#   sleep(2)
