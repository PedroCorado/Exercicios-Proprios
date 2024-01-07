set1 = {10,20,30,70,80,90}
set2 = {40,50,60,100,90}

print(set1 | set2)
print(set1 & set2)

lista = [1,2,3,4,4,4,5,6,41,2,4,5,2,31,1,4,5,2,23]
print(lista)

conjuto = set(lista) #O Set tambem e muito utilizado para remover itens identicos.

print(conjuto)

lista_nova = list(conjuto)

print(lista_nova)

frutas = {'maça','banana','abacaxi'}
print(frutas)
frutas.add('goiaba') #Nos set nao tem como utilizar o append, e utilizado o add
print(frutas)
frutas.update(['laranja','pera','melancia']) #O update e utilizado para adicionar varios valores
print(frutas)#E preciso colocar ele em colchetes pois o set espera que os itens sejam iteraveis.
frutas.remove('abacaxi')
print(frutas)

set1.clear()#Vai limpar todo o set
set2.discard(100)#Vai deletar o item do set

print(set1)
print(set2)