from ..models.usuario import Usuario


class UsuariosController:
    def __init__(self):
        self.usuarios = []
        self.contador_id = 1

    def agregar_usuario(self, nombre, correo, telefono, direccion):
        id_usuario = self.contador_id
        self.contador_id += 1
        if any(u.id_usuario == id_usuario for u in self.usuarios):
            return f"ERROR: El usuario con ID {id_usuario} ya existe."

        nuevo_usuario = Usuario(id_usuario, nombre, correo, telefono, direccion)
        self.usuarios.append(nuevo_usuario)
        return f"Usuario agregado con éxito: {nuevo_usuario}"

    def obtener_usuarios(self):
        return [str(u) for u in self.usuarios]


if __name__ == "__main__":
    usuarios_controller = UsuariosController()
    print(usuarios_controller.agregar_usuario("Juan Pérez", "juan@example.com", "1234567890", "Calle 123"))