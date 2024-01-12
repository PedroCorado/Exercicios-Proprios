import requests

link = 'https://4e471704-ec92-4fe0-a0e8-71e710fadd55-00-1cayjl6hy2vdh.janeway.replit.dev/tabela'

requisicao = requests.get(link)

tabela = requisicao.json()
for indice,valores in enumerate(tabela):
    print(valores['nome'])
print(requisicao)