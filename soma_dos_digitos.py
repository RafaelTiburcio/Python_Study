x = int(input("Numero: "))

soma = 0

while (x != 0):
    resto = x % 10
    print("O resto é ", resto)
    x = (x - resto)//10
    print("o valor de x é: ", x)
    soma = soma + resto
print(" O valor da soma dos digitos é: ", soma)
      
    
    
