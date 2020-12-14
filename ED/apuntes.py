#Modulos apuntes para reutilización uwu
##################################################################################################
#Recorridos
def PreOrden(Puntero):
    if Puntero != None:
        print(Puntero.Valor)        
        PreOrden(Puntero.Izq)
        PreOrden(Puntero.Der)
    
def InOrden(Puntero):
    if Puntero != None:        
        InOrden(Puntero.Izq)
        print(Puntero.Valor)
        InOrden(Puntero.Der)
        
def PostOrden(Puntero):
    if Puntero != None:        
        PostOrden(Puntero.Izq)
        PostOrden(Puntero.Der)
        print(Puntero.Valor)
####################################################################################################
class NODO:
    Edad   = 0
    Enlace = None
# Agregar un nodo al principio de la lista.
def AgregarNodo1(Base): 
    Nodo = NODO()    
    Nodo.Edad = int(input("Ingrese una edad: "))
    Nodo.Enlace = Base
    Base = Nodo
    return Base

# Agregar un nodo al final de la lista.
def AgregarNodo2(Base): 
    Nodo = NODO()    
    Nodo.Edad = int(input("Ingrese una edad: "))
    if Base == None:
        Base = Nodo
    else:
        Puntero = Base
        while Puntero.Enlace != None:
            Puntero = Puntero.Enlace
        Puntero.Enlace = Nodo    
    return Base
    
# Agregar un nodo al "medio" de la lista.
def AgregarNodo3(Base): 
    Nodo = NODO()    
    Nodo.Edad = int(input("Ingrese una edad: "))
    if Base == None or (Nodo.Edad <= Base.Edad):
        Nodo.Enlace = Base
        Base = Nodo
    else:
        Anterior = None
        Puntero  = Base
        while Puntero != None and Puntero.Edad < Nodo.Edad:
            Anterior = Puntero
            Puntero  = Puntero.Enlace

        Nodo.Enlace     = Puntero
        Anterior.Enlace = Nodo   
    return Base

def Mostrar(Base): #mostrar lista
    if Base == None:
        print("Lista vacía")
    else:
        Puntero = Base
        while Puntero != None:
            print(Puntero.Edad)
            Puntero = Puntero.Enlace
            
def EliminarNodo(Base):
    Edad = int(input("Ingrese la edad del nodo que quiere eliminar: "))  
    if Base == None:
        print("Lista vacía")
    elif Base.Edad == Edad:
        Base = Base.Enlace
    else:
        Anterior = None
        Puntero = Base
        while Puntero != None:
            if Puntero.Edad == Edad:
                Anterior.Enlace = Puntero.Enlace
            Anterior = Puntero
            Puntero = Puntero.Enlace
    return Base



#################################################################################################
"""
Programa que construye árbol de búsqueda. Permite agregar, consultar y listar.
Incluye recorridos exhaustivos utilizando recursividad. 
Incluye quiebre de la exhaustividad. 
@author: Dagoberto Cabrera
"""

class PERSONA():
    rol = 0
    nombre = "" 
    edad = 0
    sexo = "*"
    izq = None
    der = None

def AgregarNodo(raiz):
    NuevoRol = int(input("Rol: "))
    p = raiz
    while (p != None) and (p.rol != NuevoRol): 
        pant = p
        if NuevoRol < p.rol: 
            p = p.izq
        else: 
            p = p.der 
    if p != None: 
        print("Error, ese Rol ya existe")
    else:                
        q = PERSONA()
        # Se muestra dirección en que es almacenado cada nodo. 
        print("Se agregará nodo en dirección: ", id(q))
        q.rol = NuevoRol
        q.nombre = input("Nombre: ")
        q.edad = int(input("Edad: "))
        q.sexo = input("Sexo (M o F): ")
        q.izq = None
        q.der = None
        if raiz == None:
            raiz = q
        else:
            if NuevoRol < pant.rol:
                pant.izq = q
            else: 
                pant.der = q
    return raiz
# Fin AgregarNodo     

def ConsultarPorRol(raiz): 
    RolBuscado = int(input("Ingrese Rol a buscar: "))
    p = raiz
    while (p != None) and (p.rol != RolBuscado):
        if RolBuscado < p.rol:
            p = p.izq
        else: 
            p = p.der
    if p == None:
        print("Error. Ese Rol no existe")
    else: 
        print("Rol ", p.rol, " encontrado")
        print("Nombre: ", p.nombre)
        print("Edad  : ", p.edad)
        print("Sexo  : ", p.sexo)
# Fin ConsultarPorRol   
        
def Mostrar(p):     # Recorrido PRE-ORDEN  (se muestran direcciones de memoria)
    if p != None: 
        print("Se accesa nodo dirección: ", id(p))
        print(p.rol," ",(p.nombre).ljust(25)," ",p.edad,"   ",p.sexo)
        input()
        Mostrar(p.izq)
        Mostrar(p.der)
# Fin Mostar        
        
def Listado(raiz):
    print("LISTADO DE PERSONAS"); print()
    print(" ROL            NOMBRE            EDAD  SEXO")
    print(" ===            ======            ====  ====")
    Mostrar(raiz) 
    print("FIN DEL LISTADO")
# Fin Listado     

def Mostrar2(p):      # Recorrido  EN-ORDEN  (se muestran direcciones de memoria)
    if p != None:     
        Mostrar2(p.izq)
        print("Se accesa nodo dirección: ", id(p))
        print(p.rol," ",(p.nombre).ljust(25)," ",p.edad,"   ",p.sexo)
        input()
        Mostrar2(p.der)
# Fin Mostar        
        
def ListadoOrdenado(raiz):
    print("LISTADO DE PERSONAS ORDENADO POR ROL"); print()
    print(" ROL            NOMBRE            EDAD  SEXO")
    print(" ===            ======            ====  ====")
    Mostrar2(raiz) 
    print("FIN DEL LISTADO")
# Fin Listado             

def ConsultarPorNombre(p, NomBuscado, Sw):    
# Utiliza un switch para quiebre de exhaustividad de recorrido Pre-Orden. 
    if (p != None) and (Sw == 0): 
        if p.nombre == NomBuscado: 
            Sw = 1
            print("Se encontró ese nombre")
            print("Rol: ", p.rol, "Edad: ", p.edad)
        Sw = ConsultarPorNombre(p.izq, NomBuscado, Sw)
        Sw = ConsultarPorNombre(p.der, NomBuscado, Sw)
    return Sw
    
# PROGRAMA PRINCIPAL
raiz = None
Opcion = "0"
while Opcion != "9":
    print("OPCIONES: ")
    print("1: Agregar un nodo al árbol")
    print("2: Consultar por ROL")
    print("3: Listar árbol")
    print("4: Listar ordenado por ROL")
    print("5: Buscar por nombre: ")
    print("9: Terminar proceso")
    print()
    Opcion = input("Ingrese opción: ")
    if Opcion == "1": raiz = AgregarNodo(raiz)  
    if Opcion == "2": ConsultarPorRol(raiz)
    if Opcion == "3": Listado(raiz)
    if Opcion == "4": ListadoOrdenado(raiz)
    if Opcion == "5": 
        Sw = 0
        NomBuscado = input("Nombre a buscar: ")
        Sw = ConsultarPorNombre(raiz, NomBuscado, Sw)
        if Sw == 0: 
            print("No se encontró ese nombre")
    print() 

input("Fin del proceso")



################Lo corté del programa####
def agregarMatrimonioToArbol(raizEsposos):
    nodoEsposo=ESPOSOS()
    nodoEsposo.RutEsp=input('Ingrese RUT: ')
    nodoEsposo.NombreEsp=input('Ingrese nombre de esposo: ')
    nodoEsposo.SexoEsp='M'
    if raizEsposos==None:
        raizEsposos=nodoEsposo
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
            pant.izq = nodoEsposo
        else:
            pant.der = nodoEsposo

    nodoEsposA=ESPOSOS()
    nodoEsposA.RutEsp=input('Ingrese RUT: ')
    nodoEsposA.NombreEsp=input('Ingrese nombre de esposa: ')
    nodoEsposA.SexoEsp='F'
    if raizEsposos==None:
        raizEsposos=nodoEsposA
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
            pant.izq = nodoEsposA
        else:
            pant.der = nodoEsposA
    return raizEsposos