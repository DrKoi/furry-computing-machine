def DIM_VECTOR(Max, Valor = 0):
    arreglo = []    
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo

n = int(input("Ingrese cantidad de valores con los que trabajar: "))
A = DIM_VECTOR(n)
A2 = DIM_VECTOR(n)
B = DIM_VECTOR(n)
for i in range(n):
    numero = int(input("Ingrese un número positivo: "))
    while numero < 0:
        print("Error. Debe ser un valor positivo.")
        numero = int(input("Vuelva a ingresar el número: "))
    A[i] = numero
    A2[i] = numero

q = 0
for i in range(n):
    q = q + A[i]
for i in range(n):
    aux = q
    for j in range(n): 
        if aux > A2[j] and (B[i-1] < A2[j] or B[i-1] == A2[j]) and A2[j] >= 0:
            aux = A2[j]
            aux2 = j
    B[i] = aux
    A2[aux2] = -1

print("A:", A)
print("B:", B)

""" 
Realizar un algoritmo que permita llenar desde teclado un arreglo con números positivos y que
luego genere un segundo arreglo con los datos del primero, pero ordenado de menor a mayor 
"""