lista = ['maria','joao','carlos']
lista2 = ['marcelo','pedro','fabiana','maria']

print(lista2 ^ lista)

lista[-1] = 'pedro'
print(lista)

lista.insert(2,'clara')
print(lista)

lista.append('marcos')
print(lista)

lista.remove('joao')
print(lista)

lista.pop(2)
print(lista)

tupla = (1,) # Se nao adicionar uma virgula ao final ele sera considerado um int, o mesmo para str ou float...
print(type(tupla))# Tuplas sao imutaveis

funcionarios = {
    "maria":"Vendedora",
    "julia":"Atendente",
    "patricio":"Gerente",
    "pedro":{
        "cargo":"Dono",
        "salario":"170.000,00",
        },
}

funcionarios2 = {
    "lara":"Atendente",
    "luna":"Enfermeira",
    "ueber":{
        "cargo":"Dono",
        "salario":"200.000,00",
    },
}

print(funcionarios['maria'])
print(funcionarios['pedro']['salario'])

print(len(funcionarios))#Mostra a quantidade de chaves
print(str(funcionarios))#Mostra o dicionario em formato de str
print((funcionarios.keys()))#Mostra as chaves presentes no dicionario
adc1=funcionarios['beatriz']='Contabilidade'#Cria uma nova chave e seta o valor
print(funcionarios)

juncao_dicionarios = funcionarios | funcionarios2#O sinal de | faz a junção de 2 dicionarios ou mais.

print(juncao_dicionarios)

funcionarios5 = {1,2,3,7}
funcionarios52 = {1,2,3,4,5}

print(funcionarios5 & funcionarios52)#O operador & faz a intersecção presente em ambos os sets
                                    #Vai mostrar 1,2,3
junção_de_sets = funcionarios5 | funcionarios52#O sinal de | faz a junção de 2 sets ou mais.
print(junção_de_sets)

print(funcionarios5 - funcionarios52)#O sinal de - vai mostrar os unicos itens presente no primeiro set
print(funcionarios5 ^ funcionarios52)#O sinal de ^ vai mostrar os itens que nao tem em ambos.
