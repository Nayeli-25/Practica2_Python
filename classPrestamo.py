
#Prestamos

class Prestamo(object):
    def __init__(self, persona, material, cantidad, fecha):
        self.idPersona = persona
        self.material = material
        self.cantidad = cantidad
        self.fecha = fecha