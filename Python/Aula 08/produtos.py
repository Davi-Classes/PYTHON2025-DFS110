import db


produtos = db.importar_csv() 


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

    if produto_index < 1 or produto_index > len(produtos):
        print('Não há produto com esse indice.')
        return

    produtos.pop(produto_index - 1)
    
    print('Produto excluido com sucesso!')
