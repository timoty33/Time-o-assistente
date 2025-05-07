import pyautogui
import os
import google.generativeai as genai
from PIL import Image
from time import sleep
from comandos.comandosBasicos import falar

# Configura a API
genai.configure(api_key="AIzaSyB0L7UvfgKhNAwKduIdAaPWlfRC4uu3l4s")

def verTela():

    falar("Analisando tela")

    sleep(5)

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
        "Descreva essa captura de tela, em português sempre. Por você fazer parte de um assistente virtual, você precisa escrever uma resposta direto ao ponto e explicativa, já que o usuário está fazendo uma pesquisa!! Lembre-se de ser claro e resumido"
    ])

    # Mostra a resposta
    print(response.text)

    # Apaga o arquivo temporário
    image.close()
    os.remove(screenshot_path)
