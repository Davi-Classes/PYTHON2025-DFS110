# Herança e Polimorfismo
class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0):
        self.titular = titular
        self.numero = numero

        if saldo < 0:
            raise ValueError('O saldo inicial deve ser maior ou igual a 0')

        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser maior que 0')
        
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser maior que 0')
        
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente.')
        
        self.saldo -= valor

    def transferir(self, valor: float, conta_destino: 'Conta'):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def __str__(self):
        return f'{self.titular} (Nº{self.numero}) - R${self.saldo:.2f}'

# Conta Conjunta tem tudo que conta tem, mas tem outro titular.
class ContaConjunta(Conta):
    # Polimorfismo: Se não tem o metódo, herda do pai, se tem utiliza o proprio.
    def __init__(
        self, 
        titular: str, 
        titular_secundario: str,
        numero: str, 
        saldo: float = 0
    ):
        super().__init__(titular, numero, saldo)
        self.titular_secundario = titular_secundario

    def __str__(self):
        return f'{self.titular}, {self.titular_secundario} (Nº{self.numero}) - R${self.saldo:.2f}'

# Conta Investimento tem tudo que conta tem, mas ela pode "render" 1% ao mês
class ContaInvestimento(Conta):
    def __init__(self, titular, numero, saldo = 0, juros = 0.01):
        super().__init__(titular, numero, saldo)
        self.juros = juros

    def aplicar_juros(self):
        self.saldo += self.saldo * 0.01 

# Conta Corrente tem tudo que "Conta" tem mais o cheque especial.


c1 = ContaConjunta('Davi', 'Fernanda', '0001')
print(c1)
c1.depositar(100)
print(c1)