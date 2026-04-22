import requests
from bs4 import BeautifulSoup

# URL do site de notícias (G1 - Tecnologia)
url = "https://g1.globo.com/tecnologia/"

# Headers para simular um navegador real (evita bloqueio)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def extrair_noticias_g1():
    """
    Acessa o G1 Tecnologia e extrai as manchetes e links das notícias.
    """
    print("🌐 Acessando o site...")
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code != 200:
        print(f"❌ Erro ao acessar o site. Código: {resposta.status_code}")
        return []
    
    print("✅ Site acessado com sucesso!")
    
    # Cria o objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Procura por todos os links que tem a classe 'feed-post-link'
    # Essa classe é padrão das manchetes do G1
    manchetes = soup.find_all('a', class_='feed-post-link')
    
    print(f"🔍 Encontrados {len(manchetes)} elementos com a classe 'feed-post-link'")
    print("-" * 60)
    
    noticias = []
    for i, manchete in enumerate(manchetes[:10], 1):  # Pega só as 10 primeiras
        titulo = manchete.get_text().strip()
        link = manchete.get('href')
        
        if titulo and link:
            noticias.append({
                'titulo': titulo,
                'link': link
            })
            print(f"{i}. {titulo}")
            print(f"   🔗 {link}\n")
    
    return noticias

def main():
    print("=" * 60)
    print("📰 EXTRATOR DE NOTÍCIAS - G1 TECNOLOGIA")
    print("=" * 60)
    
    noticias = extrair_noticias_g1()
    
    if noticias:
        print(f"\n✅ Extração concluída! {len(noticias)} notícias capturadas.")
    else:
        print("\n⚠️ Nenhuma notícia encontrada. O site pode ter mudado o layout.")

if __name__ == "__main__":
    main()