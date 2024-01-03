def criar_lista():
    lista = []
    def manipular_lista():
        nonlocal lista
        while True:
            pergunta = str(input("Para adicionar item[+] para remover[-] para visualizar[/] para encerrar[*] "))
            if pergunta == '+':
                adicionar = str(input("Diga qual item voce dejesa adicionar: "))
                lista.append(adicionar)
            elif pergunta == '/':
                break
    manipular_lista()
    print(lista)
criar_lista()
