# Escopos
# Global
nome = 'Davi' # Escopo Global

def mostrar_nome():
    print(nome) # Mostrando Variavel de Escopo Global

print(nome)
mostrar_nome()

# Local
nome = 'Davi' # Escopo Global

def mostrar_nome():
    nome = 'Carlos' # Escopo Local (nome local != nome global)
    print(nome)

print(nome)
mostrar_nome()

# Alterando Variaveis Global em Funções
nome = 'Davi' # Escopo Global

def mostrar_nome():
    global nome # Informando que no escopo da função, nome será refenciado a global
    nome = 'Carlos' # Agora essa variavel que está sendo alterada é a global
    print(nome)

mostrar_nome()
print(nome)
