# Funções 3
# def <nome_funcao>(...<parametros>):
#   <corpo da funcao>

# Podemos tornar um parametro opcional, definindo 
# um valor padrão para quando ele não for informado
# OBS: Somente os ultimos parametros podem ser opcionais.
def saudacao(nome = ''):
    if nome == '':
        print('Olá')
    else:
        print(f'Olá, {nome}')

saudacao()
saudacao('Camila')