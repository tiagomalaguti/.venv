import contract
import load_data
import interface

class sap():
    def executar(self, ordem_teste):
        
        contratos = contract.ordem()
        contratos.acesso_ordem(ordem_teste)

class contrato():
    def atualiza_contrato(self, contrato):
        x = load_data.atualiza()
        x.baixar_dados(contrato)

def main():
    interface.telas.tela_inicial()
    
    #atualizar = load_data.atualiza()
    #atualizar.baixar_dados()
  
    


if __name__ == '__main__':
    main()
