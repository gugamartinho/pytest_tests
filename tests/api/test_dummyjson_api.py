import pytest


def test_listar_produtos(api):
    resposta = api.get(api.base_url + "/products")

    #print("STATUS:", resposta.status_code)
    #print("JSON:", resposta.json())

    assert resposta.status_code == 200
    dados = resposta.json()
    assert "products" in dados

def test_obter_produto_por_id(api):
    resposta = api.get(api.base_url + "/products/1")
    #print("STATUS:", resposta.status_code)
    #print("JSON:", resposta.json())

    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["id"] == 1
    assert "title" in dados

def test_obter_produto_inexistente(api):
    resposta = api.get(api.base_url + "/products/99999")

    #print("STATUS:", resposta.status_code)
    #print("JSON:", resposta.json())

    assert resposta.status_code == 404

@pytest.mark.parametrize("produto_id", [1, 2, 3, 4, 5])
def test_produtos_multiplos(api, produto_id):
    resposta = api.get(f"{api.base_url}/products/{produto_id}")
    assert resposta.status_code == 200
    assert resposta.json()["id"] == produto_id


def test_criar_produto(api):
    payload = {
        "title": "Produto QA",
        "price": 99
    }

    resposta = api.post(api.base_url + "/products/add", json=payload)

    #print("STATUS:", resposta.status_code)
    #print("JSON:", resposta.json())

    assert resposta.status_code == 201
    dados = resposta.json()
    assert dados["title"] == "Produto QA"
    assert dados["price"] == 99

def test_schema_produto(api):
    resposta = api.get(api.base_url + "/products/1")
    dados = resposta.json()

    campos_esperados = ["id", "title", "description", "price", "rating"]

    for campo in campos_esperados:
        assert campo in dados
