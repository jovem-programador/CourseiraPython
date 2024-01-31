numero = int(input('Digite um número inteiro: '))


def primo(numero):
    x = 1
    contador = 0

    while x <= numero:
        d = numero % x

        if d == 0:
            contador += 1
        x += 1

    if contador < 1 or contador > 2:
        return 'não primo'
    else:
        return 'primo'


print(primo(numero))
