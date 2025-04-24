import speech_recognition as sr
import time
import keyboard
from comandosBasicos import (
    falar, horas, hoje, aumentarVolume, diminuirVolume, alternar_mudo, 
    abrirGPT, tocarLofi, cronometro, lembrete, obrigado,
    aumentarVelocidade, diminuirVelocidade, jogarMoeda, clima, naoEntendi
)
from comandosIA import (fraseMotivacional, chatBot, curiosidade, piadas)
import estado
from plyer import notification

recognizer = sr.Recognizer()

def ouvir_comando_continuamente():
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
                if texto.strip().lower() != "":
                    processar_comando(texto)
            except sr.UnknownValueError:
                print("Não entendi.")
            except sr.WaitTimeoutError:
                pass
            except sr.RequestError:
                print("Erro de conexão.")
                break

def processar_comando(comando):

    if "assistente" in comando or "Tente":

        if "hora" in comando or "horas" in comando:
            horas()
        elif "data" in comando or "hoje" in comando:
            hoje()
        elif "aumentar" in comando and ("volume" in comando or "som" in comando):
            aumentarVolume(passo=0.1)
        elif "diminuir" in comando and ("volume" in comando or "som" in comando):
            diminuirVolume(passo=0.1)
        elif "silenciar" in comando or "silencio" in comando:
            alternar_mudo()
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
        elif "frase motivacional" in comando:
            fraseMotivacional()
        elif "curiosidade" in comando:
            curiosidade()
        elif "piada" in comando or "piadas" in comando:
            piadas()
        elif "inteligente" in comando:
            chatBot()
        elif "obrigado" in comando:
            obrigado()
        elif "sair" in comando:
            falar("Encerrando. Até logo!")
            exit()
        elif "dormir" in comando or "descansar" in comando or "repouso" in comando:
            falar("Modo repouso")
            estado.ligar = False
            notification.notify(
                title="💤🛏️ Modo repouso",
                message=f"O modo repouso está ativo mas o assistente ainda fará suas tarefas, para ativá-lo, aperte f10 2 vezes",
                timeout=10
            )
        else:
            naoEntendi()
