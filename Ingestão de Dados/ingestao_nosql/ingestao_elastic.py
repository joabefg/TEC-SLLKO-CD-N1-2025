import requests
# Adicionar a importação para o cliente Elasticsearch
from elasticsearch import Elasticsearch
import time # Para gerar um ID único para o documento

def buscar_isbn_livro_by_titulo(url):
    """
    Buscar o ISBN do livro usando o título
    """
    # ... (código existente da função)

    url_base = "https://www.googleapis.com/books/v1/volumes"
    url_completa = f"{url_base}?q={url.replace(' ', '+')}"
    # url_completa = f"{url_base}?q=intitle:{url.replace(' ', '+')}" # Opção para buscar apenas no título

    try:
        resposta = requests.get(url_completa)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.RequestException as re:
        print(f"Ocorreu um erro na Requisição (requests): {re}")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado (requests): {e}")
        return

    if 'items' not in dados or not dados['items']:
        print("Nenhum resultado encontrado para a pesquisa.")
        return

    # Usar o primeiro item encontrado para simplificar
    item = dados['items'][0] 
    titulo = item.get('volumeInfo', {}).get('title', 'Título não encontrado')
    industry_ids = item.get('volumeInfo', {}).get('industryIdentifiers', [])

    isbn_13 = "Não encontrado"
    isbn_10 = "Não encontrado"

    for identificador in industry_ids:
        if identificador.get('type') == 'ISBN_13':
            isbn_13 = identificador.get('identifier')
        if identificador.get('type') == 'ISBN_10':
            isbn_10 = identificador.get('identifier')
            
    print(f"Livro: {titulo}")
    print(f"ISBN 13: {isbn_13}")
    print(f"ISBN 10: {isbn_10}\n")
    
    # ----------------------------------------------------------------------
    # NOVO CÓDIGO: Salvar no Elasticsearch
    # ----------------------------------------------------------------------
    
    # Configurações do Elasticsearch
    ES_HOST = "http://localhost:9200"
    ES_INDEX = "book_isbns" # Nome do índice
    
    try:
        # 1. Conectar ao Elasticsearch
        # Se você estiver usando uma versão recente do Elastic e tiver autenticação/SSL
        # ativados no seu contêiner Docker (o que é comum), pode ser necessário
        # fornecer `basic_auth`, `ca_certs` ou desativar o SSL se estiver usando HTTP.
        # Estamos usando a conexão simples HTTP para localhost:9200, que é comum
        # para testes locais sem segurança ativada.
        es = Elasticsearch(ES_HOST)
        
        # Opcional: Verificar a conexão
        if not es.ping():
             raise ValueError("A conexão com o Elasticsearch falhou!")
             
        # 2. Preparar o documento
        documento = {
            'title': titulo,
            'isbn_13': isbn_13,
            'isbn_10': isbn_10,
            'timestamp': int(time.time()) # Adicionar um timestamp para ordenar
        }
        
        # 3. Indexar o documento
        # Usamos o título do livro para gerar um ID do documento.
        # Para evitar problemas com caracteres especiais, podemos usar um hash ou a biblioteca
        # 'slugify', mas para este exemplo, usamos o ID gerado automaticamente.
        # response = es.index(index=ES_INDEX, document=documento)
        
        # Para garantir um ID único se o título for o mesmo, usamos o timestamp:
        # Gerar um ID baseado no título + timestamp
        doc_id = f"{titulo.replace(' ', '-').lower()}-{int(time.time())}"
        
        # Se preferir um ID gerado pelo Elasticsearch, comente a linha acima e use:
        response = es.index(index=ES_INDEX, document=documento) 
        
        print(f"✅ Dados salvos com sucesso no Elasticsearch (Índice: {ES_INDEX})")
        # print(f"ID do Documento: {response['_id']}, Resultado: {response['result']}") # Se você quiser ver a resposta
        
    except ValueError as ve:
        print(f"❌ Erro de Conexão com Elasticsearch: {ve}")
    except Exception as e:
        print(f"❌ Ocorreu um erro ao salvar no Elasticsearch: {e}")
        
    # ----------------------------------------------------------------------
    # FIM DO NOVO CÓDIGO
    # ----------------------------------------------------------------------

# Chama a função principal
nome_livro = "O Senhor dos Anéis"
buscar_isbn_livro_by_titulo(nome_livro)