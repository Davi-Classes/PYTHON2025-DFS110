# Quero saber quantas pessoas são maior de idade
# dentre 5 pessoas
qtd_maior_de_idade = 0 # Acumulador

for p in range(5):
    idade = int(input('Digite a sua idade: '))

    if idade >= 18:
        # Ao longo do for ela vai acumulando valores
        qtd_maior_de_idade += 1

print(qtd_maior_de_idade)