from tkinter import *
from tkinter import ttk
import main

class telas:

    def chamar_funcao(): 
        ordem_teste = ordem.get()
        chamar = main.sap()
        chamar.executar(ordem_teste)

    def tela_inicial():
        global ordem
        global janela
        janela = Tk()
        janela.geometry("400x400")
        janela.minsize(900, 900)
        janela.maxsize(900, 900)
        janela.title("Tela Principal")
        frm = ttk.Frame(janela, padding="3 3 12 12")

        texto = Label(janela, text="Ordem")
        texto.grid(column=1, row=2)
        
        ordem = Entry(janela)
        ordem.grid(column=2, row=2)

        frm.grid()
        botao = Button(janela, text="Gerar Custo", command=telas.chamar_funcao)
        botao.grid(column=3, row=2)
        janela.mainloop()
