linha = 1  
coluna = 1 
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t")  #end não pula linha no print
        coluna = coluna + 1
        
    linha = linha + 1
    print()                #para mudar de linha 
    coluna = 1