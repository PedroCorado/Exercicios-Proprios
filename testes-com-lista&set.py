lista1 = [1, 2, 3, 4,4]
lista2 = [3, 4, 5, 6]

diferenca = [item for item in lista1 if item not in lista2]

print(diferenca)


diferenca_com_set = set(lista1) ^ set(lista2)
print(list(diferenca_com_set))