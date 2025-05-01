import comtypes.client

try:
    # Inicializa o motor de fala
    engine = comtypes.client.CreateObject("SAPI.SpVoice")
    
    # Testa o motor de fala com um texto simples
    engine.Speak("Olá, estou funcionando?")
except Exception as e:
    print(f"Erro ao inicializar o motor de fala: {e}")