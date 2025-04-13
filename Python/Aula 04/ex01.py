def multiplicar(n1, n2):
    return n1 * n2


def main():
    numero1 = float(input('Digite o 1º numero: '))
    numero2 = float(input('Digite o 2º numero: '))

    resultado = multiplicar(numero1, numero2)

    print(f'{numero1} x {numero2} = {resultado}')


main()