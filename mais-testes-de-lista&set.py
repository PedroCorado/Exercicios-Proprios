lista1 = [1,2,3,4,2,4,2,4,5,1,22,42]
lista2 = [2,46,7,2,3,7,1,2,3,9,10,7]

itens_exclusivos_lista1 = [item for item in lista1 if item not in lista2]

print(itens_exclusivos_lista1)

#Agora vou retirar os itens repetidos e so vou deixar os unicos.

print(list(set(itens_exclusivos_lista1)))# Porem ele vai bagunçar a ordem quando eu paço ele para set
