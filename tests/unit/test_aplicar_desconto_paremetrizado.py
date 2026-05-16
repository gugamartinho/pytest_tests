from src.app import aplicar_desconto
import pytest

# Testes parametrizados para a função aplicar_desconto
@pytest.mark.parametrize(
    "preco, desconto, esperado",
    [
        (100, 20, 80),
        (100, 0, 100),
        (100, 100, 0),
        (0, 50, 0),
    ]
)
def test_aplicar_desconto_parametrizado(preco, desconto, esperado):
    assert aplicar_desconto(preco, desconto) == esperado

# Testes parametrizados para verificar erros na função aplicar_desconto
@pytest.mark.parametrize(
    "preco, desconto",
    [
        (100, -10),   # negativo
        (100, 150),   # maior que 100%
        (50, -1),     # negativo
        (80, 200),    # maior que 100%
    ]
)
def test_aplicar_desconto_parametrizado_erros(preco, desconto):
    with pytest.raises(ValueError):
        aplicar_desconto(preco, desconto)