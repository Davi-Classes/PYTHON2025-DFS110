numero1 = int(input('Digite o 1º numero: '))
numero2 = int(input('Digite o 2º numero: '))


# O elif irá ser avaliado caso o if seja "falso"
# Você pode ter quantos "elif" você quiser entre o "if" e o "else"
if numero1 > numero2:
    print(f'O maior numero é {numero1}')
elif numero1 == numero2:
    print('Os numeros são iguais.')
else:
    print(f'O maior numero é {numero2}')