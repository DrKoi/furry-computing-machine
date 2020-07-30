def Dimvector(cantidad, valorInicial=0):
    arreglo = []
    for i in range(cantidad):
        arreglo.append(valorInicial)
    return arreglo

N = int(input("Ingrese cantidad de números para buscar números primos: "))
N = N + 1
Numeros = Dimvector(N)
for i in range(N):
    Numeros[i] = i
#print(Numeros)
for i in range(2, N):
    for j in range(3, int(N/2)):
        pos = Numeros[i] * j
        if pos <= N-1:
            Numeros[pos] = 0
for i in range(N):
    if Numeros[i] > 1:
        print(Numeros[i])
