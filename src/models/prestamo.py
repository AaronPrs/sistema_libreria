from datetime import datetime

class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, isbn_libro, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.isbn_libro = isbn_libro
        self.fecha_prestamo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f"Prestamo(id_prestamo={self.id_prestamo}, id_usuario={self.id_usuario}, id_libro={self.id_libro}, isbn_libro={self.isbn_libro}, fecha_prestamo={self.fecha_prestamo}, fecha_devolucion={self.fecha_devolucion})"
    
prueba_prestamo = Prestamo(1, 1, 1, "978-3-16-148410-0", "2024-06-30 12:00:00")

print(prueba_prestamo)