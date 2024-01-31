"""
#Estrutura de repetição while
i = 0
while i <= 20:
    print(2 ** i)
    i += 1

i = int(input('Digite o tamanho da sequência de números: '))
x = 0
produto = 1

while x < i:
    valor = int(input('Digite um valor a ser multiplicado: '))
    produto *= valor
    x += 1

print(f'Valor multiplicado:  {produto}')

i = input('Informe um número: ')
x = 1
tamanho = len(i)
num = int(i)
s = 0
print(f'Número: {num}')
while x <= tamanho:

    u = num % 10
    r = num // 10
    s += u
    num = r
    x += 1
    print(f'Número: {num}, Ultimo: {u}, Soma: {s}')

print(f'Soma: {s}')


#Aula
decrescente = True
anterior = int(input('Digite o primeiro numero: '))
valor = 1

while valor != 0 and decrescente:
    valor = int(input('Digite um número da sêquencia: '))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print('A sequencia está em ordem decrescente')
else:
    print('A sequencia não está em ordem decrescente')

meuCartao = int(input('Digite o numero do seu cartão de credito: '))
cartaoLido = 1
encontreiMeuCartão = False

while cartaoLido != 0 and not encontreiMeuCartão:

    cartaoLido =  int(input('Digite o numero do proximo cartão de credito: '))

    if cartaoLido == meuCartao:
        encontreiMeuCartão = True

if encontreiMeuCartão:
    print('EBA!! Meu cartão está lá')
else:
    print('Meu cartão não está lá')


i = input('Digite a sua sequencia: ')
num = int(i)
x = 1
d = -1
t = len(i)
digitosAdjacentesIguais = False
while x <= t:
    u = num % 10
    if d == u:
        print(f'Tem dois digitos adjacentes iguais {d} e {u} !!')
        digitosAdjacentesIguais = True
        x += 1
        break
    else:
        d = u
        r = num // 10
        num = r
        x += 1

if digitosAdjacentesIguais:
    print('OBA!!')
else:
    print('Não tem digitos adjacentes iguais')


terminou = False

p = i = 0

while (not terminou):

    n = int(input("Digite um número, ou zero para terminar: "))

    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)
"""

def main():
    num = int(input('Infome a sequencia de inteiros: '))
    soma = 0

    while num != 0:
        soma += num
        num = int(input("Digite um inteiro [0 para terminar]: "))

    print('A soma foi: ', soma)

main()