def dimvector(a, b=0):
    arreglo = []
    for i in range(a):
        arreglo.append(b)
    return arreglo

print("Programa para saber si una palabra es palindrome")
palabra_original = input("Ingrese una palabra: ")
palabra = palabra_original.upper()
n = len(palabra_original)
A = dimvector(n)

I = 0
while I <= len(A)-1 and I <= len(palabra)-1:
    A[I] = palabra[I]
    I = I + 1

""" i = 0; j = n - 1; Sw = False
while i != 0:
    if A[i] != A[j]:
        Sw = True
    i = i + 1
    j = j - 1 """
print(A)
sw = False
for i in range(n):
    if A[i] != A[-(i+1)]:
        sw = True
if sw == False:
    print("Palíndrome")
else:
    print("No es Palíndrome")