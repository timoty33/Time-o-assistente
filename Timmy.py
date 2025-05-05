import speech_recognition as sr 
import threading
from comandos.comandosBasicos import *
from comandos.comandosIA import (fraseMotivacional, chatBot, curiosidade, piadas, chatBotAutomatico)
from comandos.rotinas import (bomDia, boaNoite, hidratacao, modoCinema)
import estado
from plyer import notification
import os
from model.TimmyIA import prever_intencao

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

        textoFormatado1 = comando.find("assistente")
        textoFormatado2 = comando.find("Assistente")
        textoFormatado3 = comando.find("tente")

        texto = ""

        if textoFormatado1:
            texto = comando.replace("assistente", "")
        elif textoFormatado2:
            texto = comando.replace("Assistente", "")
        elif textoFormatado3:
            texto = comando.replace("tente", "")

        comando = prever_intencao(comando)

        if comando != "nenhuma":

            if comando == "ver_horas": #basico
                horas()
            elif comando == "ver_data":
                hoje()

            if estado.EXPERIMENTAL == "True":
                if comando == "aumentar_volume":
                    aumentarVolume(passo=0.1)
                elif comando == "diminuir_volume":
                    diminuirVolume(passo=0.1)
                elif comando == "alternar_mudo":
                    alternar_mudo()
            
            elif comando == "aumentar_brilho":
                aumentarBrilho()
            elif comando == "diminuir_brilho":
                diminuirBrilho()
            elif comando == "abrir_chatgpt":
                abrirGPT()
            elif comando == "tocar_lofi":
                tocarLofi()
            elif comando == "tocar_musica_animada":
                tocarMusicaAnimada()
            elif comando == "abrir_cronometro":
                cronometro()
            elif comando == "traduzir_texto":
                texto = input("Digite o texto")
                traduzirTexto(texto)
            elif comando == "ver_receitas_bebida":
                nome = input("Digite o nome da bebida: ")
                receitaDrink(nome)
            elif comando == "ver_cotacoes":
                obter_cotacoes()
            elif comando == "ver_imagens_gato":
                abrir_imagem_de_gato()
            elif comando == "fazer_lembrete":
                lembrete(comando)
            elif comando == "ver_clima":
                clima()
            elif comando == "lançar_moeda":
                jogarMoeda()
            elif comando == "agradecer":
                obrigado()
            elif comando == "cumprimento":
                comoEsta()

            #IA
            elif comando == "ver_frase_motivacional":
                fraseMotivacional()
            elif comando == "ver_curiosidade":
                curiosidade()
            elif comando == "ver_piada":
                piadas()
            elif comando == "ativar_assistente_ia":
                chatBot()

            #rotinas
            elif comando == "rotina_bom_dia":
                diretorio_base = os.path.dirname(os.path.abspath(__file__))
                bomDia(diretorio_base)
            elif comando == "rotina_boa_noite":
                boaNoite()
            elif comando == "rotina_lembrete_hidratacao":
                hidratacao()
            elif comando == "desativar_lembrete_hidratacao":
                pausas = False
                falar("Hidratação interrompida!")
            # elif comando == "":
            #     modoCinema()

            #outros
            elif comando == "desligar_assistente":
                falar("Encerrando. Até logo!")
                notification.notify(
                    title="🥺 Assistente Desligado",
                    message=f"O assistente está desligado, para ligar ele de novo, você precisa executar: 'main.py'",
                    timeout=10
                )
                exit()
            elif comando == "modo_repouso":
                modoRepouso()
            # elif "assistente" in comando or "Assistente" in comando:
            #     falar("Olá, me chamou")
            elif comando == "nenhuma":
                naoEntendi()
            else:
                naoEntendi()

    elif "Time" in comando or "time" in comando:

        falar("Assistente inteligente")

        textoFormatado1 = comando.find("assistente")
        textoFormatado2 = comando.find("Assistente")
        textoFormatado3 = comando.find("tente")

        texto = ""

        if textoFormatado1:
            texto = comando.replace("assistente", "")
        elif textoFormatado2:
            texto = comando.replace("Assistente", "")
        elif textoFormatado3:
            texto = comando.replace("tente", "")
        chatBotAutomatico(texto)
