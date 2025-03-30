pessoa = {}

pessoa['nome'] = input('Digite o nome da pessoa: ')
pessoa['altura'] = float(input('Digite a altura da pessoa: ')) 
pessoa['idade'] = int(input('Digite a idade da pessoa: '))

print('---- Informações ----')
print(f'Nome: {pessoa.get('nome')}')
print(f'Altura: {pessoa.get('altura')}m')
print(f'Idade: {pessoa.get('idade')} anos')