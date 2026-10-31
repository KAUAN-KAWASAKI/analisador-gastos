import pandas as pd
from analise import gastos_por_mes, gastos_por_categoria, gastos_por_mes_e_categoria

def montar_df():
    df = pd.DataFrame({
        "data": ["2026-08-01", "2026-08-10", "2026-08-15", "2026-09-05"],
        "valor": [3000.0, -100.0, -50.0, -200.0],
        "categoria": ["Renda", "Alimentação", "Transporte", "Alimentação"],
    })
    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = df["data"].dt.to_period("M")
    return df

def test_gastos_por_mes_ignora_valor_positivo():
    resultado = gastos_por_mes(montar_df())
    assert resultado[pd.Period("2026-08")] == 150.0
    assert resultado[pd.Period("2026-09")] == 200.0

def test_gastos_por_categoria_ordenado_do_maior_para_o_menor():
    resultado = gastos_por_categoria(montar_df())
    assert list(resultado.index) == ["Alimentação", "Transporte"]
    assert resultado["Alimentação"] == 300.0

def test_gastos_por_mes_e_categoria_preenche_zero():
    tabela = gastos_por_mes_e_categoria(montar_df())
    assert tabela.loc[pd.Period("2026-09"), "Transporte"] == 0
    assert tabela.loc[pd.Period("2026-08"), "Alimentação"] == 100.0
