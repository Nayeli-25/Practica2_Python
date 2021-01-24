import sys
import os
import json
from classArchivoPersona import FilePersona
from classArchivoMaterial import FileMaterial
from classArchivoPrestamo import FilePrestamo
from classPersona import Persona
from classMaterial import Material
from classPrestamo import Prestamo

listaPersonas = Persona
listaMateriales = Material
listaPrestamos = Prestamo

pers = FilePersona.read()
Persona.updateLista(pers)

materiales = FileMaterial.read()
Material.updateLista(materiales)

prestamos = FilePrestamo.read()
Material.updateListaPrestamos(prestamos)

def menu():
    while True:
      print("\n|******************************|")
      print("|      CENTRO DEPORTIVO        |")
      print("|******************************|")
      print("| Clientes.....................|")
      print("| 1. Ver clientes              |")
      print("| 2. Registrar cliente         |")
      print("| 3. Buscar cliente por nombre |")
      print("| 4. Buscar cliente por ID     |")
      print("| 5. Actualizar cliente        |")
      print("| 6. Eliminar cliente          |")
      print("| Materiales...................|")
      print("| 7. Ver materiales            |")
      print("| 8. Registrar material        |")
      print("| 9. Buscar material por nombre|")
      print("| 10. Buscar material por ID   |")
      print("| 11. Actualizar material      |")
      print("| 12. Eliminar material        |")
      print("| Préstamos....................|")
      print("| 13. Lista de préstamos       |")
      print("| 14. Registrar préstamo       |")
      print("| 15. Devolver artículo        |")
      print("| 0. Salir.....................|")
      print(" ******************************\n")

      opcion = int(input("¿Qué acción desea realizar? "))
      if opcion == 1:
        print("\n_____Clientes_____")
        Persona.obtener()

      elif opcion == 2:
        print("\n_____Registrar Cliente_____")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese appellido: ")
        listaPersonas.Registrar(nombre, apellido)
        FilePersona.save()
        print("\n   ¡¡Registro exitoso!!")

      elif opcion == 3:
        print("\n_____Buscar Cliente_____")
        nombre = input("Ingrese nombre: ")
        listaPersonas.searchPersona(nombre)

      elif opcion == 4:
        print("\n_____Buscar Cliente_____")
        idPersona = int(input("Ingrese id: "))
        listaPersonas.searchIdPersona(idPersona)

      elif opcion == 5:
        print("\n_____Actualizar Cliente_____")
        idPersona = int(input("ID del ciente: "))
        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo appellido: ")
        listaPersonas.updatePersona(idPersona, nombre, apellido)

      elif opcion == 6:
        print("\n_____Eliminar Cliente_____")
        idPersona = int(input("ID del ciente: "))
        listaPersonas.removePersona(idPersona)

      elif opcion == 7:
        print("\n_____Artículos_____")
        Material.obtener()

      elif opcion == 8:
        print("\n_____Registrar Artículo_____")
        articulo = input("Ingrese artículo: ")
        cantidad = int(input("Ingrese cantidad: "))
        listaMateriales.Registrar(articulo, cantidad)
        FileMaterial.save()
        print("\n   ¡¡Registro exitoso!!\n")

      elif opcion == 9:
        print("\n_____Buscar Artículo_____")
        nombre = input("Ingrese nombre: ")
        print(listaMateriales.searchMaterial(nombre))

      elif opcion == 10:
        print("\n_____Buscar Artículo_____")
        idMaterial = int(input("Ingrese id: "))
        print(listaMateriales.searchIdMaterial(idMaterial))

      elif opcion == 11:
        print("\n_____Actualizar Artículo_____")
        idMaterial = int(input("ID del artículo: "))
        nombre = input("Nuevo nombre: ")
        cantidad = int(input("Nueva cantidad: "))
        listaMateriales.updateMaterial(idMaterial, nombre, cantidad)
        FileMaterial.save()

      elif opcion == 12:
        print("\n_____Eliminar Artículo_____")
        idMaterial = int(input("ID del artículo: "))
        listaMateriales.removeMaterial(idMaterial)
        FileMaterial.save()

      elif opcion == 13:
        print("\n_____Préstamos_____")
        Material.obtenerPrestamos()

      elif opcion == 14:
        print("\n_____Nuevo Préstamo_____")
        print("\n_____Clientes_____")
        Persona.obtener()
        persona = input("\nNombre del ciente: ")
        if Persona.searchPersona(persona) == False:
          os.system("pause")
          return menu()
        print("\n_____Artículos_____")
        Material.obtener()
        idMaterial = int(input("\nID del artículo: "))
        if Material.searchIdMaterial(idMaterial) == False:
          os.system("pause")
          return menu()
        cantidad = int(input("Cantidad: "))
        fecha = input("Fecha: ")
        listaMateriales.SolicitarPrestamo(persona, idMaterial, cantidad, fecha)
        FilePrestamo.save()

      elif opcion == 0:
        sys.exit(0)
      else: 
          print('\n  ¡Opción inválida!')
      os.system("pause")


if __name__ == '__main__':
    menu()
