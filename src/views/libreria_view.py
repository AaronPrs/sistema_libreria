class LibreriaView:
    def __init__(self, inventario_controller, prestamos_controller, usuarios_controller=None):
        self.inventario_controller = inventario_controller
        self.prestamos_controller = prestamos_controller
        self.usuarios_controller = usuarios_controller

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de la Librería ---")
            print("1. Agregar libro al inventario")
            print("2. Ver catálogo de libros")
            print("3. Crear usuario")
            print("4. Ver usuarios")
            print("5. Crear préstamo")
            print("6. Ver préstamos")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.ver_catalogo()
            elif opcion == "3":
                self.crear_usuario()
            elif opcion == "4":
                self.ver_usuarios()
            elif opcion == "5":
                self.crear_prestamo()
            elif opcion == "6":
                self.ver_prestamos()
            elif opcion == "7":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def agregar_libro(self):
        try:
            cantidad = int(input("Ingrese la cantidad de libros: "))
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero = input("Ingrese el género del libro: ")

            resultado = self.inventario_controller.agregar_libro(cantidad, isbn, titulo, autor, genero)
            print(resultado)
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")

    def ver_catalogo(self):
        catalogo = self.inventario_controller.obtener_catalogo()
        if catalogo:
            print("\n--- Catálogo de Libros ---")
            for libro in catalogo:
                print(libro)
        else:
            print("No hay libros en el inventario.")

    def crear_usuario(self):
        try:
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo del usuario: ")
            telefono = input("Ingrese el teléfono del usuario: ")
            direccion = input("Ingrese la dirección del usuario: ")

            resultado = self.usuarios_controller.agregar_usuario(nombre, correo, telefono, direccion)
            print(resultado)
        except Exception as e:
            print(f"Error al crear usuario: {e}")

    def ver_usuarios(self):
        usuarios = self.usuarios_controller.obtener_usuarios()
        if usuarios:
            print("\n--- Usuarios ---")
            for usuario in usuarios:
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    def crear_prestamo(self):
        try:
            id_usuario = int(input("Ingrese el ID del usuario: "))
            id_libro = int(input("Ingrese el ID del libro: "))
            isbn_libro = input("Ingrese el ISBN del libro: ")
            fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD HH:MM:SS): ")

            resultado = self.prestamos_controller.crear_prestamo(id_usuario, id_libro, isbn_libro, fecha_prestamo)
            print(resultado)
        except ValueError:
            print("ID inválido. Debe ser un número entero.")

    def ver_prestamos(self):
        prestamos = self.prestamos_controller.obtener_prestamos()
        if prestamos:
            print("\n--- Préstamos ---")
            for prestamo in prestamos:
                print(prestamo)
        else:
            print("No hay préstamos registrados.")