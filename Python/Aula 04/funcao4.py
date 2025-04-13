# Funções 4
# def <nome_funcao>(...<parametros>):
#   <corpo da funcao>
#   return <saida>

# O "return", permite que a gente envie um valor para o local onde a função foi chamada.
def saudacao(nome = ''):
    if nome == '':
        return 'Olá'
    else:
        return f'Olá, {nome}'


nome = input('Digite seu nome (<ENTER> caso não queira informar): ')
mensagem = saudacao(nome)
print(mensagem)