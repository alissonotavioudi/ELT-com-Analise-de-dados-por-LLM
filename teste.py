import psycopg2
import pandas as pd

def extrai_dados(caminhos_arquivos):
    try:
        dados = {}
        for nome_arquivo, caminho in caminhos_arquivos.items():
            dados[nome_arquivo] = pd.read_csv(caminho)
            print(f"Dados extraídos com sucesso do arquivo {caminho}.")
        return dados
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return None

# Função para carregar dados no banco de dados PostgreSQL
def carrega_dados(dados, conn_params):
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        # Mapeamento dos arquivos para as tabelas correspondentes
        tabela_mapeamento = {
            'clientes.csv': 'clientes',
            'produtos.csv': 'produtos',
            'compras.csv': 'compras'
        }

        for nome_arquivo, df in dados.items():
            tabela = tabela_mapeamento.get(nome_arquivo)

            if tabela:
                # Criando placeholders para os valores (ex: %s, %s, %s)
                placeholders = ', '.join(['%s'] * len(df.columns))
                colunas = ', '.join(df.columns)

                # Query parametrizada para evitar SQL Injection
                insert_query = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

                # Convertendo o DataFrame para uma lista de tuplas para a inserção em lote
                valores = [tuple(row) for row in df.itertuples(index=False, name=None)]

                # Inserindo em lote com executemany para maior eficiência
                cursor.executemany(insert_query, valores)

        conn.commit()
        cursor.close()
        conn.close()
        print("Dados carregados com sucesso nas tabelas.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

# Parâmetros de conexão com o banco de dados PostgreSQL
conn_params = {
    'dbname': 'db',
    'user': 'alisson',
    'password': 'alisson',
    'host': 'localhost',
    'port': '5959'
}

# Caminhos dos arquivos CSV
caminhos_arquivos = {
    'clientes.csv': r'C:\Users\tavin\OneDrive\Área de Trabalho\Projetos - Alisson\clientes.csv',  # Caminho para o arquivo clientes.csv
    'produtos.csv': r'C:\Users\tavin\OneDrive\Área de Trabalho\Projetos - Alisson\produtos.csv',  # Caminho para o arquivo produtos.csv
    'compras.csv': r'C:\Users\tavin\OneDrive\Área de Trabalho\Projetos - Alisson\compras.csv'     # Caminho para o arquivo compras.csv
    
}

# Executando ETL
dados_extraidos = extrai_dados(caminhos_arquivos)
if dados_extraidos is not None:
    carrega_dados(dados_extraidos, conn_params)