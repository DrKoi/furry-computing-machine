def DIM_VECTOR(Max, Valor = 0):
  arreglo = []    
  for i in range(Max):
    arreglo.append(Valor)
  return arreglo

A = DIM_VECTOR(41)
B = DIM_VECTOR(41)
C = DIM_VECTOR(41)
D = DIM_VECTOR(41)
E = DIM_VECTOR(41)
A[0] = "Nombre"
B[0] = "Certamen 1"
C[0] = "Certamen 2"
D[0] = "Certamen 3"
E[0] = "Promedio"

for i in range(1, 41, 1):
  A[i] = input("Nombre Alumno: ")
  B[i] = float(input("Certamen 1: "))
  D[i] = float(input("Certamen 3: "))
  C[i] = float(input("Certamen 2: "))

for i in range(1, 41):
  E[i] = (B[i] + C[i] + D[i])/3
for i in range(41):
  print(A[i], B[i], C[i], D[i], E[i])