def DIM_VECTOR(Max, Valor = 0):
    arreglo = []
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo

A = DIM_VECTOR(6)
B = DIM_VECTOR(6)
import random as rn
for i in range(6):
    A[i] = rn.randint(0,9)
    existe = True
    while existe:
        existe = False
        for j in range(i):
            if A[i] == A[j]:
                existe = True 
            if existe:
                A[i] = rn.randint(0,9)
cont = 15; fama = 0; toque = 0
while cont > 0 and fama != 6 and toque != 6:
    print("Toque y Fama. Le quedan ", cont, "turnos")
    numero = int(input("Ingrese un número para jugar 'Toque y Fama': ", sep=""))
    while numero < 0 or numero > 9:
        print("El número ingresado debe estar entre 0 y 9")
        numero = int(input("Ingrese un número para jugar 'Toque y Fama': ", sep=""))
    
    

""" 
Se pide implementar el juego “Toque y Fama”, pero para números de 6 cifras. 
-Primero el computador generará al azar un número de 6 cifras (todas diferentes) 
que no mostrará (por ejemplo  5 0 3 9 4 2). 
-El usuario tendrá 15 oportunidades para adivinar el número. 
Cada vez ingresará un número de 6 cifras (leerlas por separado y validar que sean diferentes). 
El computador le indicará el número de Famas y de Toques. 
Por ejemplo, si el usuario digita  7 4 2 9 1 6, el computador debe indicar “1 Fama, 2 toques”. 
-El programa debe terminar al cumplirse 15 intentos o al tener la 6 Famas. 
-Trabajar con 2 arreglos de 6 elementos numéricos cada uno. 

AVANZADO: Lo mismo, pero que el usuario ingrese el número de 6 cifras como un solo 
número (742916 y el programa separe las cifras para almacenarlas en el arreglo B). 
"""