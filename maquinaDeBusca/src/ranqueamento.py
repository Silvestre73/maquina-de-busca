from os import chdir
from glob import glob
from math import log2, sqrt
from src.indexacao import TF    # Term Frequency

colecao = []

chdir('../indexes')
for doc in glob('*txt'):
     colecao.append(TF(doc))

consulta = ''.lower().split()


def IDF(termo):
    N = len(colecao)
    ni = 0

    for documento in glob('*.txt'):
        doc = TF(documento)
        if termo in doc.keys():
            ni += 1
    idf = log2(N/ni)
    idf = round(idf, 2)

    return idf


def Wij(doc, termo):
    tf, idf = 0, 0
    if termo in TF(doc).keys():
        tf = 1 + log2(TF(doc)[termo])
        idf = IDF(termo)

    return round(tf * idf, 2)


def sim(doc, consulta):
    numerador = 0
    denominador = 0
    den1, den2 = 0, 0

    for termo in consulta:
        if termo in TF(doc).keys():
            wij = Wij(doc, termo)
            wiq = IDF(termo)
            numerador += wij * wiq

            den1 += Wij(doc, termo) ** 2
            den2 += IDF(termo) ** 2

            denominador = sqrt(den1) * sqrt(den2)

    return numerador / denominador
