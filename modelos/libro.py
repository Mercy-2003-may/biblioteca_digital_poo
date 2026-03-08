# Clase que representa un libro dentro del sistema de biblioteca
class Libro:

    # Constructor de la clase
    # Se ejecuta cuando se crea un nuevo objeto Libro
    def __init__(self, titulo, autor, categoria, isbn):

        # Guardamos el título y el autor dentro de una tupla
        # Esto cumple el requisito de usar una estructura de datos tipo tupla
        self.titulo_autor = (titulo, autor)

        # Categoría del libro
        self.categoria = categoria

        # ISBN del libro (identificador único)
        self.isbn = isbn


    # Método que retorna el título del libro
    def obtener_titulo(self):
        return self.titulo_autor[0]


    # Método que retorna el autor del libro
    def obtener_autor(self):
        return self.titulo_autor[1]


    # Método especial que permite mostrar el libro de forma legible
    def __str__(self):
        return f"{self.obtener_titulo()} - {self.obtener_autor()} ({self.categoria}) ISBN: {self.isbn}"