# Importando o Modulo Todo.
import os # Built-in
import db

# Importando as funções do Modulo
# from produtos import * # Importar tudo daquele modulo
from produtos import produtos, listar_produtos, cadastrar_produto, editar_produto, excluir_produto


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


# Codigo Principal.
while True:
    os.system('clear')
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
    
    input('\nAperte <ENTER> para continuar...')


db.exportar_csv(produtos)