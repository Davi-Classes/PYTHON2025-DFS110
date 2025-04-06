letras = {}
texto = input('Digite um texto para contar as letras: ')

for caractere in texto:
    if caractere == ' ':
        continue
    
    caractere = caractere.lower()
    if letras.get(caractere) is None:
        letras[caractere] = 1
    else:
        letras[caractere] += 1


print(letras)

# Ordenando Dicionário
# letras_em_ordem_alfabetica = dict.fromkeys(sorted(letras.keys()))

# for caractere, quantidade in letras.items():
#     letras_em_ordem_alfabetica[caractere] = quantidade

# print(letras_em_ordem_alfabetica)
