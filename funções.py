# Uma das grandes utilidades das funções é para eliminar duplicações de codigos.
# Quando trechos de codigos aparecem varias vezes realizando a mesma coisa.
def soma (x, y):
    return x + y
print(soma(10, 20))
print(soma(-20, 1010))

def multiplica (x, y):
    return x * y
print(multiplica(4, 2))

def divide (x, y):
    return x / y
print(divide(4, 2))


def nome_do_seu_time ():  # essa função nao recebe nenhum parametro
    return "vasco"
print(nome_do_seu_time())

def vazia():              
    x = 10 + 20
    print("o valor calculado é: ", x)
print(vazia())

def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:          
        x = int(input("Digite um valor: "))
    return x