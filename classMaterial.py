#Materiales
import json
from classPersona import Persona
from classPrestamo import Prestamo

listaPersonas = Persona
listaPrestamos = []
listaMateriales = []
idList = 10
cant = 0

class Material():
    def __init__(self, id, articulo, cantidad):
        self.id = id
        self.articulo = articulo
        self.cantidad = cantidad

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def getDicccionario():
        dic = []
        for i in listaMateriales:
            dic.append({"id":i.get('id'), "articulo":i.get('articulo'), "cantidad":i.get('cantidad')})
        return dic

    def updateLista(lista):
        listaMateriales.extend(lista)
        return listaMateriales

    def obtener():
        for material in listaMateriales:
          id = material.get('id')
          articulo = material.get('articulo')
          cant = material.get('cantidad')
          print(str(id) + '  ' + articulo + '  ' + str(cant))
    
    def Registrar(articulo, cantidad):  
        idList = len(Material.getDicccionario())
        idList += 1
        materiales = {}
        materiales['id'] = idList
        materiales['articulo'] = articulo
        materiales['cantidad'] = cantidad
        listaMateriales.append(materiales)

    def searchMaterial(nombre=None):
        if nombre!=None:
            i=0
            for material in listaMateriales:
                if material['articulo'] == nombre:
                    return '  ¡Artículo encontrado! -> ' + str(material.get('id')) + ' ' + material.get('articulo') + ' ' + str(material.get('cantidad'))
                    return True
                i += 1
            print ('  ¡El artículo no existe!')  
            return False
        return None

    def searchIdMaterial(id=None):
        if id!=None:
            i=0
            for material in listaMateriales:
                if material['id'] == id:
                    return '  ¡Artículo encontrado! -> ' + str(material.get('id')) + ' ' + material.get('articulo') + ' ' + str(material.get('cantidad'))
                    return True
                i += 1
            print ('  ¡El artículo no existe!')  
            return False
        return None

    def updateMaterial(id, nombre, cantidad):
        if id!=None:
            for material in listaMateriales:
                if material['id'] == id:
                    material['articulo'] = nombre
                    material['cantidad'] = cantidad
                    return print('\n¡Datos actualizados!\n')
            return print ('\n ¡El id no existe!\n')
        return None
        
    def removeMaterial(id=None):
        if id!=None:
            i=0
            for material in listaMateriales:
                if material['id'] == id:
                    listaMateriales.pop(i)
                    return print('\n ¡Artículo eliminado!\n')
                i+=1
            return print ('\n ¡El id no existe!\n')
        return None

    def SolicitarPrestamo(persona, material, cantidad, fecha): 
        for objMaterial in listaMateriales:
            if objMaterial['id'] == material:
                nombre = objMaterial['articulo']
                cant = objMaterial['cantidad']
                if cant >= cantidad:
                    cant = cant - cantidad
                    Material.updateMaterial(material, nombre, cant)
                    prestamos = {}
                    prestamos['persona'] = persona
                    prestamos['material'] = nombre
                    prestamos['cantidad'] = cantidad
                    prestamos['fecha'] = fecha
                    listaPrestamos.append(prestamos)
                    print("\n   ¡¡Prestamo exitoso!!\n")
                    return True
                print ("\n   ¡No está disponible la cantidad solicidad!\n")
                return False

    @staticmethod
    def getDicccionarioPrest():
        dic = []
        for i in listaPrestamos:
            dic.append({"persona":i.get('persona'), "material":i.get('material'), "cantidad":i.get('cantidad'), "fecha":i.get('fecha')})
        return dic

    def updateListaPrestamos(lista):
        listaPrestamos.extend(lista)
        return listaPrestamos
        
    def obtenerPrestamos():
        for prestamo in listaPrestamos:
          persona = prestamo.get('persona')
          material = prestamo.get('material')
          cant = prestamo.get('cantidad')
          fecha = prestamo.get('fecha')
          print(persona + ' ' + str(material) + ' ' + str(cant) + ' ' + str(fecha))


#listaMateriales = [ 
    #Material( 1, 'Balón futbol', 10),
    #Material( 2, 'Balón básquetbol', 6),
    #Material( 3, 'Balón voleibol', 10),
    #Material( 4, 'Pelota béisbol', 20),
    #Material( 5, 'Bat béisbol', 10),
    #Material( 6, 'Guante béisbol', 20),
    #Material( 7, 'Porterías', 10),
    #Material( 8, 'Red voleibol', 3),
    #Material( 9, 'Vallas', 10),
    #Material( 10,'Aros', 15)
    #]