# Tipos de Parametros
produtos = []


def cadastrar_produto(nome, preco, quantidade):
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    produtos.append(produto)


print(produtos)

# Passagem de Parametros Posicional
cadastrar_produto('Celular', 899.90, 3)
print(produtos)

# Passagem de Parametros Nomeada
cadastrar_produto(preco=49.90, quantidade=1, nome='Mouse')
print(produtos)

# Passagem de Parametros Posicional e Nomeada
# Os primeiros parametros devem ser os posicionais, depois os nomeados
cadastrar_produto('Monitor', quantidade=1, preco=1199.99)
print(produtos)