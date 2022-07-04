x = input("Quantos dias voce ficara de ferias? ")
duracao_ferias = int(x)


y = input("Digite o dia do mes que voce ira viajar: ")
dia_viagem = int(y)

dia_retorno = duracao_ferias + dia_viagem
if (dia_retorno > 30):
    dia_retorno = (duracao_ferias + dia_viagem) % 30

z = input("Digite o dia da semana que voce ira viajar: ")

if (z == "Domingo"):
    z = 0
if (z == "Segunda-feira"):
    z = 1
if (z == "Terca-feira"):
    z = 2
if (z == "Quarta-feira"):
    z = 3
if (z == "Quinta-feira"):
    z = 4
if (z == "Sexta-feira"):
    z = 5
if (z == "Sabado"):
    z = 6

dia_semana_retorno = duracao_ferias % 7 + z
if (dia_semana_retorno > 6):
    dia_semana_retorno = (duracao_ferias % 7 + z) - 7

if (dia_semana_retorno == 0):
    dia_semana_retorno = "Domingo"
if (dia_semana_retorno == 1):
    dia_semana_retorno = "Segunda-feira"
if (dia_semana_retorno == 2):
    dia_semana_retorno = "Terca-feira"
if (dia_semana_retorno == 3):
    dia_semana_retorno = "Quarta-feira"
if (dia_semana_retorno == 4):
    dia_semana_retorno = "Quinta-feira"
if (dia_semana_retorno == 5):
    dia_semana_retorno = "Sexta-feira"
if (dia_semana_retorno == 6):
    dia_semana_retorno = "Sabado"

print("Voce voltara no dia", dia_retorno, dia_semana_retorno)
