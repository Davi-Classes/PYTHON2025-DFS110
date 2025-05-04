# Revisão Funções
# Uma função é um bloco de codigo que recebe entradas
# e realiza algum processamento, que pode ou não retornar alguma coisa
def mostrar_produto(nome, preco, quantidade):
    print(f'Produto: {nome}')
    print(f'Preço: R${preco:.2f}')
    print(f'Quantidade: {quantidade}')


# Pedindo variaveis para o usuário
produto = input('Digite o nome do produto que deseja comprar: ')
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))

# Passando os valores das variaveis para a função
mostrar_produto(produto, preco, quantidade)
