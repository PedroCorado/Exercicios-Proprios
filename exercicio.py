lista = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,4,7,8,9],
    [1,2,3,8,8,2,1,2,7,6]
]

def encontrar_primeiro_igual(listas):
    numero_checados = set()
    primeiro_duplicado = -1
    
    for numero in listas:
        if numero in numero_checados:
            primeiro_duplicado = numero
            break
        numero_checados.add(numero)
        
    print()
    print()
    
    return primeiro_duplicado

for itens in lista:
    print(encontrar_primeiro_igual(itens))