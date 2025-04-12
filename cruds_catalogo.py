import mysql.connector

class ConexionDB:
    def conectar(self):
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql',
            database='casaapuestas'
        )

# Usuarios
class Usuario(ConexionDB):
    def __init__(self) -> None:
        pass  

    def insertar_usuarios(self, telefono_usuario, nombre, correo, saldo, contrasena):
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO usuarios (telefono_usuario, nombre, correo, saldo, contrasena)
            VALUES (%s, %s, %s, %s, %s)
        ''', (telefono_usuario, nombre, correo, saldo, contrasena))
        
        conn.commit()
        conn.close()

    def leer_usuarios(self):
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        
        conn.close()
        return usuarios

    def actualizar_usuarios(self, telefono_usuario, nombre, correo, saldo, contrasena):
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE usuarios
            SET nombre = %s, correo = %s, saldo = %s, contrasena = %s
            WHERE telefono_usuario = %s
        ''', (nombre, correo, saldo, contrasena, telefono_usuario))
        
        conn.commit()
        conn.close()

    def eliminar_usuarios(self, telefono_usuario):
        conn = self.conectar()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM usuarios WHERE telefono_usuario = %s', (telefono_usuario,))
        
        conn.commit()
        conn.close()

# Categoria
class CategoriaCRUD(ConexionDB):
    def insertar_categoria(self, nombre_categoria):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Categoria (nombre_categoria) VALUES (%s)', (nombre_categoria,))
        conn.commit()
        conn.close()

    def leer_categorias(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id_categoria, nombre_categoria FROM Categoria')
        categorias = cursor.fetchall()
        conn.close()
        return categorias

    def actualizar_categoria(self, id_categoria, nombre_categoria):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('UPDATE Categoria SET nombre_categoria = %s WHERE id_categoria = %s', (nombre_categoria, id_categoria))
        conn.commit()
        conn.close()

    def eliminar_categoria(self, id_categoria):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Categoria WHERE id_categoria = %s', (id_categoria,))
        conn.commit()
        conn.close()

# Articulos
class ArticuloCRUD(ConexionDB):
    def insertar_articulo(self, codigo, nombre, descripcion, precio, stock, costo, id_categoria):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Articulos (codigo, nombre, descripcion, precio, stock, costo, id_categoria)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (codigo, nombre, descripcion, precio, stock, costo, id_categoria))
        conn.commit()
        conn.close()

    def leer_articulos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Articulos')
        articulos = cursor.fetchall()
        conn.close()
        return articulos

    def actualizar_articulo(self, codigo, nombre, descripcion, precio, stock, costo, id_categoria):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''UPDATE Articulos
                          SET nombre = %s, descripcion = %s, precio = %s, stock = %s, costo = %s, id_categoria = %s
                          WHERE codigo = %s''',
                       (nombre, descripcion, precio, stock, costo, id_categoria, codigo))
        conn.commit()
        conn.close()

    def eliminar_articulo(self, codigo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Articulos WHERE codigo = %s', (codigo,))
        conn.commit()
        conn.close()

# Cargo
class CargoCRUD(ConexionDB):
    def insertar_cargo(self, nombre_cargo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Cargo (nombre_cargo) VALUES (%s)', (nombre_cargo,))
        conn.commit()
        conn.close()

    def leer_cargos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id_cargo, nombre_cargo FROM Cargo')
        cargos = cursor.fetchall()
        conn.close()
        return cargos

    def actualizar_cargo(self, id_cargo, nombre_cargo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('UPDATE Cargo SET nombre_cargo = %s WHERE id_cargo = %s', (nombre_cargo, id_cargo))
        conn.commit()
        conn.close()

    def eliminar_cargo(self, id_cargo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Cargo WHERE id_cargo = %s', (id_cargo,))
        conn.commit()
        conn.close()

# Empleados
class EmpleadoCRUD(ConexionDB):
    def insertar_empleado(self, telefono_empleado, nombre, correo, contrasena, id_cargo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Empleados (telefono_empleado, nombre, correo, contrasena, id_cargo)
                          VALUES (%s, %s, %s, %s, %s)''',
                       (telefono_empleado, nombre, correo, contrasena, id_cargo))
        conn.commit()
        conn.close()

    def leer_empleados(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Empleados')
        empleados = cursor.fetchall()
        conn.close()
        return empleados

    def actualizar_empleado(self, telefono_empleado, nombre, correo, contrasena, id_cargo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''UPDATE Empleados
                          SET nombre = %s, correo = %s, contrasena = %s, id_cargo = %s
                          WHERE telefono_empleado = %s''',
                       (nombre, correo, contrasena, id_cargo, telefono_empleado))
        conn.commit()
        conn.close()

    def eliminar_empleado(self, telefono_empleado):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Empleados WHERE telefono_empleado = %s', (telefono_empleado,))
        conn.commit()
        conn.close()

# Eventos
class EventoCRUD(ConexionDB):
    def insertar_evento(self, nombre_evento, fecha_evento):  # quitamos id_Evento
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Eventos (nombre_evento, fecha_evento) VALUES (%s, %s)',
                    (nombre_evento, fecha_evento))
        conn.commit()
        conn.close()

    def leer_eventos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Eventos')
        eventos = cursor.fetchall()
        conn.close()
        return eventos

    def actualizar_evento(self, id_Evento, nombre_evento, fecha_evento):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('UPDATE Eventos SET nombre_evento = %s, fecha_evento = %s WHERE id_Evento = %s',
                       (nombre_evento, fecha_evento, id_Evento))
        conn.commit()
        conn.close()

    def eliminar_evento(self, id_Evento):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Eventos WHERE id_Evento = %s', (id_Evento,))
        conn.commit()
        conn.close()