from tkinter import *
from tkinter import ttk
import main
import load_data

class telas:

    def chamar_funcao(): 
        ordem_teste = ordem.get()
        chamar = main.sap()
        chamar.executar(ordem_teste)
        
    def chamar_funcao2():
        var_contrato = contrato.get()
        chama_contrato = main.contrato()
        chama_contrato.atualiza_contrato(var_contrato)

    def tela_inicial():
        global ordem
        global janela
        global contrato
        janela = Tk()
        janela.geometry("400x400")
        janela.minsize(900, 900)
        janela.maxsize(900, 900)
        janela.title("Tela Principal")
        frm = ttk.Frame(janela, padding="3 3 12 12")

        texto = Label(janela, text="Ordem")
        texto.grid(column=1, row=2)
        
        texto2 = Label(janela, text="contrato")
        texto2.grid(column=1, row=3)
        
        ordem = Entry(janela)
        ordem.grid(column=2, row=2)
        
        contrato = Entry(janela)
        contrato.grid(column=2, row=3)

        frm.grid()
        botao = Button(janela, text="Gerar Custo", command=telas.chamar_funcao)
        botao.grid(column=3, row=2)
        botao2 = Button(janela, text="atualiza contrato", command=telas.chamar_funcao2)
        botao2.grid(column=3, row=3)
        janela.mainloop()
