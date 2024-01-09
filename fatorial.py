# # numero = 30
# # lista = []
# # contador = 1
# # while contador <= numero:
# #     lista.append(contador)
# #     contador += 1
# # soma = 0
# # for i in lista:
# #     soma += i * 30
# # print(soma)

# numero = 30
# soma = 0
# contador = 1

# while contador <= numero:
#     soma += contador * numero
#     contador += 1

# print(soma)

def calcular_fatorial(numero):
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero_para_calcular = 30
resultado_fatorial = calcular_fatorial(numero_para_calcular)
print(f"O fatorial de {numero_para_calcular} é {resultado_fatorial}")
