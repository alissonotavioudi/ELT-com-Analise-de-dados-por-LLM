--Analytics Engineering - Python, SQL e LLM Para Extrair Insights em Pipelines de Engenharia de Dados
-- SQL - Criação do Banco de Dados

-- Deleta o schema se já existir
DROP SCHEMA IF EXISTS operacoes CASCADE;

-- Cria o schema
CREATE SCHEMA operacoes AUTHORIZATION alisson;

-- Cria as tabelas

CREATE TABLE operacoes.clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(101),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE operacoes.produtos (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10, 2)
);

CREATE TABLE operacoes.compras (
    id_compra SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES operacoes.clientes(id_cliente),
    id_produto INTEGER REFERENCES operacoes.produtos(id_produto),
    data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
