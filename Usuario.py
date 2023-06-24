from db_connection import conn

class Usuario:
    def __init__(self, usuario, permisos):
        self.nombre_usuario = usuario
        self.permisos = permisos


    def check_user_exists(self, usuario):
        cursor = conn.cursor()
        query = "SELECT usuario FROM USUARIO WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        cursor.close()

        if result is not None and result[0] == usuario:
            self.nombre_usuario = usuario
            return True

        return False


    def check_user_permission(self, usuario):
        cursor = conn.cursor()
        query = "SELECT permisos FROM USUARIO WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        cursor.close()

        if result is not None:
            self.permisos = result[0]
            return result[0]