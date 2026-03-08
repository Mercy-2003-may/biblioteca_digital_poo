# Clase que representa a un usuario de la biblioteca
class Usuario:

    # Constructor de la clase
    # Se ejecuta cuando se crea un nuevo usuario
    def __init__(self, nombre, user_id):

        # Nombre del usuario
        self.nombre = nombre

        # Identificador único del usuario
        self.user_id = user_id

        # Lista donde se almacenan los libros que el usuario tiene prestados
        # Esto cumple con el requisito de usar una estructura de datos tipo lista
        self.libros_prestados = []


    # Método para prestar un libro al usuario
    def prestar_libro(self, libro):

        # Se agrega el libro a la lista de libros prestados
        self.libros_prestados.append(libro)


    # Método para devolver un libro
    def devolver_libro(self, libro):

        # Verificamos si el libro está en la lista antes de eliminarlo
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


    # Método que permite mostrar la información del usuario
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"