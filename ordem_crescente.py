from operator import truediv


crescente =  True

nAnterior = int(input("Digite o primeiro numero da sequencia:"))

valor = 1

while valor != 0 and crescente:
    valor = int(input("Digite o proximo numero da sequencia:"))
    if valor < nAnterior:
        crescente = False
        nAnterior = valor
        
if crescente:
    print("Essa seguqencia esta em ordem crescente!")
else:
    print("Essa sequencia não esta em ordem crescente!")