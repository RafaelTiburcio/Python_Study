import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - 4 * a * c

def formula ():
    return (-b + math.sqrt(delta)) / (2 * a)

if delta == 0:
    raiz1 = formula
    print("A única raíz é: ", raiz1)

else:
    if delta < 0:
        print("Essa equação não possui raízes reais")
        
    else:
        raiz1 = formula   
        raiz2 = (-b - math.sqrt(delta)) / (2 * a) 
        print("A primeira raíz é : ", raiz1, "\nA segunda raíz é : ", raiz2)
