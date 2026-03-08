# Importamos las clases de los modelos
from modelos.libro import Libro
from modelos.usuario import Usuario


# Clase que contiene toda la lógica del sistema de biblioteca
class BibliotecaServicio:

    # Constructor de la clase
    def __init__(self):

        # Diccionario que almacena los libros disponibles
        # clave -> ISBN
        # valor -> objeto Libro
        self.libros = {}

        # Diccionario para almacenar los usuarios registrados
        # clave -> ID del usuario
        # valor -> objeto Usuario
        self.usuarios = {}

        # Set para garantizar que los IDs de usuario sean únicos
        self.ids_usuarios = set()


    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):

        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente")
        else:
            print("El libro ya existe en la biblioteca")


    # Método para eliminar un libro de la biblioteca
    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado correctamente")
        else:
            print("El libro no existe")


    # Método para registrar un nuevo usuario
    def registrar_usuario(self, usuario):

        if usuario.user_id not in self.ids_usuarios:

            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)

            print("Usuario registrado correctamente")

        else:
            print("El ID del usuario ya existe")


    # Método para eliminar un usuario del sistema
    def eliminar_usuario(self, user_id):

        if user_id in self.usuarios:

            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)

            print("Usuario eliminado correctamente")

        else:
            print("Usuario no encontrado")


    # Método para prestar un libro a un usuario
    def prestar_libro(self, isbn, user_id):

        if isbn not in self.libros:
            print("El libro no está disponible")
            return

        if user_id not in self.usuarios:
            print("Usuario no encontrado")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[user_id]

        usuario.prestar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente")


    # Método para devolver un libro
    def devolver_libro(self, libro, user_id):

        if user_id not in self.usuarios:
            print("Usuario no encontrado")
            return

        usuario = self.usuarios[user_id]

        usuario.devolver_libro(libro)

        self.libros[libro.isbn] = libro

        print("Libro devuelto correctamente")


    # Método para buscar libros por título
    def buscar_por_titulo(self, titulo):

        encontrado = False

        for libro in self.libros.values():

            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("No se encontraron libros con ese título")


    # Método para buscar libros por autor
    def buscar_por_autor(self, autor):

        encontrado = False

        for libro in self.libros.values():

            if libro.obtener_autor().lower() == autor.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("No se encontraron libros de ese autor")


    # Método para buscar libros por categoría
    def buscar_por_categoria(self, categoria):

        encontrado = False

        for libro in self.libros.values():

            if libro.categoria.lower() == categoria.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("No se encontraron libros en esa categoría")


    # Método para listar los libros prestados por un usuario
    def listar_libros_usuario(self, user_id):

        if user_id not in self.usuarios:
            print("Usuario no encontrado")
            return

        usuario = self.usuarios[user_id]

        if not usuario.libros_prestados:
            print("El usuario no tiene libros prestados")
            return

        print("Libros prestados:")

        for libro in usuario.libros_prestados:
            print(libro)