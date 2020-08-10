import random as rn

def ValorPieza(TAB, Fil, Col):
    Valor = 0
    if Fil >= 0 and Fil <= 7 and Col >= 0 and Col <= 7:
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
tablero[fila][columna] = "CB"

for i in range(8):
    for j in range(8):
      print(str(tablero[i][j]).rjust(4), end=" ")
    print("\n")

# Piezas
Mayor = 0
Pieza = ValorPieza(tablero, fila-2, columna-1)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila-2, columna+1)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila-1, columna+2)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila+1, columna+2)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila+2, columna+1)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila+2, columna-1)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila+1, columna-2)
if Mayor < Pieza:
  Mayor = Pieza
Pieza = ValorPieza(tablero, fila-1, columna-2)
if Mayor < Pieza:
  Mayor = Pieza

if Mayor == 0:
  print("No hay piezas para comer")
else:
  print("Caballo blanco puede comer", Nombre[Mayor-1])