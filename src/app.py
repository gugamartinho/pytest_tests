def aplicar_desconto(preco, desconto):
    if desconto < 0:
        raise ValueError("O desconto não pode ser negativo")
    if desconto > 100:
        raise ValueError("O desconto não pode ser maior que 100%")

    return preco - (preco * desconto / 100)
