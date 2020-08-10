import random as rn

def ValorPiezaArriba(TAB, Fil, Col):
    Valor = 0
    Fil   = Fil - 1
    while Fil >= 0 and TAB[Fil][Col] == "**":
        Fil = Fil - 1

    if Fil >= 0:
        for Indice in range(6):
            if TAB[Fil][Col] == Codigos[Indice]:
                Valor = Indice + 1
    return Valor

def ValorPiezaDerecha(TAB, Fil, Col):
    Valor = 0
    Col   = Col + 1
    while Col <= 7 and TAB[Fil][Col] == "**":
        Col = Col + 1

    if Col <= 7:
        for Indice in range(6):
            if TAB[Fil][Col] == Codigos[Indice]:
                Valor = Indice + 1
    return Valor
    
def ValorPiezaAbajo(TAB, Fil, Col):
    Valor = 0
    Fil   = Fil + 1
    while Fil <= 7 and TAB[Fil][Col] == "**":
        Fil = Fil + 1

    if Fil <= 7:
        for Indice in range(6):
            if TAB[Fil][Col] == Codigos[Indice]:
                Valor = Indice + 1
    return Valor

def ValorPiezaIzquierda(TAB, Fil, Col):
    Valor = 0
    Col   = Col - 1
    while Col >= 0 and TAB[Fil][Col] == "**":
        Col = Col - 1

    if Col >= 0:
        for Indice in range(6):
            if TAB[Fil][Col] == Codigos[Indice]:
                Valor = Indice + 1
    return Valor

Codigos = ["PN", "TN", "CN", "AN", "RN", "XN"]
Nombre = ["PEÓN NEGRO", "TORRE NEGRA", "CABALLO NEGRO", "ALFIL NEGRO", "REINA NEGRA", "REY NEGRO"]
cantidad = [8, 2, 2, 2, 1, 1]

tablero = []
for i in range(8):
  tablero.append([])
  for j in range(8):
    tablero[i].append("**")


for i in range(len(Codigos)):
  Total = rn.randrange(cantidad[i])
  for j in range(Total):
    A = rn.randrange(8)
    B = rn.randrange(8)
    tablero[A][B] = Codigos[i]

# Caballo blanco
fila = rn.randrange(8)
columna = rn.randrange(8)
tablero[fila][columna] = "TB|"

for i in range(8):
    for j in range(8):
      print(str(tablero[i][j]).rjust(4), end=" ")
    print("\n")

# Piezas
Mayor = 0
Pieza = ValorPiezaArriba(tablero, fila, columna)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPiezaDerecha(tablero, fila, columna)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPiezaAbajo(tablero, fila, columna)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPiezaIzquierda(tablero, fila, columna)
if Mayor < Pieza:
  Mayor = Pieza



if Mayor == 0:
  print("No hay piezas para comer")
else:
  print("Torre blanca puede comer", Nombre[Mayor-1])