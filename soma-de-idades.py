pessoas = [
    {"id": 1, "nome": "João", "idade": 25},
    {"id": 2, "nome": "Maria", "idade": 30},
    {"id": 3, "nome": "Pedro", "idade": 22},
    {"id": 4, "nome": "Ana", "idade": 28},
    {"id": 5, "nome": "Carlos", "idade": 35},
    {"id": 6, "nome": "Isabel", "idade": 40},
    {"id": 7, "nome": "Lucas", "idade": 27},
    {"id": 8, "nome": "Mariana", "idade": 32},
    {"id": 9, "nome": "Gabriel", "idade": 29},
    {"id": 10, "nome": "Laura", "idade": 26}
]
valores = 0
for indice,valor in enumerate(pessoas):
    valores += valor['idade']
    quantidade_pessoas = indice + 1
print(valores)
print(quantidade_pessoas)
print(f'A media de idade é de : {valores/quantidade_pessoas}')
