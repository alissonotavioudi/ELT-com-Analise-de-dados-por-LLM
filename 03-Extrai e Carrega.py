# Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados

# Python - Pipeline de Carga de Dados

# Imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Cria o motor de conexão 
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

print("\nIniciando o Processo de Carga dos Dados!\n")

# Função para carregar dados dos arquivos CSV para o PostgreSQL no schema especificado
def carrega_dados(csv_file, table_name, schema):

    # Bloco try/except
    try:

        # Lê o arquivo CSV
        df = pd.read_csv(csv_file)

        # Executa SQL a partir do dataframe do Pandas
        df.to_sql(table_name, engine, schema = schema, if_exists = 'append', index = False)
        print(f"Dados do arquivo {csv_file} foram inseridos na tabela {schema}.{table_name}.")

    except Exception as e:
        print(f"Erro ao inserir dados do arquivo {csv_file} na tabela {schema}.{table_name}: {e}")

# Carregamento dos dados no schema 'lab5'
carrega_dados('clientes.csv', 'clientes', 'operacoes')
carrega_dados('produtos.csv', 'produtos', 'operacoes')
carrega_dados('compras.csv', 'compras', 'operacoes')

print("\nCarga Executada com Sucesso! Use o pgAdmin Para Checar os Dados Se Desejar!\n")



