def DIM_VECTOR(Max, Valor = 0):
    arreglo = []    
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo

numero = int(input("Ingrese un número entero positivo de no más de 10 Cifras: "))
while len(str(numero)) > 10 or numero < 0:
        print("Error. Debe ser un valor positivo de hasta 10 cifras.")
        numero = int(input("Vuelva a ingresar el número: "))
n = len(str(numero))
A = DIM_VECTOR(10)

for i in range(n):
  A[i] = int(str(numero)[i])

print(A)



"""
Realizar un algoritmo que lea desde teclado un número entero positivo, luego cada dígito debe
quedar almacenado en un elemento de un arreglo de largo máximo 10
"""