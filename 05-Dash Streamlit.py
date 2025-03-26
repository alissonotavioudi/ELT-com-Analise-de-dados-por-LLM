import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import psycopg2
from sklearn.cluster import KMeans

# Configuração do dashboard
st.set_page_config(page_title="📊 Dashboard de Análises de Clientes", layout="wide")
st.title("📊 Análises Avançadas dos Clientes")

# Função para carregar os dados do banco de dados
def load_data():
    query = """
        SELECT 
            c.nome AS Cliente,
            COUNT(p.id_compra) AS "Total Compras",
            SUM(pr.preco) AS "Total Gasto"
        FROM 
            operacoes.clientes c
        JOIN 
            operacoes.compras p ON c.id_cliente = p.id_cliente
        JOIN 
            operacoes.produtos pr ON p.id_produto = pr.id_produto
        GROUP BY 
            c.nome
        ORDER BY     
            "Total Gasto" DESC;
    """

    try:
        conn = psycopg2.connect(
            dbname=st.secrets["database"]["DB_NAME"],
            user=st.secrets["database"]["DB_USER"],
            password=st.secrets["database"]["DB_PASSWORD"],
            host=st.secrets["database"]["DB_HOST"],
            port=st.secrets["database"]["DB_PORT"]
        )
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    # 1️⃣ - Top 10 Clientes por Gasto
    df_sorted = df.sort_values(by="Total Gasto", ascending=False)
    st.subheader("🏆 Top Clientes por Gasto")
    st.dataframe(df_sorted)

    # 2️⃣ - Distribuição dos Gastos
    df["Faixa de Gasto"] = pd.qcut(df["Total Gasto"], q=4, labels=["Baixo", "Médio", "Alto", "Muito Alto"])
    fig_hist = px.histogram(df, x="Total Gasto", nbins=5, title="Distribuição de Gastos")
    st.plotly_chart(fig_hist, use_container_width=True)

    # 3️⃣ - Concentração de Receita
    df_sorted["% Acumulado"] = df_sorted["Total Gasto"].cumsum() / df_sorted["Total Gasto"].sum() * 100
    fig_pareto = px.line(df_sorted, x="cliente", y="% Acumulado", title="Concentração de Receita (Regra 80/20)")
    st.plotly_chart(fig_pareto, use_container_width=True)

    # 4️⃣ - Segmentação Automática (Clusters)
    X = df[["Total Compras", "Total Gasto"]]
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    df["Segmento"] = kmeans.labels_
    fig_clusters = px.scatter(df, x="Total Compras", y="Total Gasto", color="Segmento", title="Segmentação de Clientes")
    st.plotly_chart(fig_clusters, use_container_width=True)

    # 5️⃣ - Insights Adicionais
    st.sidebar.header("🔍 Filtro por Cliente")
    cliente = st.sidebar.selectbox("Selecione um Cliente", df["cliente"])
    cliente_info = df[df["cliente"] == cliente]
    st.sidebar.write(cliente_info)
else:
    st.warning("Nenhum dado foi carregado. Verifique a conexão com o banco.")