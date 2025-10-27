def soma_pares(num):
    contador = 0

    for par in num:
        if par % 2 == 0:
            contador += par

    return contador