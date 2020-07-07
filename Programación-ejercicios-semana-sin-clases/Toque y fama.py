def arreglo():
    global numero, azar
    numero = [0]; azar = [0]
    for i in range(1, 100):
        numero.append(0)
        azar.append(0)
        i = i + 1

def Numeroazar():
    i = 0
    azar[i] = 10
    import random as rn
    for i in range(7):
        azar[i] = rn.randint(0,9)


    """ while i < 6:
        azar[i] = rn.randint(0,9)
        while azar[i] == azar[i-1] or azar[i] == azar[i-2] or azar[i] == azar[i-3] or azar[i] == azar[i-4] or azar[i] == azar[i-5]:
            azar[i] = rn.randint(0,9)
        i = i + 1 """


def Juego():
    cont = 0
    fama = 0
    toque = 0
    while cont < 15 and fama != 6:
        i = 0
        while i < 6:
            for i in range(6) :
                numero[i] = int(input("Cifra ", i + 1,": "))


arreglo()
Numeroazar()
Juego()


""" 
-Se pide implementar el juego “Toque y Fama”, pero para números de 6 cifras. 
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