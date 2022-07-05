seq = int(input("Digite o tamanho da sequência que será somada: "))

soma = 0
i = 0
while i < seq:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    i = i + 1
    
print("A soma dos valores digitados é: ", soma)