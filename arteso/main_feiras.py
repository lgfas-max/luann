# ==================================================
#   Imports iniciais
# ==================================================
from menu import *
from crud import *
# ==================================================
#   Main || LOOP INICIAL
# ==================================================
def main():
    while True:
        menu()

        try:
            acao = int(input("\nEscolha sua ação (1 - 5): "))
        except ValueError:
            print("\nDigite apenas números.")
            continue
        match acao: #eu pensei em deixar cada case na ordem que ta o crud, mas n sei se é detalhe besta
            case 1:
                inscrever_feiras()
            
            case 2:
                # ler_inscricao()
                print("\nFunção 'Excluir Produto' ainda não implementada.")
            
            case 3:
                # atualizar_inscricao()
                print("\nFunção 'Atualizar Produto' ainda não implementada.")
            
            case 4:
                #deletar_inscrição()               
            
            case 5:
                print("\nPrograma encerrado.")
                break
            
            case _:
                print("\nOpção inválida. Escolha um número entre 1 e 5.")


# ==================================================
#   INICIALIZAÇÃO DO PROGRAMA
# ==================================================
if __name__ == "__main__":
    main()
