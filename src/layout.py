from tkinter import *
from tkinter import ttk


class Tela():
    def executa_1():
        print("chamou1")

    def executa_2():
        print("chamou2")

    def main():
        janela = Tk()
        janela.geometry("750x500")
        janela.title("Tela Principal")
        frm = ttk.Frame(janela)

        frm.grid()
        botao = Button(janela, text="Gerar Custo", command=Tela.executa_1)
        botao.grid(row=1,column=0,sticky="nsew")

        botao1 = Button(janela, text="Gerar Custo2", command=Tela.executa_2)
        botao1.grid(row=1, column=1,sticky="nsew")

        janela.mainloop()


if __name__ == '__main__':
    Tela.main()
