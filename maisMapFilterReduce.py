# lista = [
#     [1,2,3,4,5,6,7,8,9,10],
#     [1,2,4,5,6,1,6,9,10,7],
#     [1,2,3,5,5,6,8,7,9,10],
# ]

# def iguais(lista):
#     unicos = set()
#     repetido = -1
    
#     for item in lista:
#         if item in unicos:
#             repetido = item
#             break
#         unicos.add(item)
#     return repetido

# for itens in lista:
#     print(iguais(itens))
from functools import reduce

lista = [
    {'id_vendedor': '104271', 'valor_emprestimos': '448.0', 'quantidade_emprestimos': '1', 'data': '20161208'},
{'id_vendedor': '21476', 'valor_emprestimos': '826.7', 'quantidade_emprestimos': '3', 'data': '20161208'},
{'id_vendedor': '87440', 'valor_emprestimos': '313.6', 'quantidade_emprestimos': '3', 'data': '20161208'},
{'id_vendedor': '15980', 'valor_emprestimos': '-8008.0', 'quantidade_emprestimos': '6', 'data': '20161208'},
{'id_vendedor': '215906', 'valor_emprestimos': '2212.0', 'quantidade_emprestimos': '5', 'data': '20161208'},
{'id_vendedor': '33696', 'valor_emprestimos': '2771.3', 'quantidade_emprestimos': '2', 'data': '20161208'},
{'id_vendedor': '33893', 'valor_emprestimos': '2240.0', 'quantidade_emprestimos': '3', 'data': '20161208'},
{'id_vendedor': '214946', 'valor_emprestimos': '-4151.0', 'quantidade_emprestimos': '18', 'data': '20161208'},
{'id_vendedor': '123974', 'valor_emprestimos': '2021.95', 'quantidade_emprestimos': '2', 'data': '20161208'},
{'id_vendedor': '225870', 'valor_emprestimos': '4039.0', 'quantidade_emprestimos': '2', 'data': '20161208'},
]

valores_emprestimos = list(map(lambda x:float(x['valor_emprestimos']),lista))
print(valores_emprestimos)
print()
valores_emprestimos_filtrado = list(filter(lambda x:x >= 0,valores_emprestimos))
print(valores_emprestimos_filtrado)
print()
valores_somados = reduce(lambda x,y:x+y,valores_emprestimos_filtrado)
print(valores_somados)