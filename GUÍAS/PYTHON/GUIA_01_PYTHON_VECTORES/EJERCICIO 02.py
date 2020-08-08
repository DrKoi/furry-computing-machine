def DIM_VECTOR(Max, Valor = 0):
    arreglo = []    
    for j in range(Max):
        arreglo.append(Valor)
    return arreglo
    
NUMEROS = DIM_VECTOR(10)
for i in range(10):
    print("Ingrese numero para poblar arreglo NUMEROS[", i, "]: ", sep="", end="")
    Valor = int(input())
    while Valor % 2 != 0:
        print("El número debe ser par:")
        Valor = int(input("Vuelva a ingresar: "))
    NUMEROS[i] = Valor
print(NUMEROS)

""" 
Realizar un algoritmo que permita poblar (llenar) un arreglo con valores ingresados por
teclado, aceptando sólo aquellos datos cuyo valor sea par 
"""