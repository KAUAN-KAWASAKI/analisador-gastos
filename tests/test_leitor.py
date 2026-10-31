import pandas as pd
from leitor import ler_extrato

def test_ler_extrato_converte_tipos_e_cria_mes(tmp_path):
    csv = tmp_path / "extrato.csv"
    csv.write_text("data,descricao,valor\n2026-08-03,SALARIO,3200.00\n2026-09-04,ALUGUEL,-1100.00\n")
    df = ler_extrato(csv)
    assert pd.api.types.is_datetime64_any_dtype(df["data"])
    assert df["valor"].dtype == "float64"
    assert list(df["mes"].astype(str)) == ["2026-08", "2026-09"]
