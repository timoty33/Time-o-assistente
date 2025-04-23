import speech_recognition as sr
import time
import keyboard
from comandosBasicos import (
    falar, horas, hoje, abrirGPT, tocarLofi,
    cronometro, lembrete, obrigado,
    aumentarVelocidade, diminuirVelocidade, jogarMoeda, clima, naoEntendi
)
import estado

recognizer = sr.Recognizer()

ligar = True

def ouvir_comando_continuamente():
    ligar = True
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        if keyboard.is_pressed("f10"):
            estado.ligar = not estado.ligar
            print("Assistente:", "Ligado" if estado.ligar else "Desligado")
            keyboard.wait("f10")
        while estado.ligar:

            try:
                print("Escutando...")
                audio = recognizer.listen(source, timeout=5)
                texto = recognizer.recognize_google(audio, language="pt-BR")
                print(f"Você disse: {texto}")
                if texto.strip() != "":
                    processar_comando(texto)
            except sr.UnknownValueError:
                print("Não entendi.")
            except sr.WaitTimeoutError:
                pass
            except sr.RequestError:
                print("Erro de conexão.")
                break

def processar_comando(comando):

    if "assistente" in comando:

        if "hora" in comando or "horas" in comando:
            horas()
        elif "data" in comando or "hoje" in comando:
            hoje()
        elif "abrir gpt" in comando:
            abrirGPT()
        elif "lofi" in comando or "música relaxante" in comando:
            tocarLofi()
        elif "cronômetro" in comando:
            cronometro()
        elif "lembrete" in comando:
            lembrete(comando)
        elif "rápido" in comando:
            aumentarVelocidade()
        elif "devagar" in comando or "lento" in comando:
            diminuirVelocidade()
        elif "clima" in comando:
            clima()
        elif "moeda" in comando:
            jogarMoeda()
        elif "obrigado" in comando:
            obrigado()
        elif "sair" in comando:
            falar("Encerrando. Até logo!")
            exit()
        elif "dormir" in comando or "descansar" in comando:
            falar("Modo repouso")
            estado.ligar = False
        else:
            naoEntendi()
