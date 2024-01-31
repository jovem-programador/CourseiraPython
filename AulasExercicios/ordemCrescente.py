a = int(input('Informe um numero inteiro: '))
b = int(input('Informe outro numero inteiro: '))
c = int(input('Informe outro numero inteiro: '))


def ordemCres(a, b, c):
    if a < b and b < c:
        print('crescente')
    else:
        print('não está em ordem crescente')


ordemCres(a, b, c)
