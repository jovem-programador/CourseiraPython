primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
terceira = float(input('Digite a terceira nota: '))
quarta = float(input('Digite a quarta nota: '))


def media(primeira, segunda, terceira, quarta):
    total = primeira + segunda + terceira + quarta
    media = total // 4
    print(f'A média aritmética é {media}')


media(primeira, segunda, terceira, quarta)
