inicio = int(input('Digite o inicio da contagem: '))
final = int(input('Digite o final da contagem: '))
passo = int(input('Digite o passo da contagem: '))

# Operador Ternário
ajuste = -1 if inicio > final else 1

for n in range(inicio, final + ajuste, passo):
    print(n)

print('Fim do Programa.')