""" 
Realizar un algoritmo que llene un arreglo de largo 10 (par) e intercambie los elementos,
el primero con el último, el segundo con el penultimo y así sucesivamente
"""
def DIM_VECTOR(Max, Valor = 0):
    arreglo = []    
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo

numero = int(input("Ingrese un número entero positivo: "))
while numero < 0:
        print("Error. Debe ser un valor positivo.")
        numero = int(input("Vuelva a ingresar el número: "))
A = DIM_VECTOR(len(str(numero)))
n = 0
for i in range(len(str(numero))):
  A[i] = int(str(numero)[i])
  n += 1
print(A)

for i in range(int(n/2)):
  aux = A[i]
  A[i] = A[(-i)-1]
  A[(-i)-1] = aux
print(A)