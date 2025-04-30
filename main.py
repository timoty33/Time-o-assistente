from Timmy import iniciarThread, modoRepouso
from comandos.comandosBasicos import falar
import estado
from plyer import notification
import pyttsx3
import time
import eel

# Inicializa o Eel
eel.init("www")

def listar_vozes_disponiveis():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print("🔊 Vozes disponíveis:")
    for index, voice in enumerate(voices):
        print(f"{index} - {voice.name} ({voice.id})")

@eel.expose
def iniciar_assistente():
    if not estado.ligar:
        estado.ligar = True
        print(f"Olá {estado.USER}, como você está hoje?")
        notification.notify(
            title="🥸 Estou ativo!",
            message="Você ativou o Timmy, seu assistente",
            timeout=10
        )
        falar(f"Olá {estado.USER}, como posso te ajudar hoje?")
        iniciarThread()

@eel.expose
def parar_assistente():
    modoRepouso()

if __name__ == "__main__": 
    print("Inicializando Timmy...")
    eel.start("templates/index.html", port=8765)

    try:
        while True:
            time.sleep(1)  # Mantém o app rodando
    except Exception as e:
        print(f"\n❗ Ocorreu um erro: {e}")
