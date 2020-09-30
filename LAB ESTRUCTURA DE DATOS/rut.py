# -*- coding: utf-8 -*-

RUT = input("Ingrese su rut: ")
if len(RUT) < 2:
  print("Error. El rut debe tener al menos dos caracteres")
else:
  pos = RUT.split("-")
  if pos == (-1):
    #El RUT no tiene guión
  else:
    #El RUT tiene guión
    if len(RUT) < 3:
      print("Error. El RUT debe tener al menos 3 caracteres.")



