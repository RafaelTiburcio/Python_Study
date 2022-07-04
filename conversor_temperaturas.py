temperatura = float(input(
    "Olá, me diga a temperatura em Fahrenheit, que iremos converter para Celsius!"))
F = temperatura

conversor = (F - 32) * 5 / 9

print("Sua temperatura convertida para celsius é de {:.2f}".format(
    conversor), "°C")


temperaturaCelsius = float(input(
    "Agora me diga a temperatura em Fahrenheit, que iremos converter para Celsius!"))
C = temperaturaCelsius

conversorFahrenheit = (C * 9 / 5) + 32

print("Sua temperatura convertida para Fahrenheit é de {:.2f}".format(
    conversorFahrenheit), "°F")
