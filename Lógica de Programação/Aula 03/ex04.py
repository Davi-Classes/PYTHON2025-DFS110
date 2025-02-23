numero = soma = 0

while numero >= 0:
    numero = float(input('Digite um numero (negativo p/ parar): '))
    
    if numero > 0:
        soma += numero

print(f'A soma dos valores é: {soma}')
print('Fim do Programa!')