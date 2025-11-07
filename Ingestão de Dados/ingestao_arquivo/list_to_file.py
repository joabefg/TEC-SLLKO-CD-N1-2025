import csv

# 1. Defina a lista de alunos (dados).
# Cada dicionário representa um aluno, e as chaves são os nomes das colunas.
alunos = [
    {'Nome': 'Ana Silva', 'Idade': 20, 'Curso': 'Engenharia de Software'},
    {'Nome': 'Bruno Costa', 'Idade': 22, 'Curso': 'Ciência da Computação'},
    {'Nome': 'Carla Souza', 'Idade': 19, 'Curso': 'Design Gráfico'},
    {'Nome': 'Daniel Pereira', 'Idade': 21, 'Curso': 'Administração'}
]

# 2. Defina o nome do arquivo CSV e os cabeçalhos (fieldnames).
nome_arquivo = 'lista_de_alunos.csv'
# Estes devem corresponder às chaves nos dicionários de alunos.
cabecalhos = ['Nome', 'Idade', 'Curso']

# 3. Abra e escreva no arquivo CSV.
try:
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        # Crie um objeto DictWriter (escritor de dicionário)
        # Ele mapeia os dicionários Python para linhas CSV.
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)

        # Escreva a primeira linha com os cabeçalhos das colunas
        escritor_csv.writeheader()

        # Escreva os dados de cada aluno
        escritor_csv.writerows(alunos)

    print(f"Sucesso! A lista de alunos foi salva em '{nome_arquivo}'.")

except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")

# Exemplo de conteúdo do arquivo lista_de_alunos.csv:
# Nome,Idade,Curso
# Ana Silva,20,Engenharia de Software
# Bruno Costa,22,Ciência da Computação
# Carla Souza,19,Design Gráfico
# Daniel Pereira,21,Administração