def substituir_vogais(palavra):
    palavra = palavra.lower()
    vogais = 'aeiou'
    palavra_nova = ''

    for letras in palavra:
        if letras in vogais:
            palavra_nova += '*'
        else:
            palavra_nova += letras

    return palavra_nova

print(substituir_vogais('banana'))