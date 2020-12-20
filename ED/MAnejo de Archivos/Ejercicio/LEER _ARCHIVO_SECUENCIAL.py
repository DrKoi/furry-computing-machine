# -*- coding: utf-8 -*-

Archivo = open('PERSONAS.DAT', 'r')
Registro = Archivo.readline().strip()
while Registro != '':
    Datos = Registro.split(';')
    print(Datos)
    Registro = Archivo.readline().strip()
Archivo.close()