def calcular_media(numeros):
    if len(numeros) == 0:
        return 0

    return sum(numeros) / len(numeros) 


# Entrada
# Buscando dados de um input
numeros = []

while True:
    numero = float(input('Digite um numero: '))
    numeros.append(numero)

    resp = input('Deseja Continuar [S/N]? ')
    if resp == 'N':
        break

# Entrada
# Buscando dados de um CSV
# numeros = []

# with open('numeros.csv', 'r') as file:
#     texto = file.read()
#     numeros_string = texto.split(',')

#     for num_str in numeros_string:
#         numeros.append(float(num_str))
    
# Processamento
media = calcular_media(numeros)

# Saída
print(f'A média é: {media}')