tempFahrenheit = float(input("Informe a temperatura Fahrenheit: "))


def conversor(tempFahrenheit):
    tempCels = (tempFahrenheit - 32) * 5 / 9
    print(f'Temperatura: {tempCels}°')


conversor(tempFahrenheit)
