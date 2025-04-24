from Timmy import ouvir_comando_continuamente
from comandosBasicos import falar
import keyboard
import estado
from plyer import notification
import pyttsx3
import time

def listar_vozes_disponiveis():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print("🔊 Vozes disponíveis:")
    for index, voice in enumerate(voices):
        print(f"{index} - {voice.name} ({voice.id})")

def main():
    falar("Olá Mestre, como posso te ajudar hoje?")
    ouvir_comando_continuamente()

if __name__ == "__main__":
    print("Pressione F10 para ligar/desligar o assistente. ESC para sair.")

    try:
        while True:
            if keyboard.is_pressed("f10"):
                estado.ligar = not estado.ligar
                print("Assistente:", "Ligado" if estado.ligar else "Desligado")
                keyboard.wait("f10")

                if estado.ligar:
                    notification.notify(
                        title="🥸 Estou ativo!",
                        message="Você ativou o Timmy, seu assistente",
                        timeout=10
                    )
                    main()

            if keyboard.is_pressed("esc"):
                print("Saindo...")
                estado.ligar = False
                notification.notify(
                    title="🫂 Assistente desativado",
                    message="Tchau até a próxima",
                    timeout=10
                )
                break

            time.sleep(0.1)  # Evita travar o CPU

    except Exception as e:
        print(f"\n❗ Ocorreu um erro: {e}")
