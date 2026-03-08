# Importamos las clases necesarias del proyecto
from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


# Función que muestra el menú principal del sistema
def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Prestar libro")
    print("5. Buscar libro por título")
    print("6. Buscar libro por autor")
    print("7. Buscar libro por categoría")
    print("8. Listar libros de un usuario")
    print("0. Salir")


# Función principal del programa
def main():

    # Creamos una instancia del servicio de biblioteca
    biblioteca = BibliotecaServicio()

    # Bucle principal del programa
    while True:

        # Mostramos el menú
        mostrar_menu()

        # Pedimos al usuario elegir una opción
        opcion = input("Seleccione una opción: ")

        # Opción 1: Añadir libro
        if opcion == "1":

            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")

            # Creamos un objeto Libro
            libro = Libro(titulo, autor, categoria, isbn)

            # Lo agregamos a la biblioteca
            biblioteca.agregar_libro(libro)

            print("Libro añadido correctamente.")


        # Opción 2: Quitar libro
        elif opcion == "2":

            isbn = input("Ingrese el ISBN del libro a eliminar: ")

            biblioteca.quitar_libro(isbn)

            print("Libro eliminado si existía.")


        # Opción 3: Registrar usuario
        elif opcion == "3":

            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")

            usuario = Usuario(nombre, user_id)

            biblioteca.registrar_usuario(usuario)


        # Opción 4: Prestar libro
        elif opcion == "4":

            isbn = input("ISBN del libro: ")
            user_id = input("ID del usuario: ")

            biblioteca.prestar_libro(isbn, user_id)


        # Opción 5: Buscar por título
        elif opcion == "5":

            titulo = input("Ingrese el título: ")

            biblioteca.buscar_por_titulo(titulo)


        # Opción 6: Buscar por autor
        elif opcion == "6":

            autor = input("Ingrese el autor: ")

            biblioteca.buscar_por_autor(autor)


        # Opción 7: Buscar por categoría
        elif opcion == "7":

            categoria = input("Ingrese la categoría: ")

            biblioteca.buscar_por_categoria(categoria)


        # Opción 8: Ver libros prestados de un usuario
        elif opcion == "8":

            user_id = input("ID del usuario: ")

            biblioteca.listar_libros_usuario(user_id)


        # Opción 0: Salir
        elif opcion == "0":

            print("Saliendo del sistema...")
            break


        # Si el usuario escribe algo incorrecto
        else:
            print("Opción no válida, intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()