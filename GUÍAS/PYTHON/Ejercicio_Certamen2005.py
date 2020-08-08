""" 
Se pide simular el comportamiento de 2 gusanos dentro de un cuadrado de 15x15, rodeado de paredes.
Cada gusano siempre ocupará un solo casillero y se podrá mover a lo más a un casillero contiguo. Al principio el
gusano 1 estará en esquina superior izquierda del cuadrado y el gusano 2 estará en la esquina inferior derecha.
Ambos gusanos comienzan con “gordura” 1.
Dentro del cuadrado existirán casilleros con “comida” y con “agujeros”, cuyas posiciones serán leídas como datos
al principio del programa.
Cada segundo se moverá (o intentará moverse) uno de los dos gusanos, en forma cíclica (gusano 1, gusano 2,
gusano 1 de nuevo, etc.).
Un gusano se podrá mover a un casillero contiguo, en uno de 4 sentidos (arriba, derecha, abajo o izquierda), lo
que será determinado al azar. El gusano se podrá mover sólo si no hay pared, si el casillero al que se va a mover
está desocupado, si allí hay un agujero, si hay comida o si en ese casillero está un gusano “menos gordo”. En este
último caso, el gusano menos gordo es “devorado” por el que se mueve a ese casillero y el gusano “devorador”
aumenta su gordura exactamente en la gordura que tenía el gusano devorado (por supuesto que el gusano
devorado muere). Si el gusano se mueve hacia un agujero, en ese momento muere. Si el gusano se mueve hacia
un casillero con comida, “engorda” según el valor de la comida, pero puede comer como máximo un valor de 5.
La comida disminuye en la cantidad comida.
Se pide construir un algoritmo que haga lo siguiente:
-
Lea los datos: cantidad de agujeros, cantidad de comidas, posiciones (fila, columna) de los agujeros,
posiciones (fila, columna) de las comidas y valor de cada comida (son 3 datos por cada comida).
-
Simule el comportamiento de los dos gusanos.
-
El proceso debe terminar cuando mueran todos los gusanos.
-
Al final se debe indicar cuánto tiempo duró cada gusano y qué “gordura” tenía al morir. 
"""
import random as rn

def vector(cantidad, valorInicial = 0):
  arreglo = []
  for i in range(cantidad):
    arreglo.append(valorInicial)
  return arreglo

def matrix(filas, columnas, valorInicial = 0):
  arreglo = []
  for i in range(filas):
    arreglo.append([])
    for j in range(columnas):
      arreglo[i].append(valorInicial)
  return arreglo

def movimiento_gusanos(gusano, tablero, Fila, Columna, tamaño):
  direccion = rn.randint(0,3)
  print(direccion, Fila, Columna)
  if direccion == 0 and Fila > 0: #ARRIBA
    if tablero[Fila - 1][Columna] == "[X]":
      gusano = 0
    else:
      aux = tablero[Fila][Columna]
      tablero[Fila][Columna] = 0
      tablero[Fila - 1][Columna] = tablero[Fila - 1][Columna] + aux
      Fila = Fila - 1

  if direccion == 1 and Columna < tamaño - 1: #DERECHA
    if tablero[Fila][Columna + 1] == "[X]":
      gusano = 0
    else:
      aux = tablero[Fila][Columna]
      tablero[Fila][Columna] = 0
      tablero[Fila][Columna + 1] = tablero[Fila][Columna + 1] + aux
      Columna = Columna + 1

  if direccion == 2 and Fila < tamaño - 1: #ABAJO
    if tablero[Fila + 1][Columna] == "[X]":
      gusano = 0
    else:
      aux = tablero[Fila][Columna]
      tablero[Fila][Columna] = 0
      tablero[Fila + 1][Columna] = tablero[Fila + 1][Columna] + aux
      Fila = Fila + 1

  if direccion == 3 and Columna > 0: #IZQUIERDA
    if tablero[Fila][Columna - 1] == "[X]":
      gusano = 0
    else:
      aux = tablero[Fila][Columna]
      tablero[Fila][Columna] = 0
      tablero[Fila][Columna - 1] = tablero[Fila][Columna - 1] + aux
      Columna = Columna - 1
  input()
  return tablero, gusano, Fila, Columna

def mostrar_matriz(tamaño, matriz):
  for i in range(tamaño):
    for j in range(tamaño):
      print(str(matriz[i][j]).rjust(4), end=" ")
    print("\n")

dimensiones_matriz = int(input("Dimensiones: "))
tablero = matrix(dimensiones_matriz, dimensiones_matriz)

print("\nDatos agujeros: ")
cantidad_agujeros = int(input("Ingrese cantidad de agujeros: "))
pos_FILA_agujero = vector(cantidad_agujeros)
pos_COLUMNA_agujero = vector(cantidad_agujeros)
for i in range(cantidad_agujeros):
  pos_FILA_agujero[i] = int(input("Ingrese la fila del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  pos_COLUMNA_agujero[i] = int(input("Ingrese la columna del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  while (pos_FILA_agujero[i] == 0 and pos_COLUMNA_agujero[i] == 0) or (pos_FILA_agujero[i] == dimensiones_matriz - 1 and pos_COLUMNA_agujero[i] == dimensiones_matriz - 1):
    print("El agujero no puede estar en el mismo lugar que el gusano")
    pos_FILA_agujero[i] = int(input("Ingrese la fila del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
    pos_COLUMNA_agujero[i] = int(input("Ingrese la columna del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  
  while pos_FILA_agujero[i] < 0 or pos_COLUMNA_agujero[i] < 0 or pos_FILA_agujero[i] > dimensiones_matriz - 1 or pos_COLUMNA_agujero[i] > dimensiones_matriz - 1:
    print("Error, el agujero está fuera de la matriz... Vuelva a ingresar")
    pos_FILA_agujero[i] = int(input("Ingrese la fila del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
    pos_COLUMNA_agujero[i] = int(input("Ingrese la columna del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  
  tablero[pos_FILA_agujero[i]][pos_COLUMNA_agujero[i]] = "[X]"
  print()

print("\nDatos comida: ")
cantidad_comida = int(input("Ingrese cantidad de comida: "))
pos_FILA_comida = vector(cantidad_comida) 
pos_COLUMNA_comida = vector(cantidad_comida)
valor_comida = vector(cantidad_comida)

for i in range(cantidad_comida):
  pos_FILA_comida[i] = int(input("Ingrese la fila del comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): ")) 
  pos_COLUMNA_comida[i] = int(input("Ingrese la columna del comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  while (pos_FILA_comida[i] == 0 and pos_COLUMNA_comida[i] == 0) or (pos_FILA_comida[i] == dimensiones_matriz - 1 and pos_COLUMNA_comida[i] == dimensiones_matriz - 1):
    print("La comida no puede estar en el mismo lugar que el gusano")
    pos_FILA_comida[i] = int(input("Ingrese la fila del comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): ")) 
    pos_COLUMNA_comida[i] = int(input("Ingrese la columna del comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))

  while pos_FILA_comida[i] < 0 or pos_COLUMNA_comida[i] < 0 or pos_FILA_comida[i] > dimensiones_matriz - 1 or pos_COLUMNA_comida[i] > dimensiones_matriz - 1:
    print("Error, la comida está fuera de la matriz... Vuelva a ingresar")
    pos_FILA_comida[i] = int(input("Ingrese la fila de la comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
    pos_COLUMNA_comida[i] = int(input("Ingrese la columna de la comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))

  valor_comida[i] = int(input("Ingrese el valor de la comida (Máximo 5): "))
  while valor_comida[i] > 5 or valor_comida[i] < 1:
    valor_comida[i] = int(input("Vuelva a ingresar el valor de la comida (Máximo 5): "))
  print()
  tablero[pos_FILA_comida[i]][pos_COLUMNA_comida[i]] = valor_comida[i]

gusano_1 = 1; G1_F = 0; G1_C = 0
gusano_2 = 1; G2_F = dimensiones_matriz - 1; G2_C = dimensiones_matriz - 1
tablero[G1_F][G1_C] = gusano_1; tablero[G2_F][G2_C] = gusano_2

for i in range(dimensiones_matriz):
  for j in range(dimensiones_matriz):
    print(str(tablero[i][j]).rjust(4), end=" ")
  print("\n")
for i in range(cantidad_agujeros):
  print("Posición agujero "+str(i + 1)+": ", pos_FILA_agujero[i], ", ", pos_COLUMNA_agujero[i])
for i in range(cantidad_comida):
  print("Posición comida "+str(i + 1)+": ", pos_FILA_comida[i], ", ", pos_COLUMNA_comida[i])
input()

gusanos_muertos = False
sw = 1
cont = 0
while not gusanos_muertos:
  if gusano_1 > 0 and sw == 1:
    movimiento_gusanos(gusano_1, tablero, G1_F, G1_C, dimensiones_matriz)
    print("gordura",gusano_1, G1_F, G1_C)
  if gusano_2 > 0 and sw == 2:
    movimiento_gusanos(gusano_2, tablero, G2_F, G2_C, dimensiones_matriz)
    print("gordura",gusano_2, G2_F, G2_C)
  if sw == 1:
    sw = 2
  else:
    sw = 1
  if gusano_1 + gusano_2 == 0:
    gusanos_muertos == True
  cont += 1
  mostrar_matriz(dimensiones_matriz, tablero)
  print("\nTiempo transcurrido: ", cont)
print("Tiempo total transcurrido: ", cont)
print("Gordura con que murieron los gusanos: \nGusano 1: ", gusano_1, " \nGusano 2: ", gusano_2)




