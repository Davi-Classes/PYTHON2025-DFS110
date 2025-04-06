# Percorrendo Dicionários
dicionario = {
    # Chave  : Valor
    'cliente': 'Davi', # Item
    'endereco': 'Rua Tal', 
    'telefone': '312213', 
    'valor': 3.4
}

# Percorrer as Chaves
# Ao percorrer diretamente o dicionário
# ele terá o mesmo efeito de percorrer o .keys()
# for chave in dicionario: 
for chave in dicionario.keys(): 
    print(f'{chave.capitalize()}: {dicionario[chave]}')

# Percorrer os Valores
valores = dicionario.values()
print(valores)

# Percorrer os Items
# items = dicionario.items()
# print(items)
for chave, valor in dicionario.items():
    print(f'{chave.capitalize()}: {valor}')
    