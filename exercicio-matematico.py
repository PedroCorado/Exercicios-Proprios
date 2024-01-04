def exercicios():
    escolha = str(input("Diga-me qual categoria de exercicios voce quer fazer \n"
                        "Multiplicação[*]\n"
                        "Divisãa[/]\n"
                        "Adição[+]\n"
                        "Subtração[-]\n"
                        ))
    if escolha == '*':
        def tabuada():
                perguntas = [
            {
                'pergunta':'Quanto e 5x5',
                'alternativas': ['5','20','25','30','10'],
                'resposta':'25',
            },
            {
                'pergunta':'Quanto e 3x5',
                'alternativas': ['15','5','3','30','10'],
                'resposta':'25',
            },
            {
                'pergunta':'Quanto e 9x5',
                'alternativas': ['95','20','65','40','45'],
                'resposta':'25',
            },
        ]
                print(perguntas[0]['pergunta'])
                print(perguntas[0]['alternativas'])
                respostas = str(input('Qual a alternativa correta : '))
                if respostas == perguntas[0]['resposta']:
                    print('Parabens voce acertou!')
                else:
                    print('Voce errou.')
    tabuada()
exercicios()
