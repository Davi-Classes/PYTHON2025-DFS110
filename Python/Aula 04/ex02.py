def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

num1 = float(input('Digite o 1º numero: '))
num2 = float(input('Digite o 2º numero: '))
num3 = float(input('Digite o 3º numero: '))

media = calcular_media(num1, num2, num3)

print(f'A média é: {media:.2f}')