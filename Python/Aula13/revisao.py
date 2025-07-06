# Ex01. 
# a) Implemente uma classe chamada "Funcionario" que deve conter os atributos:
# - nome (string)
# - cargo (string)
# - salario (float)

# b) Implemente uma classe chamada "Empresa" que deve conter:
# - funcionarios (list[Funcionarios])

# e também os metódos:
# - listar_funcionarios()
# - adicionar_funcionario(funcionario: Funcionario)
# - remover_funcionario(nome: str)
# a)
class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f'{self.nome} ({self.cargo})'

    def __repr__(self):
        return f'<Funcionario - {self.nome} ({self.cargo})>'


class Empresa:
    def __init__(self, funcionarios: list[Funcionario] = []):
        self.funcionarios = funcionarios

    def listar_funcionarios(self):
        print('Funcionários: ')
        for funcionario in self.funcionarios:
            print(f'- {funcionario}')

    def adicionar_funcionario(self, funcionario: Funcionario):
        for funcionario_atual in self.funcionarios:
            if funcionario_atual.nome == funcionario.nome:
                raise ValueError('Funcionário já está cadastrado.')

        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome: str):
        for index, funcionario in enumerate(self.funcionarios):
            if funcionario.nome == nome:
                self.funcionarios.pop(index)
                return
        
        raise ValueError('Funcionário não encontrado.')


funcionario1 = Funcionario('Villena', 'Gerente Operacional', 3500)
funcionario2 = Funcionario('Maria', 'Gerente', 10000)

empresa = Empresa()

# empresa.listar_funcionarios()
empresa.adicionar_funcionario(funcionario1)

# Aqui ele vai dar o error.
try:
    empresa.adicionar_funcionario(funcionario1)
except ValueError as err:
    print(err)

empresa.listar_funcionarios()

try:
    empresa.remover_funcionario('Villena')
except ValueError as err:
    print(err)

print(empresa.funcionarios)
