from ..models.libro import Libro


class InventarioController:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, cantidad, isbn, titulo, autor, genero):
        if isbn in self.libros:
            self.libros[isbn].cantidad += cantidad
            return f"Se han agregado {cantidad} unidades al libro con ISBN {isbn}. Total disponible: {self.libros[isbn].cantidad}"
        else:
            nuevo_libro = Libro(len(self.libros) + 1, titulo, autor, genero, cantidad, isbn)
            self.libros[isbn] = nuevo_libro
            return f"Libro agregado con éxito. Total disponible: {nuevo_libro.cantidad}"

    def obtener_catalogo(self):
        return [str(l) for l in self.libros.values()]


if __name__ == "__main__":
    inventario = InventarioController()
    print(inventario.agregar_libro(5, "978-3-16-148410-0", "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela"))
    print(inventario.agregar_libro(3, "978-0-14-044913-6", "La Odisea", "Homero", "Épica"))
    print(inventario.obtener_catalogo())