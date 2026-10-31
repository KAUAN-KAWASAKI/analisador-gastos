import matplotlib
matplotlib.use("Agg")

import pandas as pd
from grafico import grafico_categorias, grafico_mensal

def montar_df():
    df = pd.DataFrame({
        "data": pd.to_datetime(["2026-08-10", "2026-09-05"]),
        "valor": [-100.0, -200.0],
        "categoria": ["Alimentação", "Transporte"],
    })
    df["mes"] = df["data"].dt.to_period("M")
    return df

def test_grafico_categorias_salva_png(tmp_path):
    caminho = tmp_path / "categorias.png"
    grafico_categorias(montar_df(), caminho)
    assert caminho.exists() and caminho.stat().st_size > 0

def test_grafico_mensal_salva_png(tmp_path):
    caminho = tmp_path / "mensal.png"
    grafico_mensal(montar_df(), caminho)
    assert caminho.exists() and caminho.stat().st_size > 0
