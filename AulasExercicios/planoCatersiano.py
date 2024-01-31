import math

x1 = int(input('Ponto X1: '))
y1 = int(input('Ponto Y1: '))

x2 = int(input('Ponto X2: '))
y2 = int(input('Ponto Y2: '))


def distanciaPlanoCartesiano(x1, x2, y1, y2):

    pontos = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    distancia = math.sqrt(pontos)

    if distancia >= 10:
        print('longe')
    else:
        print('perto')


distanciaPlanoCartesiano(x1,x2, y1, y2)
