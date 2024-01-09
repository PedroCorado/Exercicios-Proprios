palavra = 'radar'
tamanho = len(palavra)
resultado = ""

for i in range(tamanho - 1, -1, -1):
    resultado += palavra[i]

if resultado == palavra:
    print("Parabens, a sua palavra e um palíndromo")
else:
    print("A sua palavra não e um palíndromo.")