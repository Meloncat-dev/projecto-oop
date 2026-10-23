from sqlite3 import Cursor
from config.database import Database
from modelos.Departamento import Departamento

class Departamento_dao:
    @staticmethod
    def crear(departamento: Departamento) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute(
                "INSERT INTO departamento (nombre) VALUES (?)",
                (departamento.nombre,)
            )
            conn.commit()
            departamento.id_departamento = cursor.lastrowid
            return True
        except Exception as e:
            print(f"err:: no se pudo crear el departamento ::err = {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def obtener_todos() -> list[Departamento]:
        conn = Database().get_connection()
        departamentos: list[Departamento] = []
        
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "SELECT nombre, id_departamento FROM departamento"
            )
            filas = cursor.fetchall()
            for fila in filas:
                departamentos.append(Departamento(fila['nombre'], fila['id_departamento']))
        except Exception as e:
            print(f"err:: no se pudo obtener los departamentos ::err = {e}")
        finally:
            conn.close()
        return departamentos
    
    @staticmethod
    def obtener_por_id(id: int) -> Departamento:
        conn = Database().get_connection()
        depa: Departamento = None
        
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute("SELECT nombre, id_departamento FROM departamento WHERE id_departamento = ?", (id,))
            fila = cursor.fetchone()
            if fila:
                depa = Departamento(fila['nombre'], fila['id_departamento'])
        except Exception as e:
            print(f"err:: no se pudo obtener el empleado ::err = {e}")
        finally:
            conn.close()
        return depa
    
    @staticmethod
    def actualizar(departamento: Departamento) -> bool:
        if departamento.id_departamento is None:
            return False
        
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute("""UPDATE departamento
            SET nombre = ?
            WHERE id_departamento = ?
            """, (departamento.nombre, departamento.id_departamento))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo actualizar el departamento ::err = {e}")
            return False
        finally:
            conn.close()
            
    @staticmethod
    def eliminar(id: int) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM departamento
                WHERE id_departamento = ?
            """, (id, ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo eliminar el departamento ::err = {e}")
            return False
        finally:
            conn.close()
        