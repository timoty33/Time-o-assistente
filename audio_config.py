import speech_recognition as sr
import time
from comandosBasicos import (
    falar, horas, hoje, abrirGPT, tocarLofi,
    cronometro, lembrete, obrigado,
    aumentarVelocidade, diminuirVelocidade, jogarMoeda, naoEntendi
)

recognizer = sr.Recognizer()

def ouvir_comando_continuamente():
    with sr.Microphone() as source:
        print("Assistente ouvindo o tempo todo...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                audio = recognizer.listen(source, phrase_time_limit=6)
                comando = recognizer.recognize_google(audio, language="pt-BR").strip()
                if not comando:
                    print("Silêncio detectado. Ignorando...")
                    continue

                print(f"Comando reconhecido: {comando}")
                processar_comando(comando)
                time.sleep(1)

            except sr.UnknownValueError:
                print("Não entendi o que foi dito.")
            except sr.RequestError:
                print("Erro ao conectar ao serviço de reconhecimento de fala.")
                falar("Erro de conexão.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

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
        elif "moeda" in comando:
            jogarMoeda()
        elif "obrigado" in comando:
            obrigado()
        elif "sair" in comando:
            falar("Encerrando. Até logo!")
            exit()
        else:
            naoEntendi()
