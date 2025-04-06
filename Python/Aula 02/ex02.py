aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['notas'] = []

for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    aluno['notas'].append(nota)

aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
aluno['situacao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'

print('----- Aluno ------')
for chave, valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')