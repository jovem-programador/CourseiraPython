segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))


def conversor(segundos):
    horas = segundos // 3600 % 24
    segundosRestantes = segundos % 3600
    minutos = segundosRestantes // 60
    segundosRestantesFinal = segundosRestantes % 60

    # Convertendo Hora para Dias > 24
    dia = segundos // 86400
    print(f'{dia} dias, {horas} horas, {minutos} minutos e {segundosRestantesFinal} segundos.')


conversor(segundos)
