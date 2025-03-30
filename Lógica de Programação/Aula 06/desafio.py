# Desafio!

# Vocês foram contratados para Desenvolver um sistema para registrar vendas de uma loja de doce:

# - Ao funcionario chegar na loja, ele inicia o sistema que fica rodando durante todo o expediente (ou seja, em processo de repetição) - OK

# - Ao registrar uma venda, o sistema pede: nome do cliente, endereco do cliente, numero de telefone do cliente e valor da compra. Essas informações precisam ser armazenadas de alguma forma (fica a criterio de vocês descobrir como armazenar essas informações)

# - Após cada venda registrada, o sistema perguntará se o operador deseja registrar outra venda, e caso não queira encerra o programa. - OK

# - Ao encerrar o programa, o sistema sorteia uma das vendas do dia para enviar um brinde para o cliente sorteado (fica ao seu criterio entender como fazer o sorteio)
vendas = []

while True:
    resp = input('Deseja registrar uma nova venda? [S/N] -> ')

    if resp.upper() == 'N':
        break

    cliente = input('Digite o nome do cliente: ')
    endereco = input('Digite o endereço do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    valor = float(input('Digite o valor da compra: '))

    venda = (cliente, endereco, telefone, valor)
    vendas.append(venda)

print(vendas)
print('Fim do Programa.')