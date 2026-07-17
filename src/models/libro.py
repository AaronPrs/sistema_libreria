class Libro:
    def __init__(self, id_libro, titulo, autor, genero, cantidad, isbn):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad = cantidad
        self.isbn = isbn

    def __str__(self):
        return f"id:{self.id}, titulo:{self.titulo}, autor:{self.autor}, genero:{self.genero}, cantidad:{self.cantidad}, isbn:{self.isbn})"

if __name__ == "__main__":
    libro_ejemplo = Libro(1, "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 5, "978-3-16-148410-0")
    print(libro_ejemplo)