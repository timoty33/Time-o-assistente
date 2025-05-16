from comandos.comandosBasicos import falar, ouvir
import estado
import webbrowser
import google.generativeai as genai
import urllib

GEMINI_KEY = estado.API_GEMINI
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

link = ""
padrao = ""
def formatarUrlMaps(url):

    query = urllib.parse.quote_plus(url)

    return f"https://www.google.com/maps/search/{query}"

def buscarMaps(prompt):

    falar("Busca no Google maps!")
    
    resposta = model.generate_content(
        f"Reescreva a frase abaixo como uma busca direta no Google Maps. Se for genérica, retorne até 5 locais próximos. Apenas a frase, sem explicação: '{prompt}'"
    )

    resposta = resposta.text.strip()

    link = formatarUrlMaps(resposta)

    webbrowser.open(link)

    executado = True
