       
def primo(x):
    fator = 2 
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False   
    else: 
        return True



n = int(input("Digite um numero inteiro: "))
while n > 0:
    if primo(n):
        print(n , "é primo!")
    else:
        print(n, "Não é primo!")     
    n = int(input("Digite um numero inteiro: "))
       
       
