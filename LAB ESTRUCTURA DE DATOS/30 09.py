# -*- coding:utf-8 -*-
##############################################################
# DECLARACIONES
class RegAlumno:
  IdAlumno = 0
  Nombre=""

class RegRamo:
  IdRamo=0
  Nombre=""

class RegNota:
  IdAlumno=0
  IdRamo=0
  Nota1=0
  Nota2=0
  Nota3=0

####################################################################
# MÓDULOS.
######################################################################
# PROGRAMA PRINCIPAL.
VecAlumnos=[]
for contador in range(5):
  VecAlumnos.append(RegAlumno())