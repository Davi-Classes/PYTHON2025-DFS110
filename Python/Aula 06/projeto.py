produtos = [
    # Estrutura de Exemplo!
    # {
    #     'nome': 'Produto 1',
    #     'preco': 1234.43,
    #     'quantidade': 1
    # },
    # {
    #     'nome': 'Produto 1',
    #     'preco': 1234.43,
    #     'quantidade': 1
    # },
]

def menu():
    print('=' * 30)
    print('Gerenciamento de Produtos'.center(30))
    print('=' * 30)
    print('[1] - Listar Produtos')
    print('[2] - Cadastrar Produto')
    print('[3] - Editar Produto')
    print('[4] - Excluir Produto')
    print('[5] - Sair')
    print('=' * 30)

    opcao = input('--> Selecione uma Opção: ')
    return opcao


def listar_produtos():
    # Ao listar produtos você deve mostrar todos 
    # os produtos cadastrados na lista na tela
    print('Listando Produtos...')


def cadastrar_produto():
    # Ao cadastrar um novo produto o usuário insere nome, preço e quantidade
    # e você deve criar um dicionário e adiciona na lista de produtos.
    print('Cadastrando Produtos...')


def editar_produto():
    # Ao editar o usuário seleciona o produto que deseja editar 
    # e você deve alterar todas as informações dequele produto (nome, o preço e quantidade)
    print('Editando Produtos...')


def excluir_produto():
    # Ao excluir o usuário seleciona o produto que deseja excluir
    # e você deve remover o produto da lista
    print('Excluindo Produtos...')


# Codigo Principal.
while True:
    opcao = menu()
    
    if opcao == '1':
        listar_produtos()
    elif opcao == '2':
        cadastrar_produto()
    elif opcao == '3':
        editar_produto() 
    elif opcao == '4':
        excluir_produto()
    elif opcao == '5':
        break
    else:
        print('Opção Inválida.')

    input('Pressione <ENTER> para continuar...')
