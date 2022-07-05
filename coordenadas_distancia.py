import math

ponto1 = float(input("Digite um valor que corresponderá ao eixo x de origem: "))
ponto2 = float(input("Digite um valor que corresponderá ao eixo y de origem: "))
ponto3 = float(input("Agora digite um valor que corresponderá ao eixo x de destino: "))
ponto4 = float(input("Agora digite um valor que corresponderá ao eixo y de destino: "))

formula = math.sqrt((ponto1 - ponto2) ** 2 + (ponto3 - ponto4) ** 2)

if formula > 10:
    print("longe")
    
else: 
    print("perto")

