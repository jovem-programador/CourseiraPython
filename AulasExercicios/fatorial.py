n = int(input('Digite o valor de n: '))

def fatorial(n):
    if n == 0 or n == 1:
        print(1)
    else:
        r = 1
        x = 2
        while x <= n:
            r *= x
            x += 1
        print(r)

fatorial(n)