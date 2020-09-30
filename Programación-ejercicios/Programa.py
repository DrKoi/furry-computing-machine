# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:02:24 2020
@author: dagob
"""
# Ejemplo de programacion modular (SIN variables globales). Autor: Dagoberto Cabrera. 
# Módulo que acepta datos por teclado y llena arreglos NOM y ED
class Personita(): 
    rol : 0
    nombre: "******"
    edad: 0
    sexo: "*"

def LeerDatos():
    # Se definen el arreglo ED (numérico) y NOM (strings), ambos de 100 elementos.
    print("Comienza programa")
    PER = []
    for i in range(100): 
        PER.append(Personita())

    i, resp = 0, "S"
    while (resp != "N") and (resp != "n") and (i <= 99):
        print("Ingrese Rol, Nombre, Edad y Sexo (M o F) de persona ", i+1, ": ")
        PER[i].rol = int(input("Rol: "))
        PER[i].nombre = input("Nombre: ")
        PER[i].edad  = int(input("Edad  : "))
        PER[i].sexo = input("Sexo (M o F): ")
        i = i + 1
        resp = input("¿Más personas? (S/N): ")
        print()
    N = i    # N es cantidad de personas
    return PER, N
# Fin LeerDatos

# Función que ordena los arreglos por edad
def OrdenarPorEdad(PER, N):
    for i in range (0, N-1): 
        for j in range (i+1, N): 
            if PER[i].edad > PER[j].edad: 
                aux = Personita()
                
    return (PER)
# Fin OrdenarPorEdad
       
# Procedimiento que muestra listado ordenado por edad
def Listado(PER, N): 
    print("LISTADO DE PERSONAS ")
    print()
    print("ROL     NOMBRE    EDAD  SEXO")
    print("====    ======    ====  ====")
    for i in range (0, N):
        print(" ", PER[i].rol, "   ",PER[i].nombre, "   ", PER[i].edad, "  ", PER[i].sexo)
    print("FIN DEL LISTADO")
    print()
# Fin Listado  

# Obtención Edad mínima y Edad máxima
def MinMax(NOM, ED, N):
    EdMin, EdMax, NomMin, NomMax = ED[0], ED[0], NOM[0], NOM[0]  
    for i in range(0, N):
        if ED[i] < EdMin:
            EdMin = ED[i]
            NomMin = NOM[i]
        if ED[i] > EdMax:
            EdMax = ED[i]
            NomMax = NOM[i]
    print("Edad mínima =", EdMin, ". Una persona con esa edad =", NomMin)
    print("Edad máxima =", EdMax, ". Una persona con esa edad =", NomMax)
    print()
# Fin MinMax

# Obtención promedio de edad
def Promedio(ED, N):
    Suma = 0
    for i in range (0, N):
        Suma = Suma + ED[i]
    prom = round(float(Suma/N),2)
    return prom
# Fin Prom

# PROGRAMA PRINCIPAL
PER, N = LeerDatos()

Listado(PER, N)

print(); print("Se ordenan los datos por edad"); print()
PER = OrdenarPorEdad(PER, N)

Listado(PER, N)

# print("Promedio de edad = ", Promedio(ED, N))
print()

# MinMax(NOM, ED, N)
print("FIN DE PROCESO")
input()
