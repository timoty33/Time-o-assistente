import comtypes.client
from time import sleep
import threading
import keyboard

engine = comtypes.client.CreateObject("SAPI.SpVoice")
engine.Rate = 2

parar = False

def monitorar_tecla():
    global parar
    while True:
        keyboard.wait("f10")
        engine.Volume = 80
        sleep(0.3)
        engine.Volume = 60
        sleep(0.3)
        engine.Volume = 40
        sleep(0.3)
        engine.Volume = 0
        sleep(0.3)
        parar = True
        engine.Speak("", 2)

def falar(texto):
    global parar
    parar = False
    engine.Volume = 100
    print(f"Falando: {texto}")
    engine.Speak(texto, 1)
    while engine.Status.RunningState == 2 and not parar:
        sleep(0.1)

threading.Thread(target=monitorar_tecla, daemon=True).start()

while True:
    texto = input("Digite o texto para falar (ou 'sair'): ")
    if texto.lower() == "sair":
        break
    falar(texto)
