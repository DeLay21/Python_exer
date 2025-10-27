def caixa(texto):
    tamanho = len(texto)

    largura_cima = '+' + '-' * (tamanho) + '+'
    meio = '|' + '' + texto + '' +'|'
    largura_baixo = '+' + '-' * (tamanho) + '+'

    print(largura_cima)
    print(meio)
    print(largura_baixo)

caixa('pyhton')