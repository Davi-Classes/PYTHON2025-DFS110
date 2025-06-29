import pprint

# Paradigma Procedural
cliente = {}

cliente['nome'] = input('Digite o nome do cliente: ')
cliente['endereco'] = input('Digite o endereço do cliente: ')
cliente['compras'] = []


compra = {}
compra['valor_bruto'] = float(input('Digite o valor da compra do cliente: '))
compra['desconto'] = float(input('Digite o percentual de desconto na compra: '))
compra['valor_liquido'] = compra['valor_bruto'] * (1 - compra['desconto'])
cliente['compras'].append(compra)

pprint.pp(cliente)

