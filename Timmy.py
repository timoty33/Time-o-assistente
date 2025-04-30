import speech_recognition as sr 
import threading
import keyboard
from comandos.comandosBasicos import *
from comandos.comandosIA import (fraseMotivacional, chatBot, curiosidade, piadas)
from comandos.rotinas import (bomDia, boaNoite, hidratacao, modoCinema)
import estado
from plyer import notification
import os

def modoRepouso():
    falar("Modo repouso")
    estado.ligar = False
    notification.notify(
        title="💤🛏️ Modo repouso",
        message=f"O modo repouso está ativo mas o assistente ainda fará suas tarefas, para ativá-lo, aperte f10 2 vezes",
        timeout=10
    )

recognizer = sr.Recognizer()

def ouvir_comando_continuamente():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:  # Mudei de 'while estado.ligar' para 'while True' para garantir que a escuta continue.
            if not estado.ligar:
                print("🛑 Escuta interrompida!")
                break  # Sai do loop apenas se o assistente for desligado explicitamente.

            print("Escutando...")

            audio = None
            for _ in range(100):  # Tentando ouvir por 10 segundos no total.
                try:
                    audio = recognizer.listen(source, timeout=0.1)
                    break  # Escuta válida, quebramos o loop interno e continuamos.
                except sr.WaitTimeoutError:
                    continue

            if not estado.ligar or audio is None:
                continue  # Se o estado for 'ligar' é False ou não há áudio, continua escutando.

            try:
                texto = recognizer.recognize_google(audio, language="pt-BR")
                print(f"Você disse: {texto}")
                if texto.strip().lower() != "":
                    processar_comando(texto)
                else:
                    print("Fala vazia!")
            except sr.UnknownValueError:
                print("Não entendi.")
            except sr.RequestError:
                print("Erro de conexão.")
                break  # Se houver erro de conexão, saímos do loop.

def iniciarThread():
    thread = threading.Thread(target=ouvir_comando_continuamente)
    thread.start()
    estado.ligar = True

def processar_comando(comando):

    if "assistente" in comando or "Assistente" in comando or "tente" in comando: # Nome do seu assistente

        if "hora" in comando or "horas" in comando: #basico
            horas()
        elif "data" in comando or "hoje" in comando:
            hoje()
        elif "aumentar" in comando or "Aumente" and ("volume" in comando or "som" in comando):
            aumentarVolume(passo=0.1)
        elif "diminuir" in comando and ("volume" in comando or "som" in comando):
            diminuirVolume(passo=0.1)
        elif "silenciar" in comando or "silencio" in comando:
            alternar_mudo()
        elif "aumentar" in comando or "mais" in comando and("brilho" in comando):
            aumentarBrilho()
        elif "diminuir" in comando or "menos" in comando and("brilho" in comando):
            diminuirBrilho()
        elif "abrir chat" in comando:
            abrirGPT()
        elif "lofi" in comando or "música relaxante" in comando:
            tocarLofi()
        elif "música" in comando and "animada" in comando:
            tocarMusicaAnimada()
        elif "cronômetro" in comando:
            cronometro()
        elif "traduzir" in comando or "tradução" in comando:
            texto = input("Digite o texto")
            traduzirTexto(texto)
        elif "receita" in comando and ("bebida" in comando or "drink" in comando):
            nome = input("Digite o nome da bebida: ")
            receitaDrink(nome)
        elif "cotação" in comando or "cotações" in comando:
            obter_cotacoes()
        elif "gato" in comando:
            abrir_imagem_de_gato()
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
        elif "como" in comando and "está" in comando:
            comoEsta()

        #IA
        elif "frase motivacional" in comando:
            fraseMotivacional()
        elif "curiosidade" in comando:
            curiosidade()
        elif "piada" in comando or "piadas" in comando:
            piadas()
        elif "inteligente" in comando:
            chatBot()

        #rotinas
        elif "Bom dia" in comando:
            diretorio_base = os.path.dirname(os.path.abspath(__file__))
            bomDia(diretorio_base)
        elif "boa noite" in comando:
            boaNoite()
        elif ("ativar" in comando or "iniciar" in comando) and "hidratação" in comando:
            hidratacao()
        elif ("desligar" in comando or "parar" in comando) and "hidratação" in comando:
            pausas = False
            falar("Hidratação interrompida!")
        elif "modo cinema" in comando:
            modoCinema()

        #outros
        elif "sair" in comando:
            falar("Encerrando. Até logo!")
            notification.notify(
                title="🥺 Assistente Desligado",
                message=f"O assistente está desligado, para ligar ele de novo, você precisa executar: 'main.py'",
                timeout=10
            )
            exit()
        elif "dormir" in comando or "descansar" in comando or "repouso" in comando:
            modoRepouso()
        elif "assistente" in comando or "Assistente" in comando:
            falar("Olá, me chamou")
        else:
            naoEntendi()


