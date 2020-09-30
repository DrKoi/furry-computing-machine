""" 
Realizar un algoritmo que permita llenar un arreglo de largo 9, en donde cada elemento debe
almacenar un caracter (que debe ser ingresado desde teclado). A continuación, se deberá
procesar el arreglo de tal forma que despliegue por pantalla los valores almacenados pero con
corrimiento 
"""
def DIM_VECTOR(Max, Valor = 0):
  arreglo = []    
  for i in range(Max):
    arreglo.append(Valor)
  return arreglo

A = DIM_VECTOR(9)
palabra = input("Ingrese una palabra de 9 caracteres: ")

for i in range(9):
  A[i] = palabra[i]
print(A)
for j in range(9):
  for i in range(8):
    aux = A[i]
    A[i] = A[i-1]
    A[i-1] = aux
  print(A)