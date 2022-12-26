import contract
import load_data
import interface

class sap():
    def executar(self):
        
        contratos = contract.ordem()
        listas = load_data.Listas()
        contratos.acesso_ordem()
        listas.load_data()


def main():
    interfaces = interface.telas.tela_inicial()
    interfaces.tela_inicial()
    
    


if __name__ == '__main__':
    main()
