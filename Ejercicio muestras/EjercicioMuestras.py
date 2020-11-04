class NODO():
    T = None
    A = None
    C = None
    G = None

def LeerDatos(Base, Archivo):
    AnteriorNodo = Base
    ArchivoMuestra = open(Archivo, "r")
    Registro = ArchivoMuestra.readline()
    while Registro != "":
        NuevoNodo = NODO()
        Nucleotido = Registro.strip()
        if Nucleotido == "T":
            AnteriorNodo.T = NuevoNodo
        elif Nucleotido == "A":
            AnteriorNodo.A = NuevoNodo
        elif Nucleotido == "C":
            AnteriorNodo.C = NuevoNodo
        elif Nucleotido == "G":
            AnteriorNodo.G = NuevoNodo
        print(Registro.strip())
        Registro = ArchivoMuestra.readline()
    ArchivoMuestra.close()

def MostrarSecuencia(Base):
    puntero = Base
    while puntero.T != None or puntero.A != None or puntero.C != None or puntero.G != None: 
        if puntero.T != None:
            print("T")
            puntero = puntero.T
        elif puntero.A != None:
            print("A")
            puntero = puntero.A
        elif puntero.C != None:
            print("C")
            puntero = puntero.C
        elif puntero.G != None:
            print("G")
            puntero = puntero.G

def Avanzar(Punt):
	if Punt.T != None:
		return Punt.T
	if Punt.A != None:
		return Punt.A 
	if Punt.C != None:
		return Punt.C
	if Punt.G != None:
		return Punt.G

def CompararMuestras(Base1, Base2):
  pass

Base1 = NODO()
Base2 = NODO()

LeerDatos(Base1, "MUESTRA 1.txt")
print()
LeerDatos(Base2, "MUESTRA 2.txt")

