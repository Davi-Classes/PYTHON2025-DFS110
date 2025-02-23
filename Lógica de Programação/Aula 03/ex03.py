contador = 0
soma = 0 # Variavel acumuladora

while contador < 3:
    numero = float(input('Digite um numero: '))
    soma += numero # Acumulando os numeros somando-os na variavel "soma"
    contador += 1

print(f'A soma dos numeros é: {soma}')