from Timmy import ouvir_comando_continuamente
from comandosBasicos import falar
import keyboard
import estado
from plyer import notification
import pyttsx3

def listar_vozes_disponiveis():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    print("🔊 Vozes disponíveis:")
    for index, voice in enumerate(voices):
        print(f"{index} - {voice.name} ({voice.id})")

def main():
    listar_vozes_disponiveis()
    falar("Olá Mestre, como posso te ajudar hoje?")
    ouvir_comando_continuamente()

print("Pressione F10 para ligar/desligar o assistente. ESC para sair.")

while True:
    if keyboard.is_pressed("f10"):
        estado.ligar = not estado.ligar
        print("Assistente:", "Ligado" if estado.ligar else "Desligado")
        keyboard.wait("f10")
        if estado.ligar:
            notification.notify(
                title="🥸 Estou ativo!",
                message=f"Você ativou o Timmy, seu assistente",
                timeout=10
            )
            main()  # Chama main enquanto ligado

    if keyboard.is_pressed("esc"):
        print("Saindo...")
        estado.ligar = False
        notification.notify(
            title="🫂 Assistente desativado",
            message="Tchau até a próxima",
            timeout=10
        )
        break
