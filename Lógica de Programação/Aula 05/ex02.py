soma = 0
qtd_numeros = int(input('Digite quantos numeros deseja calcular a média: '))

for n in range(qtd_numeros):
    numero = float(input(f'Digite o {n+1}º numero: '))
    soma += numero

media = soma / qtd_numeros
print(f'A média dos numeros é {media:.2f}')
