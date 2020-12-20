

Archivo = open('PERSONAS.DAT', 'w')

for contador in range(2):
    Rut       = input('RUT: ')
    Nombre    = input('NOMBRE: ')
    Edad      = input('EDAD: ')
    Direccion = input('DIRECCIÓN: ')
    Sexo      = input('SEXO: ')
    Archivo.write(Rut + ';' + Nombre + ';' + Edad + ';' + Direccion + ';' + Sexo +'\n')
Archivo.close()


