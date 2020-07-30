cifrado = input("Ingrese codigo cifrado: ")
# M23DS6M89S12BKIWK8WUXA*4X678EY1Y3NJ67J90_Z34567Z90 
# ingresar este código


"""CIF = ["M","2","3","D","S","6","M","8","9","S","1","2","B","K","I","W","K","8",
"W","U","X","A","*","4","X","6","7","8","E","Y","1","Y","3","N","J","6",
"7","J","9","0","_","Z","3","4","5","6","7","Z","9","0"]"""

N = len(cifrado)
CIF = []
for i in range(N):
    CIF.append("")

I = 0
while I <= len(CIF)-1 and I <= len(cifrado)-1:
    CIF[I] = cifrado[I]
    I = I + 1

print("El mensaje cifrado es: ")
for i in range (0,N): 
    print(CIF[i]," ", end="")
print()

# Descifrar el mensaje
i = 0; Sw = False
while Sw == False:
    Letra = CIF[i]  # Letra a buscar
    i = i + 1
    contador = 1
    while CIF[i] != Letra:
        i = i + 1
        if i > N-1:
            i = 0
        contador = contador + 1
    i = i + contador
    if i > N-1:
        i = i - N
    print(CIF[i], end="")
    i = i + 1
    if CIF[i] == "*":
        Sw = True
input()