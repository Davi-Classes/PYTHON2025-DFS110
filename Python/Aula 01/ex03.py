# Ex03. Faça um programa que peça 6 numeros e armazene-os em uma lista. Ao final, mostre a soma entre os numeros.
numeros = []

# Entrada
for n in range(6):
    numero = float(input(f'Digite o {n + 1}º numero: '))
    numeros.append(numero)

# Processamento
# soma = 0
# for numero in numeros:
#     soma += numero
soma = sum(numeros)


# Saída
print(f'A soma é {soma}')