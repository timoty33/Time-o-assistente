import base64
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# ========= CONFIGURAÇÕES =========
IMAGE_PATH = "rock2.png"  # 🖼️ Caminho da sua imagem local
SERPER_KEY = "8f7cc62382a2469d192a642a6f1dcc28251aa0c7"
GEMINI_KEY = "AIzaSyB0L7UvfgKhNAwKduIdAaPWlfRC4uu3l4s"

# ========= ETAPA 1: ENVIAR IMAGEM PRO SERPER =========
def buscar_links_por_imagem(image_path):
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    url = "https://google.serper.dev/lens"
    headers = {
        "X-API-KEY": SERPER_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "imageContent": image_base64
    }

    res = requests.post(url, headers=headers, json=payload)
    data = res.json()

    links = []
    if "organic" in data:
        for item in data["organic"][:3]:
            title = item.get("title", "Sem título")
            link = item.get("link", "")
            links.append((title, link))
    return links

# ========= ETAPA 2: PEGAR CONTEÚDO DOS LINKS =========
def extrair_texto_da_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        textos = soup.stripped_strings
        return "\n".join(list(textos)[:500])  # Limita o texto
    except Exception as e:
        return f"[Erro ao acessar {url}: {e}]"

# ========= ETAPA 3: ANALISAR COM GEMINI =========
def analisar_com_gemini(conteudos):
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = "Analise os seguintes textos extraídos de sites a partir de uma imagem:\n\n"
    for i, (titulo, link, texto) in enumerate(conteudos, 1):
        prompt += f"{i}. {titulo} ({link}):\n{texto[:1000]}\n\n"

    resposta = model.generate_content(prompt)
    return resposta.text

# ========= EXECUÇÃO =========
def executar_fluxo():
    print("🔍 Buscando links a partir da imagem...")
    links = buscar_links_por_imagem(IMAGE_PATH)

    if not links:
        print("❌ Nenhum link encontrado.")
        return

    conteudos = []
    for titulo, link in links:
        print(f"🌐 Acessando: {link}")
        texto = extrair_texto_da_url(link)
        conteudos.append((titulo, link, texto))

    print("\n🧠 Enviando para o Gemini...")
    analise = analisar_com_gemini(conteudos)

    print("\n📊 Resultado da análise do Gemini:\n")
    print(analise)

# ========= INICIAR =========
executar_fluxo()
