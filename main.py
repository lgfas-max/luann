
# ==================================================
#   Imports iniciais
# ==================================================
from dados import descricao_produtos
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
        match acao:
            case 1:
                adicionar_produtos(descricao_produtos)
            
            case 2:
                # excluir_produto(descrição_produtos)
                print("\nFunção 'Excluir Produto' ainda não implementada.")
            
            case 3:
                # atualizar_produto(descrição_produtos)
                print("\nFunção 'Atualizar Produto' ainda não implementada.")
            
            case 4:
                # visualizar_produtos(descrição_produtos)
                print("\nFunção 'READ' ainda não implementada.")
            
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
