#Agregar módulo validar
def factorial(numero):
  facto = 1
  if numero > 0:
    for i in range(1, numero + 1):
      facto = facto * i
  return facto

N = int(input("Ingrese valor N: "))
M = int(input("Ingrese valor M: "))
N_FACTORIAL = factorial(N) 
M_FACTORIAL = factorial(M)

print((N_FACTORIAL)/(M_FACTORIAL * (factorial(N-M))))
