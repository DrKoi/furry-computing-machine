def DIM_VECTOR(Max, Valor = ""):
    arreglo = []    
    for i in range(Max):
        arreglo.append(Valor)
    return arreglo

cantidad_caracteres = int(input("Ingrese número de caracteres con los que trabajar: "))
CARACTERES = DIM_VECTOR(cantidad_caracteres)
for i in range(cantidad_caracteres):
    print("Ingrese un carácter para poblar arreglo CARACTERES[", i, "]: ", sep="")
    Valor = input() #Ingresa "Valor" para trabajar con ese valor, al final se agrega a la lista
    while len(Valor) != 1:
        print("Ingrese un solo carácter: ")
        Valor = input()
    
    existe = True
    while existe:
        existe = False
        for j in range(i):
            if Valor == CARACTERES[j]:
                existe = True 
        if existe:
            print("Este carácter ya existe, vuelva a ingresar un carácter: ")
            Valor = input()
            while len(Valor) != 1:
                print("Ingrese un solo carácter: ")
                Valor = input()
    CARACTERES[i] = Valor #Aquí se agrega la varable a la lista
print(CARACTERES)

""" 
Realizar un algoritmo que permita llenar desde teclado un arreglo, en donde cada elemento
almacene un carácter, pero éste no debe estar ya almacenado en el mismo arreglo 
"""