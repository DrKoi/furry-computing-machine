def DefinirArreglo():
    global nombre, edad, peso
    nombre = [""]; edad = [0]; peso = [0]
    for i in range(1, 21):
        nombre.append("")
        edad.append(0)
        peso.append("")
        

def IngresoDatos():
    global cant
    print("Ingrese datos de tripulantes: ")
    cant = int(input("Cantidad de personas: "))
    i = 0
    while i < cant:
        print("Ingrese nombre de persona", i + 1, ": ")
        nombre[i] = input() 
        edad[i] = int(input("Ingrese edad: "))
        peso[i] = float(input("Ingrese peso: ", "kg"))
        i = i + 1 

def PromedioPesoTotal():
    global suma_peso
    suma_peso = 0; i = 0
    while i < cant:
        suma_peso = suma_peso + peso[i]
        i = i + 1

def SumaPesos100():
    global pesos100
    pesos100 = 0 ; i = 0
    while i < cant:
        if peso[i] > 100:
            pesos100 = pesos100 + peso[i]
        i = i + 1

DefinirArreglo()
IngresoDatos()
PromedioPesoTotal()
SumaPesos100()
print("Total de personas:", cant)
print("Promedio de todos los pesos:", suma_peso/cant)
i = 0
print("Personas con pesos mayor al promedio: ") 
while i < cant:
    if peso[i] > suma_peso/cant:
        print(nombre[i], "   Edad:", edad[i], "   Peso:", peso[i], "kg.")
    i = i + 1

print("Suma del peso de todas las personas que pesan más de 100 kg: ", pesos100, "kg.")

input()
