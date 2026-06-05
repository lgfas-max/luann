# ==================================================
#   DADOS || LISTA/DICT DOS PRODUTOS
# ==================================================
descrição_produtos = [{
                "nome":     "Item",
                "preço":    12.00,
                "material": "Madeira",
                "estoque":  2
            }] #lista de dicionários que irão conter a descrição dos produtos


# pensei nesse dicionário = {"nome" = ----, "preço" = -----, "categoria/material": ----, "estoque" = -----,
# e pensei em ser uma lista de dicionários, um pra cada produto (pim: é uma das possíbilidades, só coloquei esse dict como sugestão)

# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================


# CREATE  |  cadastro de produto(s) 

#pensei em fazer um mini menu perguntando se quer criar ou nao, e provavelmente um while com uma condicional dentro pra criar um loop de cadastro de produto que pode ser interrompida

def adicionar_produtos(descrição_produtos):

    add_produto = input("\nDeseja adicionar produtos na loja? [S/N] ").strip().upper()

    while add_produto == "S":

        produto = input("\nDigite o nome do produto: ").strip().capitalize()

        #descrição_produtos = [] #em duvida se deixo a lista com os nomes dos produtos apenas aqui ou em escopo global, a IA disse que eu tava duplicando dados...

        #for p in descrição_produtos: #esse for adiciona apenas a chave nome na lista para ter onde fazer a busca do produto
         #   descrição_produtos.append (p["nome"])
                    
        if not any(chave["nome"] == produto for chave in descrição_produtos): #possui a mesma função da outra lista criada e evita a duplicidade pra não trabalhar com varias listas
            print(f"\nProduto '{produto}' adicionado!")

            print(f"\nAdicione a descrição do produto: ") #criação do dicionário com a descrição do produto

            produtos = {
                "nome":     produto,
                "preço":    float(input("Valor do produto: R$ ")),
                "material": input("Material do produto: ").strip().capitalize(),
                "estoque":  int(input("Estoque do produto: "))
            }
            descrição_produtos.append(produtos) #adiciona o dicionário em uma lista para ter uma sequência de cadastros
        else:
            print("\nProduto já existe na loja.")

        add_produto = input("\nDeseja adicionar mais produtos? [S/N] ").strip().upper()

    return 0

# READ    |  listar produto(s)

# - poderia fazer um for para listar os produtos na lista e outro para o dicionário
# - um for para ver colocar o indice e/ou chave para acessar um produto específico na lista e/ou no dicionario

# UPDATE  |  atualizar produto() 

# - atualização poderia ser de preço e estoque

# DELETE  |  excluir produto(s)

# eu to achando isso aqui mais direto, será que pode reaproveitar a busca do read para saber o que deletar? (pim: da pra chamar a função do read e fazer as alterações tanto do DELETE como do UPDATE se preferir)

# ==================================================
#   MENU || "INTERFACE" DO SISTEMA
# ==================================================
def menu():
    print("\n======= MENU =======")
    print("1 - Adicionar Produto")
    print("2 - Excluir Produto")
    print("3 - Atualizar Produto")
    print("4 - Ver Produtos")
    print("5 - Sair")
    print("====================")


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
                adicionar_produtos(descrição_produtos)
            
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

