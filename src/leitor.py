# leitor.py
import pandas as pd

def ler_extrato(caminho):
    df = pd.read_csv(caminho)
    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = df["data"].dt.to_period("M")
    return df

if __name__ == "__main__":
    df = ler_extrato("dados/exemplo.csv")
    print(df.head())
    print(df.dtypes)
