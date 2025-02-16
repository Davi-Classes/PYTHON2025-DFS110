idade = int(input('Digite sua idade: '))


if idade < 16:
    print('Não pode votar.')
elif (idade >= 16 and idade < 18) or idade >= 65:
    print('Voto Facultativo.')
else:
    print('Voto Obrigatório.')