# ==================================================
#   DADOS || LISTA/DICT DOS PRODUTOS
# ==================================================
produtos = {
  "produto1" : 12,99,
  "produto2" : 19,99
}

# pensei nesse dicionário = {"nome" = ----, "preço" = -----, "categoria/material": ----, "estoque" = -----,
# e pensei em ser uma lista de dicionários, um pra cada produto (pim: é uma das possíbilidades, só coloquei esse dict como sugestão)

lista_produtos = [] #aqui teria uma lista com os nomes dos produtos na mesma ordem

#pode pensar em outras estruturas de dados

# ==================================================
#   FUNÇÕES DO CRUD
# ==================================================


# CREATE  |  cadastro de produto(s) 

#pensei em fazer um mini menu perguntando se quer criar ou nao, e provavelmente um while com uma condicional dentro pra criar um loop de cadastro de produto que pode ser interrompida

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

# ==================================================
#   Main || LOOP INICIAL
# ==================================================
