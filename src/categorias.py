# categorias.py
from leitor import ler_extrato

CATEGORIAS = {
    "Renda": ["SALARIO"],
    "Alimentação": ["IFOOD", "SUPERMERCADO", "PADARIA", "RESTAURANTE"],
    "Transporte": ["UBER", "99APP", "POSTO"],
    "Saúde": ["UNIMED", "DROGARIA", "DROGASIL", "LABORATORIO", "ODONTOPREV"],
    "Seguros": ["SEGURO"],
    "Moradia": ["ALUGUEL", "CONDOMINIO", "AGUA", "ENERGIA", "INTERNET"],
    "Assinaturas": ["NETFLIX", "SPOTIFY"],
    "Impostos": ["IPVA", "DETRAN"],
    "Lazer": ["CINEMARK", "SMART FIT"],
    "Compras": ["AMAZON", "MERCADO LIVRE", "LIVRARIA"],
    "Taxas": ["TARIFA"],
    "Transferências": ["PIX ENVIADO"],
}

def categorizar(descricao):
    for categoria, palavras in CATEGORIAS.items():
        for palavra in palavras:
            if palavra in descricao.upper():
                return categoria
    return "Outros"

def adicionar_categoria(df):
    df["categoria"] = df["descricao"].apply(categorizar)
    return df

if __name__ == "__main__":
    df = ler_extrato("dados/exemplo.csv")
    df = adicionar_categoria(df)
    print(df[df["categoria"] == "Outros"])
