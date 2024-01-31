a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))


def fatorial(n):
    if n == 0 or n == 1:
        return 1

    else:
        r = 1
        x = 2
        while x <= n:
            r *= x
            x += 1

        return r


def testeFatorial():
    if fatorial(1) == 1:
        print('Funciona para 1')
    else:
        print('Não funciona para 1')

    if fatorial(2) ==2:
        print('Funciona para 2')
    else:
        print('Não funciona para 2')

    if fatorial(0) == 1:
        print('Funciona para 0')
    else:
        print('Não funciona para 0')

    if fatorial(5) == 120:
        print('Funciona para 5')
    else:
        print('Não funciona para 5')


def coeficienteBinomial(n, k):

    calculo = fatorial(n) / (fatorial(k) * (fatorial(n - k)))
    return calculo



if not a < 0 or b < 0:
    print(coeficienteBinomial(a, b))
else:
    print('Erro!! Não aceitamos números negativos')
