# Criando um novo dicionário
pet = {}

pet['nome'] = input('Digite o nome do Pet: ')
pet['especie'] = input('Digite a especie do animal: ')
pet['cor'] = input('Digite a cor do pet: ')
pet['idade'] = int(input('Digite a idade do pet: '))

print('Meu Pet: ')
print(f'Nome: {pet['nome']}')
print(f'Especie: {pet.get('especie')}')
print(f'Cor: {pet.get('cor')}')
print(f'Especie: {pet.get('idade')}')

print(pet)