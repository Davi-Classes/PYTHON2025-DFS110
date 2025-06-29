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


funcionario1 = Funcionario('Villena', 'Gerente Operacional', 3500)
print(repr(funcionario1))


# b)
class Empresa:
    def __init__(self, funcionarios: list[Funcionario] = []):
        self.funcionarios = funcionarios

    def listar_funcionarios(self):
        print('Funcionarios: ')
        for funcionario in self.funcionarios:
            print(f'- {funcionario}')

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome: str) -> Funcionario | None:
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.nome == nome:
                self.funcionarios.pop(i)
                return funcionario

        return None
    

empresa = Empresa()
empresa.adicionar_funcionario(funcionario1)

empresa.listar_funcionarios()

print(empresa.remover_funcionario('aaaa'))
print(empresa.remover_funcionario(funcionario1.nome))