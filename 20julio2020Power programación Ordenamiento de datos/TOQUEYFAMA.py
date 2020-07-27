def DIM_VECTOR(Max, Valor = 0):
    arreglo = []
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo

A = DIM_VECTOR(6)
B = DIM_VECTOR(6)
import random as rn
for i in range(6):
    A[i] = rn.randint(0,9)
for i in range(6):
	existe = True
	while existe:
		existe = False
		for j in range(i):
			if A[i] == A[j]:
				existe = True
			if existe:
				A[i] = rn.randint(0,9)
print(A)
cont = 15; fama = 0; toque = 0
while cont > 0 and (fama != 6 and toque != 6):
	B = DIM_VECTOR(6)
	print("Toque y Fama. Le quedan ", cont, "turnos")
	cont = cont - 1
	print("Debe ingresar el valor de 6 cifras con que trabajar: ")
	for i in range(6):
		B[i] = int(input("Ingrese un digito (entre 0 y 9): "))
		while len(str(B[i])) > 1:
					print("Ingrese los números de a uno")
					B[i] = int(input("Ingrese digito (uno por vez): "))
		existe = True
		while existe:
			existe = False
			for j in range(i):
				if B[i] == B[j]:
					existe = True 
			if existe:
				print("Error. El valor está repetido.")
				B[i] = int(input("Ingrese un digito (entre 0 y 9): "))
				while len(str(B[i])) > 1:
					print("Ingrese los números de a uno")
					B[i] = int(input("Ingrese digito (uno por vez): "))
	print(B)
	fama = 0; toque = 0
	for i in range(6):
		if A[i] == B[i]:
			fama = fama + 1
		for j in range(6):
			if B[i] == A[j]:
				toque = toque + 1
	print("Toque: ", toque, "Fama: ", fama)


""" 
Se pide implementar el juego “Toque y Fama”, pero para números de 6 cifras. 
-Primero el computador generará al azar un número de 6 cifras (todas diferentes) 
que no mostrará (por ejemplo  5 0 3 9 4 2). 
-El usuario tendrá 15 oportunidades para adivinar el número. 
Cada vez ingresará un número de 6 cifras (leerlas por separado y validar que sean diferentes). 
El computador le indicará el número de Famas y de Toques. 
Por ejemplo, si el usuario digita  7 4 2 9 1 6, el computador debe indicar “1 Fama, 2 toques”. 
-El programa debe terminar al cumplirse 15 intentos o al tener la 6 Famas. 
-Trabajar con 2 arreglos de 6 elementos numéricos cada uno. 

AVANZADO: Lo mismo, pero que el usuario ingrese el número de 6 cifras como un solo 
número (742916 y el programa separe las cifras para almacenarlas en el arreglo B). 
"""