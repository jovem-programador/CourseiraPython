import math

# Raiz quadrada - print(math.sqrt(5))

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))


def deltaCalculo(a, b, c):

    delta = (b ** 2) - 4 * a * c
    bhaskara(a, b, c, delta)


def bhaskara(a, b, c, delta):

    if delta < 0:
        print('esta equação não possui raízes reais')
    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print(f'a raiz desta equação é {x1}')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        # Ordem crescente
        #if x1 > x2:
            #x1, x2 = x2, x1

        print(f'as raízes da equação são {x1} e {x2}')


deltaCalculo(a, b, c)
