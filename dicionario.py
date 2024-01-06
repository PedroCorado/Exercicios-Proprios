meses = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Mai":"Maio",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro",
}

variavel = str(input("Diga-me o que voce quer encontrar: "))


print(meses["Nov"]) #Precisamos colocar o "Indice" inicial dentro de um colchete.
#print(meses["qualquer"]) # Digamos que a pessoa vai consultar se consta um determinado item no dicionario
                        # Porem, se esse item nao tiver, o codigo vai quebrar, para isso nao acontecer
                        # Precisa ser utilizado a função .get
print(meses.get("qualquer")) # Assim vai ser informado que o valor e None, ou seja, nao contem valor
                            # Para definir uma mensagem padrão, colocamos uma virgula na frente e
                            #Dizemos o que vai ser exibido.
print(meses.get(variavel,"Valor não encontrado"))# Aqui eu estou pegando a resposta do input e confer
                                            #Se o mesmo consta no dicionario.