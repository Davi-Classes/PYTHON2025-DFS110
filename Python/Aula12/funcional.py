# Paradigma Funcional

def criar_cliente():
    nome = input('Digite o nome do cliente: ')
    endereco = input('Digite o endereço do cliente: ')
    compras = []

    return novo_cliente(nome, endereco, compras)


def novo_cliente(nome, endereco, compras = []):
    return {
        'nome': nome,
        'endereco': endereco,
        'compras': compras
    }


def realizar_compra(cliente):
    compra = {}

    compra['valor_bruto'] = float(input('Digite o valor da compra do cliente: '))
    compra['desconto'] = float(input('Digite o percentual de desconto na compra: '))
    compra['valor_liquido'] = compra['valor_bruto'] * (1 - compra['desconto'])
    cliente['compras'].append(compra)

    return compra


cliente1 = criar_cliente()

print(cliente1)
realizar_compra(cliente1)
print(cliente1)
realizar_compra(cliente1)
print(cliente1)

# cliente2 = criar_cliente()
# realizar_compra(cliente2)