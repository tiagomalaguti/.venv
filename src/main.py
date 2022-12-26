import contract
import load_data
import interface

class sap():
    def executar(self, ordem_teste):
        
        contratos = contract.ordem()
        contratos.acesso_ordem(ordem_teste)


def main():
    interfaces = interface.telas.tela_inicial()
    interfaces.tela_inicial()
    
    


if __name__ == '__main__':
    main()
