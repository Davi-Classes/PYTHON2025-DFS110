# Dicionários
venda = {
    # Chave  : Valor
    'cliente': 'Davi', # Item
    'endereco': 'Rua Tal', 
    'telefone': '312213', 
    'valor': 3.4
}

# Acessar um valor (Chave Existente)
print(venda['cliente'])
print(venda.get('endereco'))

# Acessar um valor (Chave não existente)
# print(venda['nao_existe']) # KeyError
print(venda.get('nao_existe')) # Retorna "None" pois chave não existe.


# Adicionar ou Alterar um Valor
print(venda)

venda['cliente'] = 'Davi Lucciola' # A chave existe, ele altera o valor.
venda['cpf'] = '54358435834' # A chave não existe, ele cria um novo item.

print(venda)

# Removendo um item
venda.pop('cpf') # Removendo o item na chave CPF
print(venda)