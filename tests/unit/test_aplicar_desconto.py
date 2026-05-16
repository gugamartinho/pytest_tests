from src.app import aplicar_desconto
import pytest

def test_aplicar_desconto_20_porcento():
    assert aplicar_desconto(100, 20) == 80.0

def test_aplicar_desconto_zero_porcento():
    assert aplicar_desconto(100, 0) == 100

def test_aplicar_desconto_cem_porcento():
    assert aplicar_desconto(100, 100) == 0.0

def test_aplicar_desconto_50_porcento():
    assert aplicar_desconto(200, 50) == 100.0

def test_aplicar_desconto_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(100, -10)

def test_aplicar_desconto_maior_que_cem_porcento():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)