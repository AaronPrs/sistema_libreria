from ..models.prestamo import Prestamo


class PrestamosController:
    def __init__(self, inventario_controller=None, usuarios_controller=None):
        self.prestamos = []
        self.contador_id = 1
        self.inventario = inventario_controller
        self.usuarios = usuarios_controller

    def crear_prestamo(self, id_usuario, id_libro, isbn_libro, fecha_devolucion):
        # verificar usuario existente
        if not any(usuario.id_usuario == id_usuario for usuario in self.usuarios.usuarios):
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



