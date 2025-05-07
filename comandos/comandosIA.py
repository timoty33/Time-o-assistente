import speech_recognition as sr
import google.generativeai as genai
from comandos.comandosBasicos import falar, ouvir
import estado
import pyautogui
import os
from PIL import Image
from time import sleep

GEMINI_KEY = estado.API_GEMINI
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def fraseMotivacional():

    resposta = model.generate_content("Crie uma frase motivacional única para motivar meu dia, todas as vezes que te pedir isso você precisará criar ou usar uma nova frase, você precisa ser bem autêntica e precisam ser frases muito legais! Mas lembre de nunca usar asteríscos na mensagem, e você precisa me devolver apenas a frase motivacional, nada antes nem depois.")
    resposta = resposta.text

    falar(resposta)

def curiosidade():

    resposta = model.generate_content("Me diga uma curiosidade interessante, mas preciso que todas as mensagens que você criar não podem ter asteríscos(*)")
    resposta = resposta.text

    falar(resposta)

def piadas():
    continuar = True

    while continuar:
        resposta = model.generate_content(
            "Agora você é um humorista muito experiente e sabe as melhores piadas do mundo, você irá dizer uma piada muito criativa e que seja bem fácil de entender, elas não podem ficar repetindo. Importante: lembre de que não pode usar asteríscos(*) na mensagem"
        )
        resposta = resposta.text

        falar(resposta)
        falar("Quer mais uma?")

        mais = ouvir().lower()

        if "sim" in mais or "quero" in mais:
            continuar = True
        else:
            falar("Tudo bem! Se quiser mais piadas depois, é só pedir.")
            continuar = False

    return ""  # Isso garante que a função termina normalmente, sem quebrar o fluxo principal   

def chatBot():

    falar("Chat de IA ativado!")
    # Inicia uma conversa com histórico
    chat = model.start_chat(history=[])

    sistema = "Você será um chatbot simpático de um assistente virtual. IMPORTANTE: você nunca pode usar asteriscos (*) na mensagem! Entenda que, por ser de um assistente virtual, a mensagem pode chegar um pouco 'estranha', então você deve interpretar a intenção do usuário. Além disso lembre-se que sua resposta será enviada por voz, e como não pode ser interrompida, você precisa ser breve e resumida, sem palavras mais complexas!"
    
    chat.send_message(sistema)

    mensagem = ""

    while True:
        falar("Ouvindo!")
        mensagem = ouvir()

        if not mensagem:
            falar("Você não disse nada")

        if "sair" in mensagem:
            falar("Encerrando o chat. Até logo!")
            break

        if mensagem:
            mensagem = mensagem.strip().lower()
            resposta = chat.send_message(mensagem)
            resposta = resposta.text.replace("*", "")
            falar(resposta)

contagem = 0

def chatBotAutomatico(mensagem):

    global contagem, chat

    contagem += 1

    if contagem == 1:

        chat = model.start_chat(history=[])

        sistema = "Você será um chatbot simpático de um assistente virtual. IMPORTANTE: você nunca pode usar asteriscos (*) na mensagem! Entenda que, por ser de um assistente virtual, a mensagem pode chegar um pouco 'estranha', então você deve interpretar a intenção do usuário. Além disso lembre-se que sua resposta será enviada por voz, e como não pode ser interrompida, você precisa ser breve e resumida, sem palavras mais complexas, mas sem ser tão resumido!"
        
        chat.send_message(sistema)

    if mensagem:
        mensagem = mensagem.strip().lower()
        resposta = chat.send_message(mensagem)
        resposta = resposta.text.replace("*", "")
        falar(resposta)

def verTela():

    falar("Analisando tela")

    sleep(0.5)

    # Tira o screenshot e salva como PNG
    screenshot_path = "temp_screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    # Carrega a imagem
    image = Image.open(screenshot_path)

    # Envia para o Gemini
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content([
        image,
        "Descreva essa captura de tela, em português sempre. Por você fazer parte de um assistente virtual, você precisa escrever uma resposta direto ao ponto e escrever a reposta com base no que o usuário está tentando saber, já que o usuário está fazendo uma pesquisa, se tiver textos na imagem, você precisa traduzir para o português!! Lembre-se de ser claro e resumido"
    ])

    # Mostra a resposta
    falar(response.text.replace("*", ""))

    # Apaga o arquivo temporário
    image.close()
    os.remove(screenshot_path)
