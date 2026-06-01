# ==================================================
#   DADOS || LISTA/DICT DOS PRODUTOS
# ==================================================
    descrição_produtos = [] #lista de dicionários que irão conter a descrição dos produtos


# pensei nesse dicionário = {"nome" = ----, "preço" = -----, "categoria/material": ----, "estoque" = -----,
# e pensei em ser uma lista de dicionários, um pra cada produto (pim: é uma das possíbilidades, só coloquei esse dict como sugestão)

# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================


# CREATE  |  cadastro de produto(s) 

#pensei em fazer um mini menu perguntando se quer criar ou nao, e provavelmente um while com uma condicional dentro pra criar um loop de cadastro de produto que pode ser interrompida

def adicionar_produtos():

    add_produto = input("\nDeseja adicionar produtos na loja? [S/N] ").strip().upper()

    while add_produto == "S":

        produto = input("\nDigite o nome do produto: ").strip().capitalize()

        prod_existentes = [] #em duvida se deixo a lista com os nomes dos produtos apenas aqui ou em escopo global, a IA disse que eu tava duplicando dados...

        for p in descrição_produtos: #esse for adiciona apenas a chave nome na lista para ter onde fazer a busca do produto
            prod_existentes.append (p["nome"])
                    
        if produto not in prod_existentes: #verifica se o produto já existe com a lista criada em escopo local com os nomes dos produtos
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

    return descrição_produtos

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

print ("====== Adicione produtos na loja ======")


# ==================================================
#   Main || LOOP INICIAL
# ==================================================

descrição_produtos = adicionar_produtos()


