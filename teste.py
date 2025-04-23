import keyboard

estado = False

print("Pressione a tecla 'f10' para alternar o estado. Pressione 'esc' para sair.")

while True:
    if keyboard.is_pressed("f10"):
        estado = not estado
        print("Estado:", estado)
        keyboard.wait("f10")  # espera soltar a tecla para evitar múltiplos toques

    if keyboard.is_pressed("esc"):
        print("Encerrando...")
        break
