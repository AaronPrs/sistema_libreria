from ..models.prestamo import Prestamo
from .inventario_controller import InventarioController
from .usuarios_controller import UsuariosController


class PrestamosController:
    def __init__(self):
        self.prestamos = []
        self.contador_id = 1
        self.inventario = InventarioController()
        self.usuarios = UsuariosController()

    def crear_prestamo(self, id_usuario, id_libro, isbn_libro, fecha_devolucion):
        # verificar usuario existente
        if id_usuario not in self.usuarios.usuarios:
            return f"ERROR: El usuario con ID {id_usuario} no existe."

        # verificar libro en inventario y disponibilidad
        if isbn_libro not in self.inventario.libros:
            return f"ERROR: El libro con ISBN {isbn_libro} no existe en el inventario."
        if self.inventario.libros[isbn_libro].cantidad <= 0:
            return f"ERROR: No hay unidades disponibles del libro con ISBN {isbn_libro}."

        # crear préstamo
        id_prestamo = self.contador_id
        nuevo = Prestamo(id_prestamo, id_usuario, id_libro, isbn_libro, fecha_devolucion)
        self.prestamos.append(nuevo)
        self.contador_id += 1

        # descontar del inventario
        self.inventario.libros[isbn_libro].cantidad -= 1

        return f"Préstamo creado: {nuevo}"

    def obtener_prestamos(self):
        return [str(p) for p in self.prestamos]


if __name__ == "__main__":
    pc = PrestamosController()
    # crear datos de ejemplo: un usuario y un libro en el inventario
    pc.usuarios.agregar_usuario("Juan Pérez", "juan@example.com", "1234567890", "Calle 123")
    pc.inventario.agregar_libro(5, "978-3-16-148410-0", "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")

    print(pc.crear_prestamo(1, 1, "978-3-16-148410-0", "2026-08-30 12:00:00"))
    print(pc.obtener_prestamos())
