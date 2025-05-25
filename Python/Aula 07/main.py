produtos = [
    # Estrutura de Exemplo!
    {
        'nome': 'Produto 1',
        'preco': 1234.43,
        'quantidade': 1
    },
    {
        'nome': 'Produto 2',
        'preco': 100,
        'quantidade': 6
    },
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
    if len(produtos) == 0:
        print('Não há produtos cadastrados')
        return False

    print(' Produtos '.center(30, '='))
    for index, produto in enumerate(produtos, start=1):
        print(f'[{index}] - {produto['nome']}')
        print(f'Preço: R${produto['preco']:.2f}')
        print(f'Quantidade: {produto['quantidade']}')
        
        # Não mostrar a separação no ultimo produto
        if index != len(produtos):
            print('-' * 30)
    
    return True


def cadastrar_produto():
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade: '))

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    produtos.append(produto)

    print('Produto cadastrado com sucesso.')


def editar_produto():
    tem_produtos = listar_produtos()

    if not tem_produtos:
        return
    
    print('=' * 30)
    produto_index = int(input('Selecione o produto a ser editado: '))
    
    # Passagem de valor por Referencia
    # A variavel produto é uma referencia ao produto que está na lista 
    produto = produtos[produto_index - 1]

    produto['nome'] = input('Digite o novo nome do produto: ')
    produto['preco'] = float(input('Digite o novo preço do produto: '))
    produto['quantidade'] = int(input('Digite a nova quantidade do produto: '))

    print('Produto editado com sucesso.')


def excluir_produto():
    tem_produtos = listar_produtos()

    if not tem_produtos:
        return
    
    print('=' * 30)
    produto_index = int(input('Selecione o produto a ser excluido: '))

    produtos.pop(produto_index - 1)
    
    print('Produto excluido com sucesso!')



# Codigo Principal.
while True:
    opcao = menu()
    
    # Match case
    match opcao:
        case '1':
            listar_produtos()
        case '2':
            cadastrar_produto()
        case '3':
            editar_produto() 
        case '4':
            excluir_produto()
        case '5':
            break
        case _:
            print('Opção Inválida.')
            
