# TEC-SLLKO-CD-N1-2025
EFG Sarah - Técnico em Ciência de Dados - Turma 2
ETL de Livros
Este projeto demonstra o uso do Apache Airflow para construir duas pipelines de ETL (Extração, Transformação e Carga) que movem dados de livros entre diferentes sistemas.
Nosso objetivo é mostrar como orquestrar o fluxo de dados do CSV para o PostgreSQL e, em seguida, para o Elasticsearch.

Arquivos localizados em: Docker > Airflow > dags

dados:
	Contém o CSV do arquivo para importar os dados dos livros
  
dag_elasticsearch:
Contém as tarefas de salvar os registros do Postgres no Elasticsearch.
dag_postgres: 
Contém as tarefas de salvar os registros do arquivo CSV no Postgres.
	
funções_helper:
Contém as funções python
  funcoes_elasticsearch:
  Contém as funções de salvar os registros do Postgres no Elasticsearch.
  funcoes_postgres:
  Contém as funções de salvar os registros do arquivo CSV no Postgres.