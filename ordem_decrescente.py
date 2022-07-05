decrescente = True
nAnterior = int(input("Digite o primeiro numero da sequencia: "))

valor = 1

while valor != 0 and decrescente :
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > nAnterior:
        decrescente = False
    nAnterior = valor    

if decrescente:
    print("A sequência está em ordem decrescente!")
else:
    print("A sequência não está em ordem decrescente!")