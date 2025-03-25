# Analytics Engineering - Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados
# Python - Pipeline de Extração de Insights com LLM

# Imports
import csv
import psycopg2
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

print("\nIniciando o Processo de Extração de Insights...\n")

# Instanciação do LLM Llama3 através do Ollama
print("Carregando modelo Llama3.1 no Ollama...")
llm = OllamaLLM(model="llama3.1")
print("Modelo carregado com sucesso!\n")

# Criação do parser para a saída do modelo de linguagem
output_parser = StrOutputParser()

# Função para gerar texto baseado nos dados do PostgreSQL
def gera_insights():

    print("Conectando ao banco de dados PostgreSQL...")
    try:
        # Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
        conn = psycopg2.connect(
            dbname="db",
            user="alisson",
            password="alisson",
            host="localhost",
            port="5959"
        )
        print("Conexão estabelecida com sucesso!\n")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return []

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()
    
    print("Executando consulta SQL para extrair dados dos clientes, compras e produtos...")
    # Define a consulta SQL para obter dados dos clientes, compras e produtos
    query = """
        SELECT 
            c.nome,
            COUNT(p.id_compra) AS total_compras,
            SUM(pr.preco) AS total_gasto
        FROM 
            operacoes.clientes c
        JOIN 
            operacoes.compras p ON c.id_cliente = p.id_cliente
        JOIN 
            operacoes.produtos pr ON p.id_produto = pr.id_produto
        GROUP BY 
            c.nome
        ORDER BY     
            total_gasto DESC;
    """
    
    try:
        # Executa a consulta SQL
        cursor.execute(query)
        print("Consulta executada com sucesso!\n")
    except Exception as e:
        print(f"Erro ao executar consulta SQL: {e}")
        conn.close()
        return []

    # Obtém todos os resultados da consulta
    rows = cursor.fetchall()
    
    print(f"{len(rows)} registros encontrados na consulta SQL.\n")

    # Inicializa uma lista para armazenar os insights
    insights = []

    # Criação do template de prompt para o chatbot
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um analista de dados especializado. Analise os dados sobre os padrões de compras dos clientes e forneça feedback em português do Brasil."),
            ("user", "question: {question}")
        ]
    )

    # Definição da cadeia de execução: prompt -> LLM -> output_parser
    chain = prompt | llm | output_parser

    # Itera sobre as linhas de resultados
    for index, row in enumerate(rows):
        # Desempacota os valores de cada linha
        name, total_purchases, total_spent = row

        print(f"Gerando insight {index + 1}/{len(rows)} para o cliente {name}...")

        # Cria o prompt para o LLM com base nos dados do cliente
        consulta_cliente = f"Cliente {name} fez {total_purchases} compras totalizando ${total_spent:.2f}."

        try:
            # Gera o texto de insight usando o LLM
            response = chain.invoke({'question': consulta_cliente})
            print(f"Insight gerado para {name}!\n")
        except Exception as e:
            print(f"Erro ao gerar insight para {name}: {e}")
            response = "Erro ao gerar insight."

        # Adiciona o texto gerado à lista de insights
        insights.append(response)
    
    # Fecha a conexão com o banco de dados
    conn.close()
    print("Conexão com o banco de dados encerrada.\n")

    # Salva os insights em um arquivo CSV
    print("Salvando insights no arquivo insights.csv...")
    try:
        with open('insights.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Insight"])
            for insight in insights:
                writer.writerow([insight])
        print("Insights salvos com sucesso!\n")
    except Exception as e:
        print(f"Erro ao salvar insights no arquivo CSV: {e}")

    # Retorna a lista de insights
    return insights

# Gera insights chamando a função definida
insights = gera_insights()

print("\nProcesso de Extração de Insights Finalizado!\n")

# Imprime cada insight gerado
for insight in insights:
    print(insight)
