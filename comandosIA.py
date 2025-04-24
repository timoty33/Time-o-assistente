import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 40)

def falar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        falar("Ouvindo...")

        try:
            audio = reconhecedor.listen(source, timeout=5, phrase_time_limit=8)
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            falar(f"Você disse: {texto}")
            return texto.lower()
        except sr.WaitTimeoutError:
            falar("Você não falou nada.")
        except sr.UnknownValueError:
            falar("Não entendi o que você disse.")
        except sr.RequestError as e:
            falar(f"Erro ao se conectar ao serviço de reconhecimento: {e}")
        except Exception as e:
            falar(f"Ocorreu um erro: {e}")

        return ""
        
API_KEY = "AIzaSyB0L7UvfgKhNAwKduIdAaPWlfRC4uu3l4s"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def fraseMotivacional():

    resposta = model.generate_content("Crie uma frase motivacional única para motivar meu dia, todas as vezes que te pedir isso você precisará criar ou usar uma nova frase, você precisa ser bem autêntica e precisam ser frases muito legais! Mas lembre de nunca usar asteríscos na mensagem, e você precisa me devolver apenas a frase motivacional, nada antes nem depois.")
    resposta = resposta.text

    falar(resposta)

def chatBot():
    
    chat = model.start_chat(history=[])

    sistema = "Você será um chatbot simpático de um assistente virtual. IMPORTANTE: !!!você nunca pode usar asteríscos na mensagem!!!, você tem que saber que por ser de um assistente virtual a mensagem pode chegar um pouco 'estranha' por isso você irá precisar entender  a intenção do usuário."
    chat.send_message(sistema)

    mensagem = ""

    while mensagem != "sair":

        mensagem = ouvir()

        resposta = model.generate_content(mensagem)
        resposta = resposta.text

        falar(resposta)
