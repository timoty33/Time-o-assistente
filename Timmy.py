import speech_recognition as sr 
import threading
from comandos.comandosBasicos import *
from comandos.comandosIA import (fraseMotivacional, chatBot, curiosidade, piadas, chatBotAutomatico, verTela)
from comandos.rotinas import (bomDia, boaNoite, hidratacao)
from comandos.comandosAutomacoes import (buscarMaps)
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

comando_salvo = ""
def processar_comando(comando):

    if "assistente" in comando or "Assistente" in comando or "tente" in comando: # Nome do seu assistente

        contagem = True

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

        comando_salvo = comando

        comando = prever_intencao(comando)

        if comando != "nenhuma":

            if comando == "ver_horas": #basico
                horas()
                contagem = False
            elif comando == "ver_data":
                hoje()
                contagem = False

            if estado.EXPERIMENTAL == "True":
                if comando == "aumentar_volume":
                    aumentarVolume(passo=0.1)
                    contagem = False
                elif comando == "diminuir_volume":
                    diminuirVolume(passo=0.1)
                    contagem = False
                elif comando == "alternar_mudo":
                    alternar_mudo()
                    contagem = False
            
            elif comando == "aumentar_brilho":
                aumentarBrilho()
                contagem = False
            elif comando == "diminuir_brilho":
                diminuirBrilho()
                contagem = False
            elif comando == "abrir_chatgpt":
                abrirGPT()
                contagem = False
            elif comando == "tocar_lofi":
                tocarLofi()
                contagem = False
            elif comando == "tocar_musica_animada":
                tocarMusicaAnimada()
                contagem = False
            elif comando == "abrir_cronometro":
                cronometro()
                contagem = False
            elif comando == "traduzir_texto":
                texto = input("Digite o texto")
                traduzirTexto(texto)
                contagem = False
            elif comando == "ver_receitas_bebida":
                nome = input("Digite o nome da bebida: ")
                receitaDrink(nome)
                contagem = False
            elif comando == "ver_cotacoes":
                obter_cotacoes()
                contagem = False
            elif comando == "ver_imagens_gato":
                abrir_imagem_de_gato()
                contagem = False
            elif comando == "fazer_lembrete":
                lembrete(comando)
                contagem = False
            elif comando == "ver_clima":
                clima()
                contagem = False
            elif comando == "lançar_moeda":
                jogarMoeda()
                contagem = False
            elif comando == "agradecer":
                obrigado()
                contagem = False
            elif comando == "cumprimento":
                comoEsta()
                contagem = False

            #IA
            elif comando == "ver_frase_motivacional":
                fraseMotivacional()
                contagem = False
            elif comando == "ver_curiosidade":
                curiosidade()
                contagem = False
            elif comando == "ver_piada":
                piadas()
                contagem = False
            elif comando == "ativar_assistente_ia":
                chatBot()
                contagem = False
            elif comando == "ver_tela":
                verTela(comando_salvo)
                contagem = False

            #rotinas
            elif comando == "rotina_bom_dia":
                diretorio_base = os.path.dirname(os.path.abspath(__file__))
                bomDia(diretorio_base)
                contagem = False
            elif comando == "rotina_boa_noite":
                boaNoite()
                contagem = False
            elif comando == "rotina_lembrete_hidratacao":
                hidratacao()
                contagem = False
            elif comando == "desativar_lembrete_hidratacao":
                pausas = False
                falar("Hidratação interrompida!")
                contagem = False
            # elif comando == "":
            #     modoCinema()

            #outros
            elif "desligar" in comando_salvo or "sair" in comando_salvo:
                falar("Encerrando. Até logo!")
                notification.notify(
                    title="🥺 Assistente Desligado",
                    message=f"O assistente está desligado, para ligar ele de novo, você precisa executar: 'main.py'",
                    timeout=10
                )
                contagem = False
                exit()
            elif comando == "modo_repouso":
                modoRepouso()
                contagem = False
            # elif "assistente" in comando or "Assistente" in comando:
            #     falar("Olá, me chamou")

            if contagem == True:
                if comando == "nenhuma":
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
