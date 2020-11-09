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

raiz = crear_arbol()

print("hola mundo")