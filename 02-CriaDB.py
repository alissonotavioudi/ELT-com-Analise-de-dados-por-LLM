# Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados

# Python - Pipeline de Criação do Banco de Dados

import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Função para executar script SQL
def executa_script_sql(filename):
    
# Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
    conn = psycopg2.connect(
       dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Abre um cursor para realizar operações no banco de dados
    cur = conn.cursor()

    # Lê o conteúdo do arquivo SQL
    with open(filename, 'r') as file:
        sql_script = file.read()

    try:
        # Executa o script SQL
        cur.execute(sql_script)

        # Confirma as mudanças no banco de dados
        conn.commit()  
        print("\nScript executado com sucesso!\n")
    except Exception as e:
        # Reverte as mudanças em caso de erro
        conn.rollback()  
        print(f"Erro ao executar o script: {e}")
    finally:
        # Fecha a comunicação com o banco de dados
        cur.close()
        conn.close()

# Executa o script SQL
executa_script_sql('01-Cria_DB_Tabelas.sql')
