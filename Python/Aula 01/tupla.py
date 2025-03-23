# Tupla
# É uma sequencia de valores de qualquer tipo que não pode ser alterada.
# Indexada Ordenada
#               0      1    2     3
minha_tupla = ('Davi', 21, 1.72, True) 
outra_tupla = ('Valor',)

# Acessando Valores
print(minha_tupla[0])
print(minha_tupla[1])
print(outra_tupla)

# Alterando (Não é possivel)
# minha_tupla[1] = 22

# Desempacotamento
nome, idade, altura, tem_pet = minha_tupla