class Imposto:
    def calcular(self, valor: float):
        return 0

class DAS(Imposto):
    def calcular(self, valor: float):
        return valor * 0.06

class ISS(Imposto):
    def calcular(self, valor: float):
        return valor * 0.05


class IRPJ(Imposto):
    def calcular(self, valor: float):
        return valor * 0.1

def calcular_impostos(valor_bruto: float, impostos: list[Imposto]):
    descontos = 0

    for imposto in impostos:
        descontos += imposto.calcular(valor_bruto)

    return valor_bruto - descontos

def selecionar_impostos(todos_os_impostos: list[Imposto]):
    impostos = []

    while True:
        print(' Impostos Disponiveis '.center(30, '-'))
        for i, imposto in enumerate(todos_os_impostos):
            # Buscando o Nome Da Classe
            print(f'[{i}] - {imposto.__class__.__name__}')
        print('-' * 30)
        opcao = input('Selecione o imposto que deseja incluir no calculo (Digite [C] para calcular): ')

        if opcao == 'C':
            break

        if int(opcao) < 0 or int(opcao) > len(todos_os_impostos) - 1:
            print('Opção Inválida.')
        
        imposto = todos_os_impostos.pop(int(opcao))
        impostos.append(imposto)

    return impostos


impostos_cadastrados: list[Imposto] = [DAS(), ISS(), IRPJ()]

valor_bruto = float(input('Insira o valor bruto que deseja aplicar o calculo: '))
impostos = selecionar_impostos(impostos_cadastrados.copy())

valor_liquido = calcular_impostos(valor_bruto, impostos)

print(f'Valor Bruto: {valor_bruto}')
print(f'Valor Liquido: {valor_liquido}')