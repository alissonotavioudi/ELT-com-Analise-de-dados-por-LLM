import pandas as pd
from datetime import datetime
import random

# Lista de nomes e sobrenomes para gerar nomes aleatórios de clientes
nomes = ["João", "Maria", "Carlos", "Ana", "Lucas", "Fernanda", "Pedro", "Julia", "Gabriel", "Rafaela"]
sobrenomes = ["Silva", "Oliveira", "Pereira", "Costa", "Souza", "Lima", "Almeida", "Rodrigues", "Mendes", "Fernandes"]

# Lista de categorias para produtos
categorias_produtos = ["Eletrônicos", "Informática", "Cozinha", "Beleza", "Saúde", "Esportes", "Moda", "Livros", "Móveis", "Brinquedos"]

# Lista de nomes de produtos mais específicos
produtos_nomes = [
    "Smartphone", "Notebook", "Câmera", "Tablet", "Smartwatch", "Fone de Ouvido", "Teclado", "Mouse", 
    "Monitor", "Impressora", "Liquidificador", "Geladeira", "Máquina de Lavar", "Cafeteira", 
    "Máquina de Cortar Cabelo", "Escova de Dente Elétrica", "Tênis", "Blusa de Frio", "Livros", "Carrinho de Bebê"
]

# Função para gerar dados de clientes com nomes aleatórios
def gerar_clientes(num_clientes):
    clientes = []
    for i in range(1, num_clientes + 1):
        nome_cliente = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        email_cliente = f"{nome_cliente.replace(' ', '').lower()}@email.com"
        cliente = {
            "id_cliente": i,
            "nome": nome_cliente,
            "email": email_cliente,
            "criado_em": datetime(2020, random.randint(1, 12), random.randint(1, 28))
        }
        clientes.append(cliente)
    return clientes

# Função para gerar dados de produtos com nomes aleatórios
def gerar_produtos(num_produtos):
    produtos = []
    for i in range(1, num_produtos + 1):
        nome_produto = f"{random.choice(produtos_nomes)} ({random.choice(categorias_produtos)})"
        preco_produto = round(random.uniform(100, 5000), 2)
        produto = {
            "id_produto": i,
            "nome": nome_produto,
            "preco": preco_produto
        }
        produtos.append(produto)
    return produtos

# Função para gerar dados de compras
def gerar_compras(num_compras, num_clientes, num_produtos):
    compras = []
    for i in range(1, num_compras + 1):
        compra = {
            "id_compra": i,
            "id_cliente": random.randint(1, num_clientes),
            "id_produto": random.randint(1, num_produtos),
            "data_compra": datetime(2023, random.randint(1, 12), random.randint(1, 28))
        }
        compras.append(compra)
    return compras

# Definir o número de registros que você deseja gerar
num_clientes = 20
num_produtos = 10
num_compras = 40

# Gerar os dados
clientes_data = gerar_clientes(num_clientes)
produtos_data = gerar_produtos(num_produtos)
compras_data = gerar_compras(num_compras, num_clientes, num_produtos)

# Criar os DataFrames
clientes_df = pd.DataFrame(clientes_data)
produtos_df = pd.DataFrame(produtos_data)
compras_df = pd.DataFrame(compras_data)

# Salvar os arquivos CSV
clientes_df.to_csv('clientes_gerados.csv', index=False)
produtos_df.to_csv('produtos_gerados.csv', index=False)
compras_df.to_csv('compras_geradas.csv', index=False)

print("Arquivos 'clientes_extended.csv', 'produtos_extended.csv', e 'compras_extended.csv' gerados com sucesso!")
