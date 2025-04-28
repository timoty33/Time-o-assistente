from dotenv import load_dotenv
import os
from time import sleep

ligar = False #Não mude nada aqui


#Aqui estão suas configurações:

velocidadeFala = 250 #mínimo 50, máximo: 400
volumeFala = 0.7 #mínimo: 0, máximo: 1, lembre que a altura do som é relativo ao som do computador, ou seja se estiver 1, ele será 100% igual ao volume do sistema

# APIs

load_dotenv()

if not os.getenv('USER'):
    print("⚠️ Arquivo .env não encontrado ou variável USER não definida! Verifique se renomeou ele para '.env'")
    sleep(5)
    print("Saindo...")

API_GEMINI = os.getenv("GEMINI_KEY")
API_CLIMA = os.getenv("API_KEY_CLIMA")
USER = os.getenv("USER")
