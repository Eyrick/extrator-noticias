import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

# URL do site de notícias (G1 - Tecnologia)
url = "https://g1.globo.com/tecnologia/"

# Headers para simular um navegador real
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
    
    soup = BeautifulSoup(resposta.text, 'html.parser')
    manchetes = soup.find_all('a', class_='feed-post-link')
    
    print(f"🔍 Encontrados {len(manchetes)} elementos com a classe 'feed-post-link'")
    print("-" * 60)
    
    noticias = []
    for i, manchete in enumerate(manchetes[:10], 1):
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

def salvar_em_csv(noticias, nome_arquivo="noticias_g1.csv"):
    """
    Salva a lista de notícias em um arquivo CSV.
    Adiciona a data/hora da extração em cada linha.
    """
    if not noticias:
        print("⚠️ Nenhuma notícia para salvar.")
        return
    
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Abre o arquivo para escrita (cria se não existir)
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        
        # Cabeçalho
        escritor.writerow(['Data/Hora', 'Título', 'Link'])
        
        # Dados
        for noticia in noticias:
            escritor.writerow([data_hora, noticia['titulo'], noticia['link']])
    
    print(f"\n💾 Dados salvos em '{nome_arquivo}'")

def salvar_relatorio_txt(noticias, nome_arquivo="relatorio_noticias.txt"):
    """
    Salva um relatório legível em formato TXT.
    """
    if not noticias:
        return
    
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("RELATÓRIO DE NOTÍCIAS - G1 TECNOLOGIA\n")
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"Data da extração: {data_hora}\n")
        arquivo.write(f"Total de notícias extraídas: {len(noticias)}\n")
        arquivo.write("-" * 50 + "\n\n")
        
        for i, noticia in enumerate(noticias, 1):
            arquivo.write(f"{i}. {noticia['titulo']}\n")
            arquivo.write(f"   Link: {noticia['link']}\n\n")
    
    print(f"📄 Relatório salvo em '{nome_arquivo}'")

def main():
    print("=" * 60)
    print("📰 EXTRATOR DE NOTÍCIAS - G1 TECNOLOGIA")
    print("=" * 60)
    print(f"⏰ Data/Hora da extração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    
    noticias = extrair_noticias_g1()
    
    if noticias:
        print(f"\n✅ Extração concluída! {len(noticias)} notícias capturadas.")
        
        # Salva os arquivos
        salvar_em_csv(noticias)
        salvar_relatorio_txt(noticias)
        
        # Exibe o caminho absoluto dos arquivos
        caminho_csv = os.path.abspath("noticias_g1.csv")
        caminho_txt = os.path.abspath("relatorio_noticias.txt")
        print(f"\n📂 Os arquivos foram salvos em:")
        print(f"   CSV: {caminho_csv}")
        print(f"   TXT: {caminho_txt}")
    else:
        print("\n⚠️ Nenhuma notícia encontrada.")

if __name__ == "__main__":
    main()