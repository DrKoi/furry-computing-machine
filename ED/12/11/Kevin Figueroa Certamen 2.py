# Kevin Figueroa Cueto 192-B
class ESPOSOS(): 
	RutEsp =  0
	NombreEsp = ''
	SexoEsp =  ''    	# Se usará “M” o “F”
	PrimHijo = None   	# Es None o apunta a un nodo del árbol de hijos. 
	Conyuge = None   	# Apunta al nodo de la esposa o del esposo. 
	IzqEsp = None
	DerEsp = None

class HIJOS(): 
	RutHijo = 0
	NombreHijo = ''
	SexoHijo = ''     	# Se usará “M” o “F”
	Primogenito = ''   	# Se usará “S” o “N”
	IzqHijo = None
	DerHijo = None

def leerdatosESPOSOS(raizEsposos): #Modulo para ingresar los datos de cada matrimonio, 
    Esp=ESPOSOS()                    # la idea era acortar el programa llamando este modulo en el de ingreso al árbol
    Esp.RutEsp=int(input('Ingrese RUT: '))
    if raizEsposos==None:
        raizEsposos=Esp
    else:
        puntero=raizEsposos
        while puntero!=None:
            rut=puntero.RutEsp
            pant=puntero
            if rut < puntero.RutEsp:
                puntero=puntero.IzqEsp
            else:
                puntero=puntero.DerEsp
        if rut < pant.RutEsp:
            pant.izq = Esp
        else:
            pant.der = Esp
    return raizEsposos

def agregarMatrimonioToArbol(raizEsposos): # Modulo para agregar nodos Esposo y Esposa al arbol
    # Datos Esposo
    nodoEsposo=leerdatosESPOSOS(raizEsposos)
    nodoEsposo.NombreEsp=input('Ingrese nombre de esposo: ')
    nodoEsposo.SexoEsp='M'
    # Datos Esposa
    nodoEsposA=leerdatosESPOSOS(raizEsposos)
    nodoEsposA.NombreEsp=input('Ingrese nombre de esposa: ')
    nodoEsposA.SexoEsp='F'
    # Conectar matrimonio por conyuge
    nodoEsposo.Conyuge=nodoEsposA
    nodoEsposA.Conyuge=nodoEsposo
    return raizEsposos

def leerDatosHijo(raizEsposos, raizHijos): # Para leer hijo, e ingresar datos generales
    hijo=HIJOS()
    hijo.RutHijo=int(input('Ingrese RUT de hijo o hija: '))
    hijo.Primogenito=input('¿Es primogénito (S/N): ')
    if raizHijos==None:
        raizHijos=hijo
    else:
        puntero=raizHijos
        while puntero!=None:
            rut=puntero.RutHijo
            pant=puntero
            if rut < puntero.RutHijo:
                puntero=puntero.IzqHijo
            else:
                puntero=puntero.DerHijo
        if rut < pant.RutHijo:
            pant.izq = hijo
        else:
            pant.der = hijo
    return raizHijos

def agregarHijoToArbol(raizEsposos, raizHijos): #se agrega el hijo o hija al arbol y se llenan los campos de hijo primogenito en losnodos de los padres correspondientes
    rutPadreMadre=int(input('Ingrese RUT del padre o la madre: '))
    if raizEsposos==None:
        print('Primero debe ingresar un matrimonio')
    else:
        nodoHijo=leerDatosHijo(raizEsposos, raizHijos)
        nodoHijo.SexoHijo=input('Ingrese Sexo del hijo o hija (M/F): ')
        if nodoHijo.Pimogenito=='S':
            puntero=raizEsposos
            while puntero!=None:
                rut=puntero.RutEsp
                if rutPadreMadre == rut:
                    if puntero.PrimHijo!=nodoHijo: #Validacion de si existe el hijo en los datos de primogenito de los padres
                        puntero.PrimHijo=nodoHijo
                        (puntero.Conyuge).PrimHijo=nodoHijo
                elif rutPadreMadre < rut:
                    puntero=puntero.IzqEsp
                elif rutPadreMadre > rut:
                    puntero=puntero.DerEsp
    return raizEsposos, raizHijos

def PreOrden_buscarMatrimonio(raizHijos, raizEsposos):
    """  if Puntero != None:
        print(Puntero.Valor)        
        PreOrden(Puntero.Izq)
        PreOrden(Puntero.Der) """
    pass


def Listado(raizHijos, raizEsposos): #Modulo para listar los hijos primogenitos in orden
    Puntero=raizHijos
    if Puntero != None:        
        Listado(Puntero.Izq)
        if Puntero.Primogenito is 'S':
            padreMadre=PreOrden_buscarMatrimonio(raizHijos, raizEsposos)
            padreMadre2=padreMadre.Conyuge
            print('RUT hijo: ', Puntero.RutHijo, 'Nombre hijo(a): ', Puntero.NombreHijo)
            if padreMadre.SexoEsp=='M':
                print('Padre: ', padreMadre.NombreEsp)
            else:
                print('Madre: ', padreMadre.NombreEsp)
            if padreMadre2.SexoEsp=='M':
                print('Padre: ', padreMadre2.NombreEsp)
            else:
                print('Madre: ', padreMadre2.NombreEsp)
        Listado(Puntero.Der)

def MostrarEstadisticas():
    pass

raizEsposos=None; raizHijos=None
opcion = "0"
while opcion != "9":
    print("Menú principal: ")
    print("1: Agregar un matrimonio al árbol")
    print("2: Agregar un hijo al árbol")
    print("3: Listar ordenado por RUT")
    print("4: Mostrar Estadísticas: ")
    print("9: Terminar proceso\n")
    opcion = input("Ingrese opción: ")
    if opcion == "1": raizEsposos = agregarMatrimonioToArbol(raizEsposos)  
    if opcion == "2": raizEsposos, raizHijos=agregarHijoToArbol(raizEsposos, raizHijos)
    if opcion == "3": Listado(raizHijos, raizEsposos)
    if opcion == "4": MostrarEstadisticas() 