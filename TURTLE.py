import turtle                   # permite usar as funções e objetos do módulo turtle
from tkinter import Wm


cor = input(
    "Olá, Temos as seguintes opções para sua tela de fundo:"
    "\nverde claro, azul, rosa, aqua, verde-água, preto, marrom, vermelho,"
    "\nverde, cinza escuro, dourado, amarelo claro e violeta."
    "\nAgora digite sua escolha aqui:")


if (cor == "verde claro"):
    wn = turtle.Screen()        # cria uma janela gráfica
    wn.bgcolor("lightgreen")    # define a cor de fundo da janela

elif (cor == "azul"):
    wn = turtle.Screen()        # cria uma janela gráfica
    wn.bgcolor("blue")          # define a cor de fundo da janela

elif (cor == "rosa"):
    wn = turtle.Screen()
    wn.bgcolor("pink")

elif (cor == "aqua"):
    wn = turtle.Screen()
    wn.bgcolor("aqua")

elif (cor == "verde-água"):
    wn = turtle.Screen()
    wn.bgcolor("aquamarine")

elif (cor == "preto"):
    wn = turtle.Screen()
    wn.bgcolor("black")

elif (cor == "marrom"):
    wn = turtle.Screen()
    wn.bgcolor("brown")

elif (cor == "vermelho"):
    wn = turtle.Screen()
    wn.bgcolor("red")

elif (cor == "verde"):
    wn = turtle.Screen()
    wn.bgcolor("green")

elif (cor == "cinza escuro"):
    wn = turtle.Screen()
    wn.bgcolor("darkgrey")

elif (cor == "dourado"):
    wn = turtle.Screen()
    wn.bgcolor("gold")

elif (cor == "amarelo claro"):
    wn = turtle.Screen()
    wn.bgcolor("lightyellow")

elif (cor == "violeta"):
    wn = turtle.Screen()
    wn.bgcolor("violet")

else:
    print("Desculpe, não temos essa cor disponível. Escolha uma de nossas opções.")


corTurtle = input("Agora me diga qual a cor das linhas do desenho:")

if (corTurtle == "verde claro"):
    alex = turtle.Turtle()
    alex.color("lightgreen")

if (corTurtle == "azul"):
    alex = turtle.Turtle()
    alex.color("blue")

if (corTurtle == "rosa"):
    alex = turtle.Turtle()
    alex.color("pink")

if (corTurtle == "aqua"):
    alex = turtle.Turtle()
    alex.color("aqua")

if (corTurtle == "verde-água"):
    alex = turtle.Turtle()
    alex.color("aquamarine")

if (corTurtle == "preto"):
    alex = turtle.Turtle()
    alex.color("black")

if (corTurtle == "marrom"):
    alex = turtle.Turtle()
    alex.color("brown")

if (corTurtle == "vermelho"):
    alex = turtle.Turtle()
    alex.color("red")

if (corTurtle == "verde"):
    alex = turtle.Turtle()
    alex.color("green")

if (corTurtle == "cinza escuro"):
    alex = turtle.Turtle()
    alex.color("darkgrey")

if (corTurtle == "dourado"):
    alex = turtle.Turtle()
    alex.color("gold")

if (corTurtle == "amarelo claro"):
    alex = turtle.Turtle()
    alex.color("lightyellow")

if (corTurtle == "violeta"):
    alex = turtle.Turtle()
    alex.color("violet")

else:
    print("Desculpe, não temos essa cor disponível. Escolha uma de nossas opções."
          "\nverde claro, azul, rosa, aqua, verde-água, preto, marrom, vermelho,"
          "\nverde, cinza escuro, dourado, amarelo claro e violeta."
          "\nAgora digite sua escolha aqui:")


linhaSize = int(
    input("Agora, me diga uma espessura para as linhas ( de 1 até 10)"))

if linhaSize == 1:
    alex.pensize(1)

elif linhaSize == 2:
    alex.pensize(2)

elif linhaSize == 3:
    alex.pensize(3)

elif linhaSize == 4:
    alex.pensize(4)

elif linhaSize == 5:
    alex.pensize(5)

elif linhaSize == 6:
    alex.pensize(6)

elif linhaSize == 7:
    alex.pensize(7)

elif linhaSize == 8:
    alex.pensize(8)

elif linhaSize == 9:
    alex.pensize(9)

elif linhaSize == 10:
    alex.pensize(10)

else:
    print("Definição de linha fora do tamanho permitido.")


alex.forward(150)        # manda o alex se mover 150 unidades para frente
alex.left(90)            # roda de 90 graus para a esquerda
alex.forward(75)         # desenha o segundo lado do retângulo
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)


wn.exitonclick()


# função turtle:

#import turtle
# wn = turtle.Screen()     # cria uma janela gráfica
# alex = turtle.Turtle()   # cria um turtle chamado alex
# alex.forward(150)        # manda o alex se mover 150 unidades para frente
# alex.left(90)            # roda de 90 graus para a esquerda
# alex.forward(75)         # desenha o segundo lado do retângulo
#wn = turtle.Screen()
# wn.bgcolor("lightgreen")         # define a cor de fundo da janela

#tess = turtle.Turtle()
# tess.color("blue")               # tess fica azul
# tess.pensize(3)                  # define a espessura da caneta

# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# wn.exitonclick()
