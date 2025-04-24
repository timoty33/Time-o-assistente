import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
from comandosBasicos import falar, ouvir

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 40)
        
API_KEY = "AIzaSyB0L7UvfgKhNAwKduIdAaPWlfRC4uu3l4s"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def fraseMotivacional():

    resposta = model.generate_content("Crie uma frase motivacional única para motivar meu dia, todas as vezes que te pedir isso você precisará criar ou usar uma nova frase, você precisa ser bem autêntica e precisam ser frases muito legais! Mas lembre de nunca usar asteríscos na mensagem, e você precisa me devolver apenas a frase motivacional, nada antes nem depois.")
    resposta = resposta.text

    falar(resposta)

def curiosidade():

    resposta = model.generate_content("Me diga uma curiosidade interessante, mas preciso que todas as mensagens que você criar não podem ter asteríscos(*)")
    resposta = resposta.text

    falar(resposta)

def piadas():
    continuar = True

    while continuar:
        resposta = model.generate_content(
            "Agora você é um humorista muito experiente e sabe as melhores piadas do mundo, você irá dizer uma piada muito criativa e que seja bem fácil de entender, elas não podem ficar repetindo. Importante: lembre de que não pode usar asteríscos(*) na mensagem"
        )
        resposta = resposta.text

        falar(resposta)
        falar("Quer mais uma?")

        mais = ouvir().lower()

        if "sim" in mais or "quero" in mais:
            continuar = True
        else:
            falar("Tudo bem! Se quiser mais piadas depois, é só pedir.")
            continuar = False

    return ""  # Isso garante que a função termina normalmente, sem quebrar o fluxo principal   

def chatBot():
    # Inicia uma conversa com histórico
    chat = model.start_chat(history=[])

    sistema = "Você será um chatbot simpático de um assistente virtual. IMPORTANTE: você nunca pode usar asteriscos (*) na mensagem! Entenda que, por ser de um assistente virtual, a mensagem pode chegar um pouco 'estranha', então você deve interpretar a intenção do usuário."
    
    chat.send_message(sistema)

    mensagem = ""

    while True:
        mensagem = ouvir().strip().lower()

        if mensagem == "sair":
            falar("Encerrando o chat. Até logo!")
            break

        resposta = chat.send_message(mensagem)
        falar(resposta.text)
