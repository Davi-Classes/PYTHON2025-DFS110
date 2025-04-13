# Funções 2
# def <nome_funcao>(...<parametros>):
#   <corpo da funcao>

# Parametros: As variaveis na definição da função.
def saudacao(nome):
    print(f'Olá, {nome}')

# Argumentos: Os valores que passamos para os parametros.
nome1 = 'Pedro'
saudacao(nome1)

nome2 = input('Digite um nome: ')
saudacao(nome2)