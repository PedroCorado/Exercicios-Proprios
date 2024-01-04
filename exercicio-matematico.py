import os

def exercicios():
    escolha = str(input("Diga-me qual categoria de exercicios voce quer fazer \n"
                        f"{'-' * 52}\n"
                        "Multiplicação[*]\n"
                        "Divisãa[/]\n"
                        "Adição[+]\n"
                        "Subtração[-]\n"
                        "Resposta : "
                        ))
    os.system('cls')
    if escolha == '*':
        def multiplicacao():
                nivelmultiplicacao = str(input("Qual o nivel voce quer escolher da multiplicação :\n"
                                        "Facil[F]\n"
                                        "Intermediario[I]\n"
                                        "Dificil[D]\n"
                                        "Resposta : "
                                        ))
                os.system('cls')
                perguntas = [
            {
                'pergunta':'Quanto e 5x5',
                'alternativas': ['5','20','25','30','10'],
                'resposta':'25',
            },
            {
                'pergunta':'Quanto e 3x5',
                'alternativas': ['15','5','3','30','10'],
                'resposta':'15',
            },
            {
                'pergunta':'Quanto e 9x5',
                'alternativas': ['95','20','65','40','45'],
                'resposta':'45',
            },
        ]
                if nivelmultiplicacao == 'F':
                    print(perguntas[0]['pergunta'])
                    print(perguntas[0]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[0]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif nivelmultiplicacao == 'I':
                    print(perguntas[1]['pergunta'])
                    print(perguntas[1]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[1]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif nivelmultiplicacao == 'D':
                    print(perguntas[2]['pergunta'])
                    print(perguntas[2]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[2]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
    if escolha == '/':
        def multiplicacao():
                niveldivisao = str(input("Qual o nivel voce quer escolher da Divisão :\n"
                                        "Facil[F]\n"
                                        "Intermediario[I]\n"
                                        "Dificil[D]\n"
                                        "Resposta : "
                                        ))
                os.system('cls')
                perguntas = [
            {
                'pergunta':'Quanto e 4/2',
                'alternativas': ['5','2','25','30','10'],
                'resposta':'2',
            },
            {
                'pergunta':'Quanto e 100/5',
                'alternativas': ['15','5','3','30','20'],
                'resposta':'20',
            },
            {
                'pergunta':'Quanto e 75/3',
                'alternativas': ['95','20','65','40','25'],
                'resposta':'25',
            },
        ]
                if niveldivisao == 'F':
                    print(perguntas[0]['pergunta'])
                    print(perguntas[0]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[0]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif niveldivisao == 'I':
                    print(perguntas[1]['pergunta'])
                    print(perguntas[1]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[1]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif niveldivisao == 'D':
                    print(perguntas[2]['pergunta'])
                    print(perguntas[2]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[2]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
    if escolha == '+':
        def multiplicacao():
                niveldivisao = str(input("Qual o nivel voce quer escolher da Adição :\n"
                                        "Facil[F]\n"
                                        "Intermediario[I]\n"
                                        "Dificil[D]\n"
                                        "Resposta : "
                                        ))
                os.system('cls')
                perguntas = [
            {
                'pergunta':'Quanto e 15+20',
                'alternativas': ['5','2','35','30','10'],
                'resposta':'35',
            },
            {
                'pergunta':'Quanto e 73+28',
                'alternativas': ['99','98','101','100','90'],
                'resposta':'101',
            },
            {
                'pergunta':'Quanto e 376+235',
                'alternativas': ['756','520','782','350','611'],
                'resposta':'611',
            },
        ]
                if niveldivisao == 'F':
                    print(perguntas[0]['pergunta'])
                    print(perguntas[0]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[0]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif niveldivisao == 'I':
                    print(perguntas[1]['pergunta'])
                    print(perguntas[1]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[1]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif niveldivisao == 'D':
                    print(perguntas[2]['pergunta'])
                    print(perguntas[2]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[2]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
    if escolha == '-':
        def multiplicacao():
                niveldivisao = str(input("Qual o nivel voce quer escolher da Subtração :\n"
                                        "Facil[F]\n"
                                        "Intermediario[I]\n"
                                        "Dificil[D]\n"
                                        "Resposta : "
                                        ))
                os.system('cls')
                perguntas = [
            {
                'pergunta':'Quanto e 15+20',
                'alternativas': ['5','2','35','30','10'],
                'resposta':'5',
            },
            {
                'pergunta':'Quanto e 56-22',
                'alternativas': ['34','12','11','25','33'],
                'resposta':'34',
            },
            {
                'pergunta':'Quanto e 776-214',
                'alternativas': ['356','562','482','350','411'],
                'resposta':'562',
            },
        ]
                if niveldivisao == 'F':
                    print(perguntas[0]['pergunta'])
                    print(perguntas[0]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[0]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif niveldivisao == 'I':
                    print(perguntas[1]['pergunta'])
                    print(perguntas[1]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[1]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
                elif niveldivisao == 'D':
                    print(perguntas[2]['pergunta'])
                    print(perguntas[2]['alternativas'])
                    respostas = str(input('Qual a alternativa correta : '))
                    if respostas == perguntas[2]['resposta']:
                        print('Parabens voce acertou!')
                    else:
                        print('Voce errou.')
    multiplicacao()
exercicios()
