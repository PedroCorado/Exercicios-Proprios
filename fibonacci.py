primeiro = 1 # Inicia 1 // Recebe 1 // Recebe 2 // 
segundo = 1 # Inicia 1 // Recebe 2 // Recebe 3 //
terceiro = 0 # Vai receber 2 // Recebe 3 //

stop = 10000
while terceiro <= stop:
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
print(terceiro)