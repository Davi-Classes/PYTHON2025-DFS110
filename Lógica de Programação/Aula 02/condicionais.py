# Uma pessoa quer entrar em uma boate +18
ano_atual = 2025
ano_nascimento = int(input('Em que ano você nasceu? '))

idade = ano_atual - ano_nascimento

# if <condicao>
# se a condição for verdadeira, então ele 
# executa o bloco do if
# se for falsa, então ele executa o bloco do else
if idade >= 18: 
    print('Pode passar!')
else:
    print('Você não pode entrar na boate!')