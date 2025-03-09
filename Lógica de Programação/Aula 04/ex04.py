# Variavel Acumuladora
qtd_vogais = 0

print('Contador de Vogais')
texto = input('Digite um texto qualquer: ')


for letra in texto:
    # if letra.upper() in ('A', 'E', 'I', 'O', 'U'):
    if letra.upper() in 'AEIOU':
        qtd_vogais += 1

print(f'A quantidade de vogais é: {qtd_vogais}')