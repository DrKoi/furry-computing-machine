import random
def DIMVECTOR(cantidad):
  arreglo = []
  for i in range(cantidad):
    arreglo.append(random.randint(0,9))
  return arreglo

opa = DIMVECTOR(5)
print(opa)