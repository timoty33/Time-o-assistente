from Timmy import iniciarThread, modoRepouso
from comandos.comandosBasicos import falar
import estado
from plyer import notification
import time
import eel

# Inicializa o Eel
eel.init("www")

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
    eel.start("templates/index.html", port=8765, size=(450, 750))

    try:
        while True:
            time.sleep(1)  # Mantém o app rodando
    except Exception as e:
        print(f"\n❗ Ocorreu um erro: {e}")
