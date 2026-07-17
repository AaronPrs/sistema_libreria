from src.controller.inventario_controller import InventarioController
from src.controller.usuarios_controller import UsuariosController
from src.controller.prestamos_controller import PrestamosController

def main():
    inventario_controller = InventarioController()
    usuarios_controller = UsuariosController()
    prestamos_controller = PrestamosController()

    # Agregar libros al inventario
    print(inventario_controller.agregar_libro(5, "978-3-16-148410-0", "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela"))
    print(inventario_controller.agregar_libro(3, "978-0-14-044913-6", "La Odisea", "Homero", "Épica"))

    # Agregar usuarios
    print(usuarios_controller.agregar_usuario("Juan Pérez", "juan@example.com", "1234567890", "Calle 123"))