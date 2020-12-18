# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:31:33 2020
PROCESO DE UN ARCHIVO DIRECTO
@author: dagob
"""
# PRIMERO SE CREARÁ EL ARCHIVO PERSONAS.TXT, CUIDADNDO QUE LOS CAMPOS Y REGISTROS QUEDEN CON LONGITUD FIJA
ARCH = open("PERSONAS.TXT", "w")
Resp = "S"; cont = 0
while Resp != "N" and Resp != "n": 
    cont = cont + 1
    print(); print("Ingrese datos de la persona ", cont, " : ")
    rol = input("Rol (4 dígitos): ");  rol = (rol + "    ")[0:4]
    nombre = input("Nombre: ");  nombre = (nombre + "               ")[0:15]
    edad = input("Edad: ");  edad = (edad + "  ")[0:2]
    sexo = input("Sexo (M o F): ");   sexo = (sexo + " ")[0:1]
    print (rol, nombre, edad, sexo)
    registro = rol + nombre + edad + sexo
    print(registro)
    ARCH.write(registro)
    print(); Resp = input("¿Más personas? (S/N): ")
ARCH.close()
input()
#
# AHORA SE LEERÁ EL ARCHIVO QUE FUE CREADO
ARCH2 = open("PERSONAS.TXT", "r")
print(); print("LISTADO DE REGISTROS ALMACENADOS")
largo = 22
registro = "*"
while registro != "": 
    registro = ARCH2.read(largo)
    if registro != "":
        print(registro)  
        print("Rol: ", registro[0:4], " Nombre: ", registro[4:19], " Edad: ", registro[19:21], " Sexo: ", registro[21:22])
ARCH2.close()
print()
#
# AHORA SE 
input("FIN DE PROCESO")
