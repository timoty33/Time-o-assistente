from comandosBasicos import falar, ouvir
import estado
import webbrowser
import google.generativeai as genai
import urllib

GEMINI_KEY = estado.API_GEMINI
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

link = ""
def formatarUrlMaps(url):

    query = urllib.parse.quote_plus(url)

    return f"https://www.google.com/maps/search/{query}"

def buscarMaps(prompt):

    falar("Busca no Google maps!")
    
    resposta = model.generate_content(
        f"Transforme isso em uma frase de busca eficiente para o Google Maps, sem explicações, só a frase: '{prompt}'"
    )

    link = formatarUrlMaps(resposta)

    webbrowser.open(link)
