# Analytics Engineering - Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados
# Python - Pipeline de Criação do Banco de Dados

# Import
import psycopg2

# Função para executar script SQL
def executa_script_sql(filename):
    
    from dotenv import load_dotenv
    import os
    import psycopg2

    load_dotenv()

    # Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
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
