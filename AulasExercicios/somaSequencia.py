i = input('Digite um número inteiro: ')
x = 1
tamanho = len(i)
num = int(i)
s = 0
while x <= tamanho:

    u = num % 10
    r = num // 10
    s += u
    num = r
    x += 1

print(s)
