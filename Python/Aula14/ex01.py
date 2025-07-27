from dataclasses import dataclass

# a)
# @dataclass
# class Funcionario:
#     nome: str
#     cpf: str
#     salario_bruto: float

#     def calcular_salario_liquido(self):
#         desconto = self.salario_bruto * 0.03
#         salario_liquido = self.salario_bruto - desconto
#         return salario_liquido


# @dataclass
# class Gerente(Funcionario):
#     setor: str


class Funcionario:
    def __init__(self, nome: str, cpf: str, salario_bruto: float):
        self.nome = nome
        self.cpf = cpf
        self.salario_bruto = salario_bruto

    def calcular_salario_liquido(self):
        desconto = self.salario_bruto * 0.03
        salario_liquido = self.salario_bruto - desconto
        return salario_liquido


class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_bruto: float, setor: str):
        super().__init__(nome, cpf, salario_bruto)
        self.setor = setor

    def calcular_salario_liquido(self):
        desconto = self.salario_bruto * 0.07
        salario_liquido = self.salario_bruto - desconto
        return salario_liquido


funcionario = Funcionario('Davi', '2398219312', 2000.0)
gerente = Gerente('Mauricio', '231245454', 10000.0, 'TI')

print('Funcionario: ')
print(funcionario.nome)
print(funcionario.cpf)
print(f'Salario Bruto: {funcionario.salario_bruto}')
print(f'Salario Liquido: {funcionario.calcular_salario_liquido()}')

print('-' * 20)
print(f'Gerente de {gerente.setor}: ')
print(gerente.nome)
print(gerente.cpf)
print(f'Salario Bruto: {gerente.salario_bruto}')
print(f'Salario Liquido: {gerente.calcular_salario_liquido()}')