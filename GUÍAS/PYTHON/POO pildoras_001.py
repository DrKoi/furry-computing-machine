class Coche():
    largo_Chasis = 250
    ancho_Chasis = 120
    ruedas = 4
    en_marcha = False

    def arrancar(self):
        self.en_marcha=True
    
    def estado(self):
        if self.en_marcha:
            return 'El coche está en marcha'
        else:
            return 'El coche está detenido'

miCoche = Coche() #Instanciar una clase
print(miCoche.largo_Chasis)
print(miCoche.estado()) 