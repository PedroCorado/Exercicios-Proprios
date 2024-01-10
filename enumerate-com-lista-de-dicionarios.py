lista = [
    {
        "id":1,
        "nome":'Pedro',
        "idade":21,
    },
    {
        "id":2,
        "nome":'Maria',
        "idade":25,
    },
    {
        "id":3,
        "nome":'Leticia',
        "idade":18,
    },
]

for indice,valor in enumerate(lista):
    print(indice,valor['nome'])
