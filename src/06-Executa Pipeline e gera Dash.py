# Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados

# Python - Executa o Pipeline

# Imports
import subprocess

# Função para executar outros scripts Python
def run_pipeline(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True, capture_output=True, text=True)
        print(f"\nScript {script_name} executado com sucesso.")
        print("\nSaída:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"\nErro ao executar o script {script_name}.")
        print("\nErro:\n", e.stderr)

# Lista de scripts
scripts = [
    'src/02-CriaDB.py',
    'src/03-Extrai e Carrega.py',
    'src/04-Transforma dados e Gera Insights LLM.py']

# Executa os scripts em um loop
for script in scripts:
    run_pipeline(script)


print(f"\nPipeline executado com sucesso.\n")


# Inicia o Streamlit
print("\nIniciando o Dashboard no Streamlit...\n")
subprocess.run([r"C:\Users\tavin\OneDrive\Área de Trabalho\Projetos - Alisson\venv\Scripts\streamlit.exe", "run", "src/05-Dash Streamlit.py"], check=True)
