cont = 0
total = 0
while True:
    string = input('Ingrese un número: ')
    if string == 'listo':
        break
    
    try: 
        valor_float = float(string)
    except:
        print('Valor inválido')
        continue
    cont += 1
    total += valor_float
if cont == 0:
    print('Error. No hay valores ingresados.')
else:
    print(total, cont, total/cont)

