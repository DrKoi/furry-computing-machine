class SUSTANTIVO():
    palabra = ''
    veces = 0  
    siguiente = None 

class NODO():
    palabrita = '' 
    cantidad = 0  
    sinonimo = None # Apunta a un sinónimo (si tiene) o es None.  
    izq = None 
    der = None 

def LeerDatosYCrearLista(BasePal): 
    sw = True
    while sw:
        nuevoNodo = SUSTANTIVO()
        nuevoNodo.palabra = input('Ingrese palabra: ')
        if BasePal == None:
            BasePal = nuevoNodo
            BasePal.veces = 1
        else:
            p = BasePal
            sw2 = 0
            while p != None:
                if nuevoNodo.palabra == p.palabra:
                    p.veces += 1
                    sw2 = 1
                p = p.siguiente
            if sw2 == 0:
                p = BasePal
                while p.siguiente != None:
                    p = p.siguiente
                nuevoNodo.veces = 1
                p.siguiente = nuevoNodo
        resp = input('\n¿Ingresará más palabras? (S/N): \n')
        resp = resp.upper()
        while resp != 'N' and resp != 'S':
            print('Ingrese un valor correcto')
            resp = input('¿Ingresará más palabras? (S/N): ')
            resp = resp.upper()
        if resp == 'S':
            sw = True
        else:
            sw = False
    return BasePal

def CrearArbol(BasePal, RaizPal): 
    puntero = BasePal
    while puntero!=None:
        palabra=puntero.palabra; cantidad=puntero.veces
        nodo = RaizPal
        while nodo != None:
            nodo_anterior=nodo
            if palabra < nodo.palabrita:
                nodo=nodo.izq
            else:
                nodo=nodo.der
        nuevoNodo=NODO()
        nuevoNodo.palabrita=palabra
        nuevoNodo.cantidad=cantidad
        if RaizPal==None:
            RaizPal=nuevoNodo
        else:
            if palabra < nodo_anterior.palabrita:
                nodo_anterior.izq = nuevoNodo
            else:
                nodo_anterior.der = nuevoNodo
        puntero = puntero.siguiente
    return RaizPal

def ConectarSinonimos(RaizPal): 
    # Permite ingresar sinónimos para conectar palabras del árbol
    # IMPORTANTE: Como se busca por clave de ordenamiento, se deben hacer dos recorridos separados
    Resp = 'S'
    while Resp == 'S': 
        pal1 = input('Ingrese primera palabra de par de sinónimos: ')
        pal2 = input('Ingrese segunda palabra de par de sinónimos: ')
        p = RaizPal;  q1 = None    # Se busca la primera palabra
        while p != None and q1 == None:
            if p.palabrita == pal1: 
                q1 = p
            else: 
                if pal1 < p.palabrita: 
                    p = p.izq
                else: 
                    p = p.der
                    
        p = RaizPal; q2 = None    # Se busca la segunda palabra
        while p != None and q2 == None:
            if p.palabrita == pal2: 
                q2 = p
            else: 
                if pal2 < p.palabrita: 
                    p = p.izq
                else: 
                    p = p.der                    
        
        # Se supone que no hubo error, pero igual se valida. Se conectan los dos nodos del árbol
        if q1 != None and q2 != None: 
            q1.sinonimo = q2
            q2.sinonimo = q1
        Resp = input('¿Desea ingresar otro par de palabras sinónimas? (S/N): ')
        Resp = Resp.upper()

def Recorrer(puntero): #In-orden
    while puntero!=None:
        Recorrer(puntero.izq)
        if puntero.cantidad > 1:
            if puntero.sinonimo==None:
                print(str((puntero.cantidad)).rjust(5), '    ', (puntero.palabrita).ljust(10), '  *****')
            else:
                print(str((puntero.cantidad)).rjust(5), '    ', (puntero.palabrita).ljust(10), ' ', (puntero.sinonimo).palabrita)
        Recorrer(puntero.der)

def Listar(RaizPal): 
    Recorrer(RaizPal)

def MostrarLista(BASE):
    if BASE == None:
        print('ERROR, LA LISTA ESTÁ VACÍA')
    else:
        PUNTERO = BASE
        while PUNTERO != None:
            print(PUNTERO.palabra, '', PUNTERO.veces)
            PUNTERO = PUNTERO.siguiente

# PROGRAMA PRINCIPAL
BasePal = None; RaizPal = None 
BasePal = LeerDatosYCrearLista(BasePal)
MostrarLista(BasePal)
RaizPal = CrearArbol(BasePal, RaizPal)
Resp = input('Desea ingresar sinónimos? (S/N): ')
if Resp == 'S' or Resp == 's':
    ConectarSinonimos(RaizPal)
Listar(RaizPal)
input('Fin del proceso')