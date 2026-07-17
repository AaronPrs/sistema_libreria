class Usuario:
    def __init__(self, id_usuario, nombre, correo, telefono, direccion):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"Usuario(id_usuario={self.id_usuario}, nombre={self.nombre}, correo={self.correo}, telefono={self.telefono}, direccion={self.direccion})"
    
prueba_usuario = Usuario(1, "Juan Pérez", "juan.perez@example.com", "1234567890", "Calle Principal 123")
print(prueba_usuario)