lista = [0,1,2,3,4,5,6,7,8,9,10]

class EscreverArquivo(object):
    def __init__(self,arquivo: str):
        self.arquivo = arquivo
        with open(arquivo, 'w', encoding='utf-8') as dados_arquivos:
            dados_arquivos.write(str(lista))
nova_lista = EscreverArquivo('./Lendo&Escrevendo/numeros.csv')