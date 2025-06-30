from dto.PeliculaDTO import PeliculaDTO
from dao.PeliculaDAO import PeliculaDAO

def menu():
    dao = PeliculaDAO()

    while True:
        print("\n📽️ MENÚ PELÍCULAS")
        print("1. Ingresar película")
        print("2. Mostrar todas")
        print("3. Consultar por ID")
        print("4. Eliminar")
        print("5. Modificar")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pelicula = PeliculaDTO(0, "Matrix", 136, "1999-03-31", 2, 2, "Wachowski")
            dao.insertar(pelicula)
        elif opcion == "2":
            dao.consultar_todo()
        elif opcion == "3":
            dao.consultar_particular(1)
        elif opcion == "4":
            dao.eliminar(1)
        elif opcion == "5":
            pelicula = PeliculaDTO(1, "Matrix Reloaded", 138, "2003-05-15", 2, 2, "Wachowski")
            dao.modificar(pelicula)
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

menu()
