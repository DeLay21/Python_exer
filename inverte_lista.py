def inverte_lista(lista):
    lista_nova = []

    for ele in lista:
        lista_nova.insert(0,ele)

    print(lista_nova)

print(inverte_lista([1, 2, 3, 4, 5, 6]))