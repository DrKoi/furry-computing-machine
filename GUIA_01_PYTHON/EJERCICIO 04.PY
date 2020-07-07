def DIM_VECTOR(Max, Valor = 0):
    arreglo = []    
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo
NUMEROS = DIM_VECTOR(10)
for i in range(10):
    print("Ingrese numero para poblar arreglo NUMEROS[", i, "]: ", sep="")
    if i % 2 == 0:
        print("Ingrese un número impar: ", end="")
        Valor = int(input())
        while Valor % 2 == 0:
            print("El número debe ser IMPAR")
            Valor = int(input("Vuelva a ingresar: "))
    else :
        print("Ingrese un número PAR: ", end="")
        Valor = int(input())
        while Valor % 2 != 0:
            print("El número debe ser PAR")
            Valor = int(input("Vuelva a ingresar: "))
    NUMEROS[i] = Valor
print(NUMEROS)

""" 
Realizar un algoritmo que permita llenar desde teclado un arreglo, en donde cada elemento
almacene un carácter, pero éste no debe estar ya almacenado en el mismo arreglo 
"""