import unittest

from src.controller.inventario_controller import InventarioController
from src.controller.prestamos_controller import PrestamosController
from src.controller.usuarios_controller import UsuariosController


class PrestamosControllerTest(unittest.TestCase):
    def test_crear_prestamo_con_usuario_existente(self):
        inventario = InventarioController()
        usuarios = UsuariosController()
        prestamos = PrestamosController(inventario, usuarios)

        inventario.agregar_libro(2, "ISBN-TEST", "Libro de prueba", "Autor", "Género")
        usuarios.agregar_usuario("Ana", "ana@test.com", "1111", "Calle 1")
        usuarios.agregar_usuario("Luis", "luis@test.com", "2222", "Calle 2")

        resultado = prestamos.crear_prestamo(2, 1, "ISBN-TEST", "2026-07-18")

        self.assertIn("Préstamo creado", resultado)


if __name__ == "__main__":
    unittest.main()
