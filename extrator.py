import requests
from bs4 import BeautifulSoup

# URL do site de notícias (G1 - Tecnologia)
url = "https://g1.globo.com/tecnologia/"

# Headers para simular um navegador real (evita bloqueio)
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("🌐 Acessando o site...")
resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
	print("✅ Site acessado com sucesso!")
	print(f"📄 Tamanho da página: {len(resposta.text)} caracteres")

	# Cria o objeto BeautifulSoup para analisar o HTML
	soup = BeautifulSoup(resposta.text, 'html.parser')

	# Exibe o título da página
	titulo_pagina = soup.title.string if soup.title else "Título não encontrado"
	print(f"📌 Título da página: {titulo_pagina}")
else:
	print(f"❌ Erro ao acessar o site. Código: {resposta.status_code}")