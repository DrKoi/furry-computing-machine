cadena = 'X-DSPAM-Confidence:0.8475'
desde = cadena.find(':')
numero = float(cadena[desde+1:])
print(numero)