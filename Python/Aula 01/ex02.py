# Ex02. Faça um programa que peça 5 nomes e mostre todos os nomes digitados

nomes = []

for n in range(1, 6):
    nome = input(f'Digite o {n} nome: ')
    nomes.append(nome)

print('Nomes:')
for nome in nomes:
    print(f'-> {nome}')