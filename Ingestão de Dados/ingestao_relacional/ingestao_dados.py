"""
Ingestão de dados em arquivo (csv) 
e bancos relacionais (mysql) e nosql (elasticsearch)
"""
from faker import Faker
import random
import pandas as pd
# pip install mysql-connector-python
import mysql.connector

MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rootpassword',
    'database': 'db_relacional'
}

def gerar_dados_funcionarios(num_funcionarios):
    """
    Gera uma lista de dicionários contendo dados falsos de funcionários
    """
    fake = Faker('pt_BR') # Usando o locale brasileiro
    departamentos = ['TI', 'Recursos Humanos', 'Vendas', 'Marketing', 'Financeiro']
    escolaridades = ['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Pós-Graduação']
    funcionarios = []
    for i in range(1, num_funcionarios + 1):
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')
        funcionario = {
            'id': i,
            'cpf': fake.cpf(),
            'nome': fake.name(),
            'data_nascimento': data_nascimento,
            'departamento': random.choice(departamentos),
            'escolaridade': random.choice(escolaridades),
            'cidade': fake.city()
        }
        funcionarios.append(funcionario)
    return funcionarios

def inserir_dados_em_csv(funcionarios_mock, nome_arquivo):
    """
    Cria um DataFrame do Pandas a partir dos dados e salva como arquivo CSV
    """
    try:
        df_funcionarios = pd.DataFrame(funcionarios_mock)
        df_funcionarios.to_csv(nome_arquivo, index=False, encoding='utf-8')
        print(f"Dados salvos com sucesso no arquivo CSV: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")

def inserir_dados_em_mysql(funcionarios_mock, nome_tabela):
    """
    Cria a tabela e insere os dados no banco de dados MySQL
    """
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        # 1. Cria a tabela (se não existir)
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id INT PRIMARY KEY,
            cpf VARCHAR(14) UNIQUE,
            nome VARCHAR(64),
            data_nascimento DATE,
            departamento VARCHAR(64),
            escolaridade VARCHAR(64),
            cidade VARCHAR(64)
        )
        """
        cursor.execute(create_table_query)
        # 2. Prepara a inserção
        insert_query = f"""
        INSERT INTO {nome_tabela} 
        (id, cpf, nome, data_nascimento, departamento, escolaridade, cidade)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            nome=VALUES(nome),
            data_nascimento=VALUES(data_nascimento),
            departamento=VALUES(departamento),
            escolaridade=VALUES(escolaridade),
            cidade=VALUES(cidade)
        """
        dados_para_insercao = [
            (d['id'], d['cpf'], d['nome'], d['data_nascimento'], 
            d['departamento'], d['escolaridade'], d['cidade'])
            for d in funcionarios_mock
        ]
        cursor.executemany(insert_query, dados_para_insercao)
        conn.commit()
        print(f"{cursor.rowcount} registros inseridos na tabela.")
    except mysql.connector.Error as err:
        print(f"Erro no MySQL: {err}")
    finally:
        cursor.close()
        conn.close()
    

if __name__ == '__main__':
    NUM_FUNCIONARIOS = 100
    NOME_ARQUIVO_CSV = 'funcionarios.csv'
    NOME_TABELA = 'funcionarios'
    NOME_INDICE = 'funcionarios_index'

    # 1. Gerar os dados (Mock)
    funcionarios_mock = gerar_dados_funcionarios(NUM_FUNCIONARIOS)
    # 2. Salvar dados em arquivo (CSV)
    inserir_dados_em_csv(funcionarios_mock, NOME_ARQUIVO_CSV)
    # 3. Salvar dados em banco relacional (MySQL)
    inserir_dados_em_mysql(funcionarios_mock, NOME_TABELA)