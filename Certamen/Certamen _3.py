import random as rn

def DIM_MATRIZ(Filas, Columnas, Valor=0):
  ARREGLO = []
  for Fila in range(Filas):
    ARREGLO.append([])
    for Columna in range(Columnas):
      ARREGLO[Fila].append(Valor)
  return ARREGLO

def MOSTRAR_MATRIZ(Arreglo):
  print("  ", end="")
  for Columna in range(len(Arreglo[0])):
    print(Columna, sep="", end=" ")
  print()
  for Fila in range(len(Arreglo)):
    print(Fila,end=" ")
    for Columna in range(len(Arreglo[Fila])):
      if Arreglo[Fila][Columna] == -3:
        print("X",end=" ")
      elif Arreglo[Fila][Columna] < 0:
        print("*",end=" ")
      elif Arreglo[Fila][Columna] == 0:
        print("-",end=" ")
      else:
        print(Arreglo[Fila][Columna], sep="", end=" ")
    print()

# PREPARATIVOS 1
espacio = DIM_MATRIZ(10, 10)
MOSTRAR_MATRIZ(espacio)
input("PAUSA")

# UBICAR LAS NAVES
aceptar = False
while not(aceptar):
  espacio = DIM_MATRIZ(10, 10)
  F1 = rn.randint(0, 7)
  C1 = rn.randint(0, 6)
  #NAVE 1
  espacio[F1][C1] = 1
  espacio[F1][C1 + 1] = 1
  espacio[F1 + 1][C1 + 1] = 1
  espacio[F1 + 2][C1 + 1] = 1

  F2 = rn.randint(0, 7)
  C2 = rn.randint(0, 6)
  while (F2 == F1 and C2 == C1) or (F2 == F1 and C2 == C1 + 1) or (F2 == F1 + 1 and C2 == C1 + 1) or (F2 == F1 + 2 and C2 == C1 + 1) or (F2 == F1 + 1 and C2 == C1) or (F2 == F1 + 2 and C2 == C1) or (F2 == F1 and C2 == C1 - 1) or (F2 == F1 - 2 and C2 == C1 - 1) or (F2 == F1 - 1 and C2 == C1) or (F2 == F1 - 2 and C2 == C1) or (F2 == F1 - 1 and C2 == C1 + 1) or (F2 == F1 - 2 and C2 == C1 + 1):
    F2 = rn.randint(0, 7)
    C2 = rn.randint(0, 6)
  #NAVE 2
  espacio[F2][C2] = 2
  espacio[F2 + 1][C2] = 2
  espacio[F2 + 2][C2] = 2
  espacio[F2 + 2][C2 + 1] = 2
  espacio[F2][C2 + 1] = 2

  MOSTRAR_MATRIZ(espacio)
  a = input("¿Acepta la Matriz? (S/N)\n")
  if a == "N":
    aceptar = False
  else:
    aceptar = True

# DESARROLLO DEL JUEGO
misiles = 20; acertados = 0; fallados = 0; repetidos = 0
naves_derribadas = False
partes_nave1 = 4; nave1_derribada = False
partes_nave2 = 5; nave2_derribada = False

while misiles > 0 and not(naves_derribadas):
  
  print("\nIngrese las cordenadas donde disparar el misil: ")
  misil_FILA = int(input("Fila: "))
  misil_COLUMNA = int(input("Columna: "))
  print()
  if misil_FILA < 0 or misil_FILA > 9 or misil_COLUMNA < 0 or misil_COLUMNA > 9:
    print("Coordenadas incorrectas")
  
  #impacta fuera
  elif espacio[misil_FILA][misil_COLUMNA] == -3 or espacio[misil_FILA][misil_COLUMNA] == -2 or espacio[misil_FILA][misil_COLUMNA] == -1:
    print("Ya disparó acá")
    print("MISIL DESPERDICIADO")
    misiles = misiles - 1
    repetidos += 1

  #impacta nave 1
  elif (misil_FILA == F1 and misil_COLUMNA == C1) or (misil_FILA == F1 and misil_COLUMNA == C1 + 1) or (misil_FILA == F1 + 1 and misil_COLUMNA == C1 + 1) or (misil_FILA == F1 + 2 and misil_COLUMNA == C1 + 1):
    espacio[misil_FILA][misil_COLUMNA] = -1
    partes_nave1 = partes_nave1 - 1
    if partes_nave1 == 0:
      print("DERRIBADA")
    else:
      print("IMPACTO")
    misiles = misiles - 1
    acertados += 1

  #impacta la nave 2
  elif (misil_FILA == F2 and misil_COLUMNA == C2) or (misil_FILA == F2 + 1 and misil_COLUMNA == C2) or (misil_FILA == F2 + 2 and misil_COLUMNA == C2) or (misil_FILA == F2 + 2 and misil_COLUMNA == C2 + 1) or (misil_FILA == F2 and misil_COLUMNA == C2 + 1): 
    espacio[misil_FILA][misil_COLUMNA] = -2
    partes_nave2 = partes_nave2 - 1
    if partes_nave2 == 0:
      print("DERRIBADA")
    else:
      print("IMPACTO")
    misiles = misiles - 1
    acertados += 1
  else:
    espacio[misil_FILA][misil_COLUMNA] = -3
    misiles = misiles - 1
    fallados += 1
    print("SIN IMPACTO")
  print()
  if partes_nave1 == 0:
    nave1_derribada = True
  if partes_nave2 == 0:
    nave2_derribada = True
  if nave1_derribada and nave2_derribada:
    naves_derribadas = True
  MOSTRAR_MATRIZ(espacio)
  print("Misiles restantes: ", misiles)

if naves_derribadas:
  print("\nHEMOS SALVADO A LA HUMANIDAD\n")
else:
  print("\nAL PARECER NOS MERECEMOS LA EXTINCIÓN\n")
print("Disparos: \n  Totales: ", acertados + fallados + repetidos, "\n  Repetidos: ", repetidos, "\n  Acertados: ", acertados, "\n  No Acertados: ", fallados)

if not(nave1_derribada) and not(nave2_derribada):
  print("\nNaves derribadas: 0")
elif naves_derribadas:
  print("\nNaves derribadas: 2")
elif nave1_derribada and not(nave2_derribada):
  print("\nNaves derribadas: 1")
elif nave2_derribada and not(nave1_derribada):
  print("\nNaves derribadas: 1")
input("\nFin del juego")