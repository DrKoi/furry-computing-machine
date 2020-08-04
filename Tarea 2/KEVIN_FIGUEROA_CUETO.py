# Kevin Figueroa Cueto, único integrante del grupo "Kevin_Figueroa_Cueto", Saludos

import random as rn

def DIM_MATRIZ(Filas, Columnas, Valor=0):
  ARREGLO = []
  for Fila in range(Filas):
    ARREGLO.append([])
    for Columna in range(Columnas):
      ARREGLO[Fila].append(Valor)
  return ARREGLO

def SOBREESCRIBIR_SOPA(sopa, direccion, palabra, columna, fila):
  try:
    for i in range(len(palabra)):
      if (direccion == 1):  # Norte
        sopa[fila - i][columna] = palabra[i]
      if (direccion == 2):  # Noreste
        sopa[fila - i][columna + i] = palabra[i]
      if (direccion == 3):  # Este
        sopa[fila][columna + i] = palabra[i]
      if (direccion == 4):  # Sureste
        sopa[fila + i][columna + i] = palabra[i]
      if (direccion == 5):  # Sur
        sopa[fila + i][columna] = palabra[i]
      if (direccion == 6):  # Suroeste
        sopa[fila + i][columna - i] = palabra[i]
      if (direccion == 7):  # Oeste
        sopa[fila][columna - i] = palabra[i]
      if (direccion == 8):  # Noroeste
        sopa[fila - i][columna - i] = palabra[i]
  except Exception as identifier: # La palabra en conjunto con la direccion estan fuera de rango
    print("No se pudo ingresar la palabra en la sopa, error:", identifier)

sopa = DIM_MATRIZ(20, 20)

# Llenar matriz
for i in range(20):
  for j in range(20):
    sopa[i][j] = chr(rn.randint(65, 90))

palabras_escondidas = []
filas = []
columnas = []
direccion = []
for i in range(5):
  palabras_escondidas.append(input("Palabra a esconder " + str(i + 1) + ":"))
  palabras_escondidas[i] = palabras_escondidas[i].upper()
  filas.append(rn.randint(0, 19))
  columnas.append(rn.randint(0, 19))
  direccion.append(rn.randint(1, 8))
  SOBREESCRIBIR_SOPA(sopa, direccion[i], palabras_escondidas[i], columnas[i], filas[i])
print("")
palabras_encontradas = 0
desea_continuar = True
while (palabras_encontradas <= len(palabras_escondidas) and desea_continuar):
  palabra_a_buscar = input("Ingerese una palabra para buscar:")
  palabra_a_buscar = palabra_a_buscar.upper()
  for palabra_indice in range(len(palabras_escondidas)):
    encontro_palabra = False
    if (palabras_escondidas[palabra_indice] == palabra_a_buscar):
      encontro_palabra = True
      palabras_encontradas += 1
      print("La palabra existe en la sopa de letras")
      print("La ubicacion de la primera letras es... fila:", filas[palabra_indice], "columna:", columnas[palabra_indice])
      print("Dirección", end=" ")
      if (direccion[palabra_indice] == 1):  # Norte
        print("Norte")
      if (direccion[palabra_indice] == 2):  # Noreste
        print("Noreste")
      if (direccion[palabra_indice] == 3):  # Este
        print("Este")
      if (direccion[palabra_indice] == 4):  # Sureste
        print("Sureste")
      if (direccion[palabra_indice] == 5):  # Sur
        print("Sur")
      if (direccion[palabra_indice] == 6):  # Suroeste
        print("Suroeste")
      if (direccion[palabra_indice] == 7):  # Oeste
        print("Oeste")
      if (direccion[palabra_indice] == 8):  # Noroeste
        print("Noroeste")
      break
  if (not encontro_palabra):
    print("La palabra no existe")
  respuesta = input("\n¿Quieres seguir buscando palabras? (Si/No)\n")
  respuesta = respuesta.upper()
  if (respuesta == "SI"):
    desea_continuar = True
  else:
    desea_continuar = False
  print("")
for i in range(20):
  print(sopa[i])