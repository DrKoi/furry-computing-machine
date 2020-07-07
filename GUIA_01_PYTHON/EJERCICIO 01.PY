def DIM_VECTOR(Max, Valor = 0):
    arreglo = []    
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo
NUMEROS = DIM_VECTOR(10)
for i in range(10):
    print("Ingrese numero para poblar arreglo NUMEROS[", i, "]: ", sep="", end="")
    NUMEROS[i] = int(input())

print(NUMEROS)
""" 
Haga un algoritmo que permita llenar, desde teclado, un arreglo de 10 elementos con valores
numéricos 
"""