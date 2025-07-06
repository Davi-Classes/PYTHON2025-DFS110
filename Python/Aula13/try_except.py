# Try Except

# Tente executar
try:
    numero = float(input('Digite um numero: '))
    print(numero)
# Caso ocorra um Error
except Exception as err:
    print(err)
# Sempre será chamado
finally:
    print('Sempre fui chamado.')