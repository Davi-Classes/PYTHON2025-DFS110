# Ex02. Faça um programa que pede um numero para o usuário, e mostre o enésimo valor da sequencia de fibonacci. Exemplo:

# Até qual numero deseja mostrar fibonacci? 
# >>> 8
# 0 1 1 2 3 5 8 13

# OBS: a sequencia de fibonacci começa com "0" e "1" e o proximo termo é a soma dos dois anteriores.

antecessor = 0
sucessor = 1

print('Sequencia de Fibonacci')
n = int(input('Digite até qual N termo você deseja mostrar a sequencia? '))

for _ in range(n):
    print(antecessor, end=' ') 
    # aux = sucessor 
    # sucessor = antecessor + sucessor
    # antecessor = aux
    antecessor, sucessor = (sucessor, antecessor + sucessor)

print('\n') # Quebra de linha
print('Fim do Programa.')