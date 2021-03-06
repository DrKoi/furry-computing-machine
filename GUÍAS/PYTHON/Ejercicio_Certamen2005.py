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

def mostrar_matriz(tamaño, matriz):
  for i in range(tamaño):
    for j in range(tamaño):
      print(str(matriz[i][j]).rjust(4), end=" ")
    print("\n")

def mover_gusanos(MATRIZ, F1, F2, C1, C2, G1, G2, VIVO1, VIVO2, CONT):
  direccion = rn.randint(0,3)
  print(direccion, F1, C1)
  #ARRIBA
  if direccion == 0 and F1 > 0: 
    if MATRIZ[F1 - 1][C1] == -1:
      VIVO1 = True
      MATRIZ[F1][C1] = 0
    elif (F1 - 1 == F2 and C1 == C2 and G1 < G2):
      VIVO1 = True
      G2 = G2 + G1
      MATRIZ[F1][C1] = 0
    elif (F1 - 1 == F2 and C1 == C2 and G1 > G2):
      VIVO2 = True
      G1 = G2 + G1
      MATRIZ[F2][C2] = 0
    else:
      aux = MATRIZ[F1][C1]
      MATRIZ[F1][C1] = 0
      MATRIZ[F1 - 1][C1] = MATRIZ[F1 - 1][C1] + aux
      G1 = MATRIZ[F1 - 1][C1]
      F1 = F1 - 1
      CONT += 1
  #DERECHA
  if direccion == 1 and C1 < dimensiones_matriz - 1: 
    if MATRIZ[F1][C1 + 1] == -1:
      VIVO1 = True
      MATRIZ[F1][C1] = 0
    elif (F1 == F2 and C1 + 1 == C2 and G1 < G2):
      VIVO1 = True
      G2 = G2 + G1
      MATRIZ[F1][C1] = 0
    elif (F1 == F2 and C1 + 1 == C2 and G1 > G2):
      VIVO2 = True
      G1 = G2 + G1
      MATRIZ[F2][C2] = 0
    else:
      aux = MATRIZ[F1][C1]
      MATRIZ[F1][C1] = 0
      MATRIZ[F1][C1 + 1] = MATRIZ[F1][C1 + 1] + aux
      G1 = MATRIZ[F1][C1 + 1]
      C1 = C1 + 1
      CONT += 1
  #ABAJO
  if direccion == 2 and F1 < dimensiones_matriz - 1: 
    if MATRIZ[F1 + 1][C1] == -1:
      VIVO1 = True
      MATRIZ[F1][C1] = 0
    elif (F1 + 1 == F2 and C1 == C2 and G1 < G2):
      VIVO1 = True
      G2 = G2 + G1
      MATRIZ[F1][C1] = 0
    elif (F1 + 1 == F2 and C1 == C2 and G1 > G2):
      VIVO2 = True
      G1 = G2 + G1
      MATRIZ[F2][C2] = 0
    else:
      aux = MATRIZ[F1][C1]
      MATRIZ[F1][C1] = 0
      MATRIZ[F1 + 1][C1] = MATRIZ[F1 + 1][C1] + aux
      G1 = MATRIZ[F1 + 1][C1]
      F1 = F1 + 1
      CONT += 1
  #IZQUIERDA
  if direccion == 3 and C1 > 0: 
    if MATRIZ[F1][C1 - 1] == -1:
      VIVO1 = True
      MATRIZ[F1][C1] = 0
    elif (F1 == F2 and C1 - 1 == C2 and G1 < G2):
      VIVO1 = True
      G2 = G2 + G1
      MATRIZ[F1][C1] = 0
    elif (F1 == F2 and C1 - 1 == C2 and G1 > G2):
      VIVO2 = True
      G1 = G2 + G1
      MATRIZ[F2][C2] = 0
    else:
      aux = MATRIZ[F1][C1]
      MATRIZ[F1][C1] = 0
      MATRIZ[F1][C1 - 1] = MATRIZ[F1][C1 - 1] + aux
      G1 = MATRIZ[F1][C1 - 1]
      C1 = C1 - 1
      CONT += 1
  print("DATOS: \nGORD: ",G1," Posición: ", F1, C1)
  return MATRIZ, F1, F2, C1, C2, G1, G2, VIVO1, VIVO2, CONT


dimensiones_matriz = int(input("Dimensiones: "))
tablero = matrix(dimensiones_matriz, dimensiones_matriz)

# Datos agujeros
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
  
  for j in range(i):
    while (pos_FILA_agujero[i] == pos_FILA_agujero[j] and pos_COLUMNA_agujero[i] == pos_COLUMNA_agujero[j]):
      print("Ya hay un agujero ocupando esta posición. Vuelva a ingresar.")
      pos_FILA_agujero[i] = int(input("Ingrese la fila del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
      pos_COLUMNA_agujero[i] = int(input("Ingrese la columna del agujero " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  tablero[pos_FILA_agujero[i]][pos_COLUMNA_agujero[i]] = -1
  print()

# Datos Comida
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
  
  for j in range(i):
    while (pos_FILA_comida[i] == pos_FILA_comida[j] and pos_COLUMNA_comida[i] == pos_COLUMNA_comida[j]):
      print("Ya hay comida ocupando esta posición. Vuelva a ingresar.")
      pos_FILA_comida[i] = int(input("Ingrese la fila de la comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
      pos_COLUMNA_comida[i] = int(input("Ingrese la columna de la comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  
  for j in range(cantidad_agujeros):
    while (pos_FILA_comida[i] == pos_FILA_agujero[j] and pos_COLUMNA_comida[i] == pos_COLUMNA_agujero[j]):
      print("Ya hay un agujero ocupando esta posición. Vuelva a ingresar comida.")
      pos_FILA_comida[i] = int(input("Ingrese la fila de la comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
      pos_COLUMNA_comida[i] = int(input("Ingrese la columna de la comida " + str(i + 1) + " (0 a "+str(dimensiones_matriz - 1)+"): "))
  valor_comida[i] = int(input("Ingrese el valor de la comida (Máximo 5): "))
  while valor_comida[i] > 5 or valor_comida[i] < 1:
    valor_comida[i] = int(input("Vuelva a ingresar el valor de la comida (Máximo 5): "))
  tablero[pos_FILA_comida[i]][pos_COLUMNA_comida[i]] = valor_comida[i]
  print()

# Datos Gusanos
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

# Movimiento Gusanos
gusanos_muertos = False
g1_muerto = False; g2_muerto = False
sw = 1
cont = 0; cont_G1 = 0; cont_G2 = 0; aux = 0
while not(gusanos_muertos):
  #Movimiento Gusano 1
  if not(g1_muerto) and sw == 1:
    mover_gusanos(tablero, G1_F, G2_F, G1_C, G2_C, gusano_1, gusano_2, g1_muerto, g2_muerto, cont_G1)
  
  #Movimiento Gusano 2
  if not(g2_muerto) and sw == 2:
    mover_gusanos(tablero, G2_F, G1_F, G2_C, G1_C, gusano_2, gusano_1, g2_muerto, g1_muerto, cont_G2)
  
  if sw == 1 and not(g2_muerto):
    sw = 2
  else:
    if sw == 2 and not(g1_muerto):
      sw = 1
  if g1_muerto == True and g2_muerto == True:
    gusanos_muertos = True
  cont += 1
  mostrar_matriz(dimensiones_matriz, tablero)
  print("\nTiempo transcurrido: ", cont, "Sw: ", sw, "g1: ", g1_muerto, "g2: ", g2_muerto)
  
  #input("PRESIONE ENTER")
print("Tiempo total transcurrido: ", cont)
print("Gordura con que murieron los gusanos: \nGusano 1: ", gusano_1, " \nGusano 2: ", gusano_2)