# Projeto de Testes Automatizados com Pytest

## Estrutura

├── src
│   ├── app.py
│   └── __init__.py
├── testes_pytest.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
└── tests
    ├── fixtures
    │   └── conftest.py
    ├── helpers
    ├── integration
    └── unit
        ├── test_aplicar_desconto_fixtures.py
        ├── test_aplicar_desconto_paremetrizado.py
        └── test_aplicar_desconto.py
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt


## Instalação
### Criar e ativar ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Instalar dependências
```bash
pip install -r requirements.txt
```
### Instalar o projeto localmente
```bash
pip install -e .
```


### Execução dos testes
```bash
pytest
```

## Dependências

- Python 3.10 ou superior
- Pytest 8.2.0
- Ambiente virtual recomendado (`python3 -m venv .venv`)
- Instalação do pacote local via `pip install -e .`

Estas versões garantem compatibilidade total com o projeto e evitam erros de import ou execução.

---

## 💡 Notas Importantes

- Corre sempre os testes a partir da **raiz do projeto**.
- A pasta `src/` deve conter um ficheiro `__init__.py` para ser reconhecida como pacote Python.
- O ficheiro `pyproject.toml` permite instalar o projeto em modo desenvolvimento e garante que o Pytest encontra o módulo `src`.
- O comando `pip install -e .` é obrigatório para que os imports funcionem em qualquer máquina.

## Autor

Projeto mantido por **David Martinho**.

## Licença

Este projeto é disponibilizado para fins educativos e de demonstração.  
Pode ser adaptado e reutilizado livremente em ambientes internos ou de formação.
