# O break quebra o laço no momento que é executado.
soma = 0

while True:
    numero = float(input('Digite um numero (negativo p/ parar): '))
    
    if numero < 0:
        break # Quebra o laço

    soma += numero

print(f'A soma dos valores é: {soma}')
print('Fim do Programa!')