# Maior primo
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


def maior_primo(num):

    while primo(num) != 'primo':
        num -= 1

    return num
