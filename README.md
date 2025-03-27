# ELT com Análise de Dados por LLM

Este projeto demonstra um pipeline completo de **Extração, Carga e Transformação (ELT)** de dados, integrando técnicas de análise avançada utilizando **Modelos de Linguagem de Grande Escala (LLM)**. O objetivo é fornecer insights valiosos a partir de dados extraídos e transformados, culminando em um dashboard interativo para visualização.

## Visão Geral

O fluxo do projeto é estruturado nas seguintes etapas:

1. **Criação do Banco de Dados e Tabelas**: Configuração inicial do ambiente de banco de dados.
2. **Geração e Carga de Dados**: Produção de dados fictícios e inserção no banco de dados.
3. **Transformação e Análise com LLM**: Processamento dos dados e geração de insights utilizando LLM.
4. **Visualização com Streamlit**: Desenvolvimento de um dashboard interativo para apresentação dos insights.

## Estrutura do Projeto

- `01-Cria_DB_Tabelas.sql`: Script SQL para criação do banco de dados e tabelas necessárias.
- `02-CriaDB.py`: Script Python para conexão ao banco de dados e execução do script SQL.
- `03-Extrai_e_Carrega.py`: Realiza a extração de dados de uma API simulada e carrega no banco de dados.
- `04-Transforma_dados_e_Gera_Insights_LLM.py`: Processa os dados e utiliza um LLM para gerar insights.
- `05-Dash_Streamlit.py`: Implementa um dashboard interativo utilizando Streamlit para visualização dos insights.
- `06-Executa_Pipeline_e_gera_Dash.py`: Script que orquestra a execução de todo o pipeline e inicia o dashboard.
- `Gera_dados_aleatorios.py`: Gera dados fictícios para simular a extração de uma API.
- `config.py`: Arquivo de configuração com parâmetros do banco de dados.
- `insights.csv`: Arquivo CSV gerado contendo os insights produzidos pelo LLM.
- `requirements.txt`: Lista de dependências necessárias para o projeto.

## Funcionalidades

- **Automatização do Pipeline ELT**: Desde a extração de dados até a visualização, todo o processo é automatizado.
- **Geração de Insights com LLM**: Utilização de modelos de linguagem para análise e extração de insights dos dados.
- **Dashboard Interativo**: Visualização dos insights através de um dashboard desenvolvido com Streamlit.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento dos scripts.
- **PostgreSQL**: Banco de dados utilizado para armazenamento dos dados.
- **Docker**: Para containerização do banco de dados PostgreSQL.
- **Streamlit**: Framework para criação do dashboard interativo.
- **LangChain + Ollama**: Integração com modelos de linguagem para análise de dados.

## Como Executar o Projeto

1️⃣ Instale as Dependências  

pip install -r requirements.txt

2️⃣ Configure o Banco de Dados no Docker

Caso ainda não tenha um banco PostgreSQL rodando, execute o seguinte comando para criar um container com a instância do banco:

docker run --name pipeline_com_ia-sql-python-llm -p 5959:5432 -e POSTGRES_USER=seu_usuario -e POSTGRES_PASSWORD=sua_senha -e POSTGRES_DB=db -d postgres:16.1

📌 Nota: Lembre-se de alterar os valores POSTGRES_USER e POSTGRES_PASSWORD conforme sua preferência e de atualizar config.py com essas credenciais.

3️⃣ Instale o Ollama

Baixe e instale o Ollama a partir do site oficial (utilizado a versão 3.1).

Após a instalação, execute o comando abaixo para verificar se o modelo está disponível:

ollama run llama3.1

4️⃣ Execute o Pipeline e Dashboard

Agora, basta rodar o seguinte comando para executar o pipeline e iniciar o dashboard:

python "06-Executa Pipeline e gera Dash.py"

Isso irá:

✅ Processar os dados
✅ Gerar insights com o LLM
✅ Disponibilizar um dashboard interativo

⚠️ Observações Importantes

🔹 Certifique-se de que o banco de dados PostgreSQL esteja rodando no Docker antes de executar os scripts.
🔹 O projeto utiliza dados fictícios para fins de demonstração.
🔹 Para uma análise mais aprofundada, recomenda-se a utilização de um LLM adequado e devidamente configurado.

🤝 Contribuições

Contribuições são muito bem-vindas! 🚀
Sinta-se à vontade para abrir issues ou enviar pull requests.

📜 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
