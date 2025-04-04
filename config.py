from dotenv import load_dotenv
import os

# Carregar o .env uma vez
load_dotenv()

# Expor as variáveis de ambiente como constantes
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")