import contract
import load_data


def main():
    listas = load_data.Listas()
    contratos = contract.ordem
    listas.load_data()
    contratos.acesso_ordem()
    
    


if __name__ == '__main__':
    main()
