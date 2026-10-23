from modelos.Empleado import Empleado
from modelos.Departamento_dao import Departamento_dao
from sqlite3 import Cursor
from config.database import Database

class Empleado_dao:
    @staticmethod
    def crear(empleado: Empleado) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            dpto_id = empleado.departamento.id_departamento if empleado.departamento else None
            cursor.execute("""
                INSERT INTO empleado
                (nombre, rut, email, id_departamento) VALUES (?, ?, ?, ?)
            """, (empleado.nombre, empleado.rut, empleado.email, dpto_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"err:: no se pudo crear el empleado ::err = {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def eliminar(id: int) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM empleado WHERE id_empleado = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo eliminar el Empleado ::err = {e}")
            return False
        finally:
            conn.close()
            
    @staticmethod
    def actualizar(empleado: Empleado) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            dpto_id = empleado.departamento.id_departamento if empleado.departamento else None
            cursor.execute("""UPDATE empleado
                SET nombre = ?,
                rut = ?,
                email = ?,
                id_departamento = ? WHERE id_empleado = ?
            """, (empleado.nombre, empleado.rut, empleado.email, dpto_id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo actualizar el Empleado ::err = {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def obtene_por_id(id: int) -> Empleado:
        conn = Database().get_connection()
        empleado = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                SELECT id_empleado,
                nombre,
                rut,
                email,
                id_departamento
                FROM empleado WHERE id_empleado = ?
            """, (id, ))
            fila = cursor.fetchone()
            if fila:
                departamento = None
                if fila['id_departamento'] is not None:
                    departamento = Departamento_dao.obtener_por_id(fila['id_departamento'])
                empleado = Empleado(fila['nombre'], fila['rut'], fila['email'], fila['id_empleado'], departamento)
        except Exception as e:
            print(f"err:: no se encontro el Empleado ::err = {e}")
        finally:
            conn.close()
        return empleado
    
    @staticmethod
    def obtener_todo() -> list[Empleado]:
        conn = Database().get_connection()
        Empleados: list[Empleado] = []
        
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id_empleado,
                nombre,
                rut,
                email,
                id_empleado
                FROM empleado""")
            filas = cursor.fetchall()
            for fila in filas:
                departamento = None
                if fila['id_departamento'] is not None:
                    departamento = Departamento_dao.obtener_por_id(fila['id_departamento'])
                Empleados.append(Empleado(fila['nombre'],
                                fila['rut'],
                                fila['email'],
                                fila['id_empleado'],
                                departamento))
        except Exception as e:
            print(f"err:: no se pudo obtener los Empleados ::err = {e}")
        finally:
            conn.close()
        
        return Empleados