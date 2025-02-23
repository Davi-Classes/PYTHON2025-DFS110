soma = 0 # Variavel acumuladora
contador = 0

qtd_numeros = int(input('Quantos numeros deseja somar?'))

while contador < qtd_numeros:
    numero = float(input('Digite um numero: '))
    soma += numero # Acumulando os numeros somando-os na variavel "soma"
    contador += 1

print(f'A soma dos numeros é: {soma}')