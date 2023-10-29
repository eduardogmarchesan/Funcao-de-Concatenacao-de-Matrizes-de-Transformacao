import numpy as np 
import math 
import os

def tranformacao (atual,info):
    if info[0] == 1:
        nova = tranlacao(atual,info[1],info[2])
    elif info[0] == 2:
        nova = cisalhamentoX(atual,info[1])
    elif info[0] == 3:
        nova = cisalhamentoY(atual,info[1])
    elif info[0] == 4:
        nova = escala(atual,info[1],info[2])
    elif info[0] == 5:
        nova = rotacao(atual,info[1])
    elif info[0] == 6:
        nova = reflexaoX(atual)
    elif info[0] == 7:
        nova = reflexaoY(atual)
    return nova
    


def tranlacao (atual,tx,ty):
    Mtranslacao = np.array([[1,0,tx],
                           [0,1,ty],
                           [0,0,1]])
    nova = atual.dot(Mtranslacao)
    return nova

def cisalhamentoX (atual,shx):
    McisalhamentoX = np.array([[1,shx,0],
                               [0,1,0],
                               [0,0,1]])
    nova = atual.dot(McisalhamentoX)
    return nova

def cisalhamentoY (atual,shy):
    McisalhamentoY = np.array([[1,shy,0],
                               [0,1,0],
                               [0,0,1]])
    nova = atual.dot(McisalhamentoY)
    return nova

def escala (atual,sx,sy):
    Mescala = np.array([[sx,0,0],
                        [0,sy,0],
                        [0,0,1]])
    nova = atual.dot(Mescala)
    return nova

def rotacao (atual,teta):
    Mrotacao = np.array([[math.cos(teta), (math.sin(teta) * -1),0],
                            [math.sin(teta), math.cos(teta),0],
                            [0,0,1]])
    nova = atual.dot(Mrotacao)
    return nova

def reflexaoX (atual):
    MreflexaoX = np.array([[-1,0,0],
                           [0,1,0],
                           [0,0,1]])
    nova = atual.dot(MreflexaoX)
    return nova

def reflexaoY (atual):
    MreflexaoY = np.array([[1,0,0],
                           [0,-1,0],
                           [0,0,1]])
    nova = atual.dot(MreflexaoY)
    return nova

option = None
lista = []

while option != 0:

    os.system('cls' if os.name=='nt' else 'clear')

    print("Escolha a transformação que deseja adicinar. digite:")
    print("1 para translação")
    print("2 para cisalhamento em X")
    print("3 para cisalhamento em Y")
    print("4 para escala")
    print("5 para rotação")
    print("6 para reflexão em X")
    print("7 para reflexão em Y")
    print("0 para finalizar a operação")


    info = [option, None, None]
    option = int(input())
    
    if option == 1:
        posicaoX = int(input("digite o valor de X: "))
        posicaoY = int(input("digite o valor de Y: "))
        info = [option, posicaoX, posicaoY]
    elif option == 2:
        shx = int(input("digite o valor do cisalhamento: "))
        info = [option, shx, None]
    elif option == 3:
        shy = int(input("digite o valor do cisalhamento: "))
        info = [option, shy, None]
    elif option == 4:
        sx = int(input("digite o valor da escala em X: "))
        sy = int(input("digite o valor da escala em Y: "))
        info = [option, sx, sy]
    elif option == 5:
        teta = int(input("digite o valor do ângulo: "))
        info = [option, math.radians(teta), None]
        print(math.radians(teta))
    elif option == 6:
        info = [option, None, None]
    elif option == 7:
        info = [option, None, None]
    elif option == 0: break

    lista.append(info)

atual = np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1]])

for i in range(len(lista)):
    atual = tranformacao(atual, lista[len(lista)-i-1])


print(atual)   