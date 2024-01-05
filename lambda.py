iphone = 5000

salario = lambda x: x - iphone # "lambda x:" e como se foçe função(x):
                                # "x - iphone" e como se foçe o return da função
print(salario(15000))

print('-'*50)

salario_minimo = [1789,2100,2463,1995]
salario_corporativo = [3658,5274,6211,9100]

aumento_salario_minimo = list(map(lambda x:x * 0.25,salario_minimo))
aumento_salario_corporativo = list(map(lambda x:x * 0.1,salario_corporativo))

print(aumento_salario_minimo)
print(aumento_salario_corporativo)

print('-'*50)

valores = [10,50,56,42,82,854,25,68,27,684,58,55,47,68,32,11,44,55]

somatoria = list(map(lambda x:x +100, valores))

print(somatoria)

print('-'*50)

def funcao(x):
    return x + 100

somatoria2 = list(map(funcao,valores))

print(somatoria2)