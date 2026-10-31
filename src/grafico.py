# grafico.py
import os
import matplotlib.pyplot as plt
from leitor import ler_extrato
from categorias import adicionar_categoria
from analise import gastos_por_categoria, gastos_por_mes_e_categoria

def grafico_categorias(df, caminho):
    serie = gastos_por_categoria(df)
    fig, ax = plt.subplots(figsize=(10, 6))
    serie.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Gastos por categoria")
    ax.set_xlabel("Total gasto (R$)")
    ax.set_ylabel("Categoria")
    fig.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close(fig)

def grafico_mensal(df, caminho):
    tabela = gastos_por_mes_e_categoria(df)
    tabela.index = tabela.index.astype(str)
    fig, ax = plt.subplots(figsize=(10, 6))
    tabela.plot(kind="bar", stacked=True, ax=ax, colormap="tab20")
    ax.set_title("Gastos por mês e categoria")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Total gasto (R$)")
    ax.tick_params(axis="x", rotation=0)
    ax.legend(title="Categoria", bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close(fig)

if __name__ == "__main__":
    df = ler_extrato("dados/exemplo.csv")
    df = adicionar_categoria(df)
    os.makedirs("img", exist_ok=True)
    grafico_categorias(df, "img/gastos_por_categoria.png")
    grafico_mensal(df, "img/gastos_por_mes.png")
