lados = int(input('Digite o valor correspondente ao lado de um quadrado: '))


def quadrante(lados):
    area = lados ** 2
    perimetro = lados * 4
    print(f'perímetro: {perimetro} - área: {area}')


quadrante(lados)
