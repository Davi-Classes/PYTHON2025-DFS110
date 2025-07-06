# Ex01. Crie uma classe Conta.

# A classe Conta representa uma conta bancária simples e deve conter:

#     Atributos:
#         titular (str): Nome da pessoa dona da conta.
#         numero (str): Número identificador da conta.
#         saldo (float, opcional): Valor inicial da conta. Deve ser maior ou igual a zero. Caso não seja informado, deve assumir 0.

#     Métodos:
#         depositar(valor: float): Adiciona o valor informado ao saldo da conta.
#         sacar(valor: float): Remove o valor do saldo, se houver saldo suficiente. Caso contrário, uma mensagem de erro deve ser exibida.
#         transferir(valor: float, conta_destino: 'Conta'): Transfere o valor da conta atual para conta_destino, utilizando o método sacar e, se bem-sucedido, o método depositar.
class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0):
        self.titular = titular
        self.numero = numero

        if saldo < 0:
            raise ValueError('O saldo inicial deve ser maior ou igual a 0')

        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser maior que 0')
        
        self.__saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser maior que 0')
        
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente.')
        
        self.__saldo -= valor

    def transferir(self, valor: float, conta_destino: 'Conta'):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def __str__(self):
        return f'{self.titular} (Nº{self.numero}) - R${self.saldo:.2f}'


c1 = Conta('Davi', '00001', 100)
c2 = Conta('Renato', '00002', 10000)


try:
    valor = float(input('Quanto deseja depositar? '))
    c1.depositar(valor)
    print(f'Valor de R${valor:.2f} depósitado com sucesso.')
except ValueError as err:
    print(err)

# Sacar
print(c1)

try:
    valor = float(input('Quanto deseja sacar? '))
    c1.sacar(valor)
    print(f'Valor de R${valor:.2f} sacado com sucesso.')
except ValueError as err:
    print(err)

# Transferir
print(c1)
print(c2)

try:
    valor = float(input('Quanto deseja transferir? '))
    c1.transferir(valor, c2)
    print(f'Valor de R${valor:.2f} transferido com sucesso para a conta Nº{c2.numero}.')
except ValueError as err:
    print(err)


print(c1)
print(c2)
