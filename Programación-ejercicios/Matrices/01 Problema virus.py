""" 
1) En una superficie que representaremos con una matriz numérica de 10x10,  
supondremos que existen 100 bacterias (cada una en un elemento de la matriz).
Cada 1 día (y durante 10 días) cae un virus en algún lugar de la superficie 
(generar coordenadas al azar). Cuando el virus cae mata a la bacteria que estaba en ese lugar,
además de todas las que están en lugar contiguo a esa celda (entonces puede matar hasta 9 bacterias,
aunque podrian ser menos si ya habían sido aniquiladas algunas).
Si el virus cae en una celda en que no hay bacteria (ya fue muerta), no produce ningún efecto ese virus. 
Esto se puede manejar poniendo un 1 donde hay una bacteria y un 0 donde murió una bacteria.
Realizar un programa que simule lo descrito,
mostrando cómo queda al final la matriz e indicando cuántas bacterias fueron muertas. 
"""
import random as rn

m_bacterias = []
for i in range(10):
  m_bacterias.append([])
  for j in range(10):
    m_bacterias[i].append(1)

for i in range(10):
  for j in range(10):
    print(str(m_bacterias[i][j]).rjust(4), end=" ")
  print("\n")
print("\n")

virus_caen = 0
virus_inactivos = 0
bacterias_muertas = 0
while virus_caen < 10:
  F   = rn.randrange(10)
  C   = rn.randrange(10)
  if m_bacterias[F][C]  == 1:
    m_bacterias[F][C]  = 0
    bacterias_muertas += 1
    if F > 0 and m_bacterias[F - 1][C] == 1:
      m_bacterias[F - 1][C] = 0
      bacterias_muertas += 1
    if F > 0 and C < 9 and m_bacterias[F - 1][C + 1] == 1:
      m_bacterias[F - 1][C + 1] = 0
      bacterias_muertas += 1
    if C < 9 and m_bacterias[F][C + 1] == 1:
      m_bacterias[F][C + 1] = 0
      bacterias_muertas += 1
    if F < 9 and C < 9 and m_bacterias[F + 1][C + 1] == 1:
      m_bacterias[F + 1][C + 1] = 0
      bacterias_muertas += 1
    if F < 9 and m_bacterias[F + 1][C] == 1:
      m_bacterias[F + 1][C] = 0
      bacterias_muertas += 1
    if F < 9 and C > 0 and m_bacterias[F + 1][C - 1] == 1:
      m_bacterias[F + 1][C - 1] = 0
      bacterias_muertas += 1
    if C > 0 and m_bacterias[F][C - 1] == 1:
      m_bacterias[F][C - 1] = 0
      bacterias_muertas += 1
    if F > 0 and C > 0 and m_bacterias[F - 1][C - 1] == 1:
      m_bacterias[F - 1][C - 1] = 0
      bacterias_muertas += 1
  else:
    virus_inactivos +=1
  virus_caen += 1
  for i in range(10):
    for j in range(10):
      print(str(m_bacterias[i][j]).rjust(4), end=" ")
    print("\n")
  print("\n")

print("Virus inactivos: ", virus_inactivos, "\nTotal bacterias muertas: ", bacterias_muertas, "\nBacterias vivas: ", 100-bacterias_muertas)