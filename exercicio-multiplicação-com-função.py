def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador*numero
    return multiplicar
resultadox2 = criar_multiplicador(2)
resultadox3 = criar_multiplicador(3)
resultadox4 = criar_multiplicador(4)

print(resultadox2(2))
print(resultadox3(2))
print(resultadox4(2))