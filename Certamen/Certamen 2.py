# Kevin Figueroa Cueto 192-A
# al principio uso una función para asignar la cantidad de elementos a los arreglos
# luego viene la lectura y validación
# ocupé un switch con true y false para la validación de los datos ordenados, despues un if para ver si termina o sigue

def vector(cantidad, valorinicial=0):
  arreglo = []
  for i in range(cantidad):
    arreglo.append(valorinicial)
  return arreglo
A = vector(50); B = vector(50); C = vector(100)

# Leer y validar cantidad de datos
n = int(input("Cantidad de datos a ingresar en arreglo A: "))
while n > 50:
  print("Debe ser menor o igual a 50")
  n = int(input("Vuelva a ingresar cantidad de datos al arreglo A: "))

m = int(input("Cantidad de datos a ingresar en arreglo B: "))
while m > 50:
  print("Debe ser menor o igual a 50")
  m = int(input("Vuelva a ingresar cantidad de datos al arreglo B: "))

# Ingreso de datos
i = 0; contador_a = 0
while i < n:
  A[i] = int(input("Ingrese un dato a A: "))
  if A[i] != A[i-1]:
    i = i + 1
    contador_a = contador_a + 1 
print(A)

j = 0; contador_b = 0
while j < m:
  B[j] = int(input("Ingrese un dato a B: "))
  if B[j] != B[j-1]:
    j = j + 1
    contador_b = contador_b + 1
print(B)

# Validar si estan ordenados
sw = False
for i in range(n):
  if A[i] < A[i-1]:
    sw = True
for j in range(m):
  if B[j] < B[j-1]:
    sw = True

# Si están ordenados el programa sigue, si no están ordenas salta al 'else' y termina el proceso
if sw == False:
  i = 0; j = 0; k = 0
  while i != n or j != m: # En esta parte no se ejecuta bien, lo que intenté fue asignar el valor menor y aumentar el indice del arreglo del cual se tomó el valor menor
    if A[i] <= B[j]:
      if i < n:
        C[k] = A[i]
        i = i + 1
        k = k + 1
    elif B[j] < A[i]:
      if j < m:
        C[k] = B[j]
        j = j + 1
        k = k + 1
  contador_repetidos_C = 0
  for k in range(contador_a + contador_b): # Se supone que contiene los datos de la suma de ambos arreglos leídos
    print(C[k])
    if C[k] == C[k-1]:
      contador_repetidos_C = contador_repetidos_C + 1
  print("Cantidad de datos leida por teclado:", contador_a + contador_b, "(total)  A: ", contador_a, "  B: ", contador_b)
  print("Cantidad de datos repetidos en C: ", contador_repetidos_C)

else:
  print("Error. Los valores no están ordenados.")
  print("Cantidad de datos alcanzados a leer: ", contador_a + contador_b, "(total)  A: ", contador_a, "  B: ", contador_b)


input("FIN DE PROCESO")