def ContarPalabras(mensaje):
  cont = 0
  palabras = mensaje.split()
  while cont < len(palabras):
    cont += 1
  return cont

def CalcularValor(cantidad_palabras, tipo_mensaje):
  costo = 0
  if (cantidad_palabras == 0):
    costo = 45
  elif (cantidad_palabras == 1):
    costo = 70
  else:
    costo = 200 + ((cantidad_palabras - 2) * 5)
  if (tipo_mensaje == "U"):
    costo = costo + costo * 0.8
  return costo

def LeerUsuarios():
  usuarios = []
  for i in range(6): 
    nombre_ingresado = input("Usuario " + str(i+ 1) + ":")
    usuarios.append(nombre_ingresado)
  return usuarios

def MostrarMensaje(msj):
  print("-------- Mensaje Formateado --------")
  print(msj)
  print("-------- Fin Mensaje Formateado --------\n")

def stringToLista(mensaje):
  lista = []
  for i in range(len(mensaje)): 
    lista.append(mensaje[i])
  return lista

print("-----------------")
print("Calculadora de Tarifas")
print("-----------------\n")
print("Ingrese el nombre de los 6 usuarios pertenecientes al sistema.")

nombres_usuarios = LeerUsuarios()

mensaje_a_enviar = input("Ingrese mensaje a enviar: ")

mensaje_sin_espacios = mensaje_a_enviar.strip()

primer_digito = 0; segundo_digito = 0

try:
  primer_digito = int(mensaje_sin_espacios[0])
  segundo_digito = int(mensaje_sin_espacios[1])
except:
  raise Exception("Los primeros 2 caracteres deben ser numeros")

if not (1 <= primer_digito <= 6 and 1 <= segundo_digito <= 6):
  raise Exception("Los primeros 2 digitos deben estar entre 1 y 6")

tipo_mensaje = mensaje_sin_espacios[2]

if (tipo_mensaje != "N" and tipo_mensaje != "U"):
  raise Exception("El tercer caracter debe ser N o U")

mensaje_sin_tres_char = mensaje_sin_espacios[3:] # delete primeros 3 caracteres
ultimos_tres_digits = mensaje_sin_tres_char[-3:]

if (ultimos_tres_digits != "END"):
  raise Exception("El mensaje no termina con END")

mensaje_sin_end = mensaje_sin_tres_char[:len(mensaje_sin_tres_char)-3] # delete ultimos 3 caracteres

mensaje_formated_arr = mensaje_sin_end.split(" ")

for i in range(len(mensaje_formated_arr)): 
  if (mensaje_formated_arr[i] == "PS"):
    mensaje_formated_arr[i] = "."
  if (mensaje_formated_arr[i] == "PA"):
    mensaje_formated_arr[i] = ".\n"
  if(mensaje_formated_arr[i] == "CO"):
    mensaje_formated_arr[i] = ","

msj_sin_etiquetas = " ".join(mensaje_formated_arr)

msj_sin_etiquetas_arr = stringToLista(msj_sin_etiquetas)

for i in range(len(msj_sin_etiquetas_arr)):
  if (msj_sin_etiquetas_arr[i] in ".,"):
    msj_sin_etiquetas_arr[i - 1] = ""

mensaje_final = "".join(msj_sin_etiquetas_arr)

cantidad = ContarPalabras(mensaje_final)
costo_total = CalcularValor(cantidad, tipo_mensaje)
MostrarMensaje(mensaje_final)

print(
  "Nombre emisor: " + nombres_usuarios[primer_digito - 1] + 
  "\nNombre receptor: " + nombres_usuarios[segundo_digito - 1] + 
  "\nValor mensaje: " + str(costo_total)
  )










