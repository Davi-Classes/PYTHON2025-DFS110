# Soma de 5 numeros
soma = 0

for n in range(5):
    numero = float(input(f'Digite o {n+1}º numero: '))
    soma += numero

print(f'Resultado: {soma}')