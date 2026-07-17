from src.controller.inventario_controller import InventarioController
from src.controller.usuarios_controller import UsuariosController
from src.controller.prestamos_controller import PrestamosController
from src.views.libreria_view import LibreriaView


def main():
    inventario_controller = InventarioController()
    usuarios_controller = UsuariosController()
    prestamos_controller = PrestamosController(inventario_controller, usuarios_controller)

    # Agregar datos iniciales sin imprimirlos en consola
    inventario_controller.agregar_libro(5, "978-3-16-148410-0", "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")
    inventario_controller.agregar_libro(3, "978-0-14-044913-6", "La Odisea", "Homero", "Épica")
    usuarios_controller.agregar_usuario("Juan Pérez", "juan@example.com", "1234567890", "Calle 123")

    vista = LibreriaView(inventario_controller, prestamos_controller, usuarios_controller)
    vista.mostrar_menu()


if __name__ == "__main__":
    main()