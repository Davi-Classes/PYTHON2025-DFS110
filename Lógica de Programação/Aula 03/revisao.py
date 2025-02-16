# Entrada
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

# Processamento
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    situacao = 'APROVADO'
elif media < 4:
    situacao = 'REPROVADO'
else:
    situacao = 'RECUPERACAO'


# Saída
print(f'Média: {media:.2f}')
print(f'Situação: {situacao}')
