# abrindo o arquivo das stopwords em modo de leitura
with open('../indexes/stopwords', 'r', encoding = "ISO-8859-1") as stop:
    listaStw = stop.readlines()
listaStw = [x.split() for x in listaStw]        # stopwords linha a linha

stopwords = []
for stw in listaStw:                            # colocando as stopwords em uma lista única
    for teste in stw:
        stopwords.append(teste)
stop.close()


def TF(file):                                   # funcao q vai gerar o dicionario con a contagem das palavras
    arquivo = open(file, 'r')                   # abrindo o documento em modo de leitura
    texto = arquivo.readlines()                 # armazenando as linhas do arquivo em uma lista

    cont = dict()                               # dicionario para manter a contagem das palavras

    for linha in texto:                         # percorre cada linha no texto
        listaPalavras = linha.split()           # separa cada linha em uma lista de palavras
        for pal in listaPalavras:               # percorre cada palavra em cada linha
            pal = pal.lower().strip(',.:;()%?') # colocando todas as palavras em lowercase

            # verifica se a palavra já foi contada no dicionario e se ela nao é stopword
            if pal not in cont.keys() and pal not in stopwords:
                cont[pal] = 1                   # se nao estiver no dicionario, coloca ela como primeira ocorrencia
            elif pal in cont.keys():
                cont[pal] += 1                  # se ja estiver, apenas incrementa o valor dela

    arquivo.close()
    return cont                                 # retorna o dicionario para este documento

