from webbrowser import open_new
from tkinter import *
from src.ranqueamento import *


def btnBuscaClick():
    resultados = dict()
    consulta = enBusca.get().split()

    for termo in consulta:
        chdir('../indexes')
        for doc in glob('*.txt'):
            if termo in TF(doc).keys():
                resultados[doc] = round(sim(doc, consulta), 4)
    print(resultados)
    if resultados:
        lbResultados["text"] = ''
        for item in resultados.keys():
            nomeArtigo = item.strip('.txt')
            resultList.insert(END, nomeArtigo)
        resultList.place(x=15, y=40)
    else:
        resultList.place_forget()
        lbResultados["text"] = 'Sua consulta - \'{}\' - não encontrou nenhum documento correspondente.'.format(enBusca.get())


def btnAbrirClick():
    item = resultList.curselection()
    nomeArquivo = str(resultList.get(item))
    nomeArquivo = nomeArquivo + '.pdf'
    caminho = '../documentos/{}'.format(nomeArquivo)

    open_new(caminho)


tela = Tk()
tela.title('Busca Textual')
tela.geometry('800x300+300+100')

lbBusca = Label(tela, text='Digite sua busca')
lbBusca.grid(row=0, column=0, ipadx=20)

lbResultados = Label(tela, text='')
lbResultados.place(x=10, y=40)

resultList = Listbox(tela, width=95, selectmode=SINGLE)

enBusca = Entry(tela, width=50)
enBusca.grid(row=0, column=1, ipadx=20)

btnBusca = Button(tela, text='Buscar', command=btnBuscaClick)
btnBusca.grid(row=0, column=2)

btnAbrir = Button(tela, text='Abrir', command=btnAbrirClick)
btnAbrir.place(x=730, y=260)


tela.mainloop()
