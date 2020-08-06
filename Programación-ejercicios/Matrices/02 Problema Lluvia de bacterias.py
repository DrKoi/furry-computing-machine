""" 
2) En una superficie que representaremos con una matriz numérica de 12x12, 
supondremos que cae una "lluvia de bacterias". Al principio la superficie estará limpia.
Cada 1 segundo caerá una bacteria en la superficie (coordenadas al azar). 
Cada bacteria tendrá una gordura (valor entre 1 y 10 al azar).
Si en el lugar que cae la bacteria está ya una bacteria, la que cae "rebota" 
hacia otro lugar (nuevas coordenadas al azar). Una vez que cae, se come a las 
(hasta) 4 bacterias que podrían estar contiguas a la que cayó, siempre que esas 
bacterias tengan menor gordura. Si la bacteria come, aumenta su gordura según lo 
comido y las bacterias comidas desaparecen.
Solo considerar los lados verticales u horizaontales (no los diagonales). 
En cada celda se puede usar código 0 para espacio vacío y un entero (gordura) 
para caso que esté una bacteria.
Simular el proceso, hasta que se llene la matriz, mostrando cómo quedó al final. 
"""

import random as rn

M_Bacterias = []
for i in range(12):
  M_Bacterias.append([])
  for j in range(12):
    M_Bacterias[i].append(0)
    print(str(M_Bacterias[i][j]).rjust(4), end=" ")
  print(); print()

caen_bacterias = 0
MatrizLlena = False
while not (MatrizLlena):
  F = rn.randrange(12)
  C = rn.randrange(12)
  gordura = rn.randrange(10) + 1
  while M_Bacterias[F][C] > 0:
    F = rn.randrange(12)
    C = rn.randrange(12)
  M_Bacterias[F][C] = gordura
  #Revisa NORTE
  if F > 0 and M_Bacterias[F - 1][C] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F - 1][C]
    M_Bacterias[F - 1][C] = 0
  #Revisa NORESTE
  if F > 0 and C < 7 and M_Bacterias[F - 1][C+1] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F - 1][C + 1]
    M_Bacterias[F - 1][C + 1] = 0
  #Revisa ESTE
  if C < 7 and M_Bacterias[F][C + 1] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F][C + 1]
    M_Bacterias[F][C + 1] = 0
  #Revisa SURESTE
  if F < 7 and C < 7 and M_Bacterias[F + 1][C + 1] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F + 1][C + 1]
    M_Bacterias[F + 1][C + 1] = 0
  #Revisa SUR
  if F < 7 and M_Bacterias[F + 1][C] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F + 1][C]
    M_Bacterias[F + 1][C] = 0
  #Revisa SUROESTE
  if F < 7 and C > 0 and M_Bacterias[F + 1][C - 1] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F + 1][C - 1]
    M_Bacterias[F + 1][C - 1] = 0
  #Revisa OESTE
  if C > 0 and M_Bacterias[F][C - 1] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F][C - 1]
    M_Bacterias[F][C - 1] = 0
  #Revisa NOROESTE
  if F > 0 and C > 0 and M_Bacterias[F - 1][C - 1] < gordura:
    M_Bacterias[F][C] += M_Bacterias[F - 1][C - 1]
    M_Bacterias[F - 1][C - 1] = 0
  
  
  print("F-C-GORDURA = ", F, C, gordura)
  caen_bacterias += 1

  for i in range(12):
    for j in range(12):
      print(str(M_Bacterias[i][j]).rjust(4), end=" ")
    print(); print()
  
  cont = 0
  for i in range(12):
    for j in range(12):
      if M_Bacterias[i][j] > 0:
        cont += 1
  if cont == 144:
    MatrizLlena = True

print("Total de bacterias que caen: ", caen_bacterias)