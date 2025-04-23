from audio_config import ouvir_comando_continuamente
from comandosBasicos import falar
import keyboard
import estado

ligar = False

def main():
    falar("Iniciando!")
    ouvir_comando_continuamente()

print("Pressione F10 para ligar/desligar o assistente. ESC para sair.")

while True:
    if keyboard.is_pressed("f10"):
        estado.ligar = not estado.ligar
        print("Assistente:", "Ligado" if estado.ligar else "Desligado")
        keyboard.wait("f10")
        if estado.ligar:
            main()  # Chama main enquanto ligado

    if keyboard.is_pressed("esc"):
        print("Saindo...")
        estado.ligar = False
        break
