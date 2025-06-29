# Revisão Orientação a Objetos.
class Compra:
    def __init__(self, valor_bruto: float, desconto: float):
        self.valor_bruto = valor_bruto
        self.desconto = desconto
        self.calcular_valor_liquido()

    def alterar_valor_bruto(self, valor_bruto: float):
        self.valor_bruto = valor_bruto
        self.calcular_valor_liquido()

    def calcular_valor_liquido(self):
        self.valor_liquido = self.valor_bruto * (1 - self.desconto)

    def __repr__(self):
        return f'<Compra - R${self.valor_liquido:.2f} (R${self.valor_bruto:.2f} - {self.desconto * 100}%)>'

class Cliente:
    # Metódo Construtor
    def __init__(self, nome: str, endereco: str, compras: list[Compra] = []):
        self.nome = nome
        self.endereco = endereco
        self.compras = compras

    def total_gasto(self) -> float:
        return sum([compra.valor_liquido for compra in self.compras])

    def comprar(self, compra: Compra):
        self.compras.append(compra)

    def info(self):
        print(self.nome)
        print(self.endereco)
        print(self.compras)


nome = input('Digite o nome do cliente: ')
endereco = input('Digite o endereço do cliente: ')

cliente1 = Cliente(nome, endereco)
print(cliente1.total_gasto())

compra1 = Compra(100, 0.1)
compra2 = Compra(200, 0)

cliente1.comprar(compra1)
cliente1.comprar(compra2)

print(cliente1.compras[0].valor_bruto)
print(cliente1.total_gasto())