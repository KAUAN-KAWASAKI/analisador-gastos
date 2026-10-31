# analise.py
from leitor import ler_extrato

def gastos_por_mes(df):
    gastos = df[df["valor"] < 0]
    return gastos.groupby("mes")["valor"].sum().abs()

if __name__ == "__main__":
    df = ler_extrato("dados/exemplo.csv")
    print(gastos_por_mes(df))
