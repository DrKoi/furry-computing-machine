# -*- coding: utf-8 -*-
class tipo_nodo():
    valor = ""
    LEFT = None
    RIGHT = None

def crear_arbol():
    nodo_raiz = tipo_nodo()
    nodo_raiz.valor = "A"

    nodo_B = tipo_nodo()
    nodo_B.valor = "B"
    nodo_raiz.LEFT = nodo_B

    nodo_D = tipo_nodo()
    nodo_D.valor = "D"
    nodo_B.LEFT = nodo_D

    nodo_E = tipo_nodo()
    nodo_E.valor = "E"
    nodo_B.RIGHT = nodo_E

    nodo_I = tipo_nodo()
    nodo_I.valor = "I"
    nodo_E.LEFT = nodo_I

    nodo_J = tipo_nodo()
    nodo_J.valor = "J"
    nodo_E.RIGHT = nodo_J

    nodo_C = tipo_nodo()
    nodo_C.valor = "C"
    nodo_raiz.RIGHT = nodo_C

    nodo_F = tipo_nodo()
    nodo_F.valor = "F"
    nodo_C.LEFT = nodo_F
    return nodo_raiz

def pre_orden(Puntero):
    global valor_buscado
    if Puntero != None:
        print(Puntero.valor)
        if Puntero.valor == valor_buscado:
            print("Lo encontré")
        pre_orden(Puntero.LEFT)
        pre_orden(Puntero.RIGHT)

def in_orden(Puntero):
    global valor_buscado
    if Puntero != None:
        in_orden(Puntero.LEFT)
        print(Puntero.valor)
        if Puntero.valor == valor_buscado:
            print("Lo encontré")
        in_orden(Puntero.RIGHT)

def post_orden(Puntero):
    global valor_buscado
    if Puntero != None:
        post_orden(Puntero.LEFT)
        post_orden(Puntero.RIGHT)
        print(Puntero.valor)
        if Puntero.valor == valor_buscado:
            print("Lo encontré")
        

""" def modulo():
    variable = input()
    if variable != "X":
        MODULO()
        print(variable) """


raiz = crear_arbol()
valor_buscado = input("Ingrese una letra: ")
pre_orden(raiz) 
print()
in_orden(raiz)
print()
post_orden(raiz)