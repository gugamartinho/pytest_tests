from src.app import aplicar_desconto
import pytest

def test_aplicar_desconto_com_fixture(preco_base):
    assert aplicar_desconto(preco_base, 20) == 80
