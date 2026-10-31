# analise.py
from leitor import ler_extrato
from categorias import adicionar_categoria

def gastos_por_mes(df):
    gastos = df[df["valor"] < 0]
    return gastos.groupby("mes")["valor"].sum().abs()

def gastos_por_categoria(df):
    gastos = df[df["valor"] < 0]
    return gastos.groupby("categoria")["valor"].sum().abs().sort_values(ascending=False)

def gastos_por_mes_e_categoria(df):
    gastos = df[df["valor"] < 0]
    return gastos.groupby(["mes", "categoria"])["valor"].sum().abs().unstack(fill_value=0)

if __name__ == "__main__":
    df = ler_extrato("dados/exemplo.csv")
    df = adicionar_categoria(df)
    print(gastos_por_mes(df))
    print(gastos_por_categoria(df))
    print(gastos_por_mes_e_categoria(df))
