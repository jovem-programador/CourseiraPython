i = input('Digite um número inteiro: ')
num = int(i)
x = 1
d = -1
t = len(i)
digitosAdjacentesIguais = False
while x <= t:
    u = num % 10
    if d == u:
        digitosAdjacentesIguais = True
        x += 1
        break
    else:
        d = u
        r = num // 10
        num = r
        x += 1

if digitosAdjacentesIguais:
    print('sim')
else:
    print('não')