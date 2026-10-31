from categorias import categorizar

def test_alimentacao():
    assert categorizar("IFOOD *PIZZARIA") == "Alimentação"

def test_transporte():
    assert categorizar("UBER *TRIP") == "Transporte"

def test_renda():
    assert categorizar("PIX RECEBIDO EMPRESA XYZ LTDA SALARIO") == "Renda"

def test_descricao_desconhecida_vira_outros():
    assert categorizar("LOJA QUALQUER 123") == "Outros"

def test_ignora_maiusculas_e_minusculas():
    assert categorizar("netflix.com") == "Assinaturas"

def test_ordem_importa():
    assert categorizar("UNIMED SEGURO SAUDE") == "Saúde"
