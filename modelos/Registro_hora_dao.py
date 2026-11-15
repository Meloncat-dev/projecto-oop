from sqlite3 import Cursor
from config.database import Database
from modelos.RegistroHora import RegistroHora
from modelos.Empleado_dao import Empleado_dao
from modelos.Proyecto_dao import Proyecto_dao

class Registro_hora_dao:
    @staticmethod
    def crear(registro: RegistroHora) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            empleado_id = registro.empleado.id_empleado if registro.empleado else None
            proyecto_id = registro.proyecto.id_proyecto if registro.proyecto else None
            
            cursor.execute("""INSERT INTO registro_horas 
                    (id_empleado,
                    id_proyecto,
                    fecha,
                    horas_trabajadas,
                    descripcion_tarea) VALUES (?, ?, ?, ?, ?)"""
                    , (empleado_id,
                       proyecto_id,
                       registro.fecha,
                       registro.horas_trabajadas,
                       registro.descripcion_tarea))
            conn.commit()
            registro.id = cursor.lastrowid
            return True
        except Exception as e:
            print(f"err:: no se pudo crear el registro ::err = {e}")
            return False
        finally:
            conn.close()
        
    @staticmethod
    def obtener_todos() -> list[RegistroHora]:
        conn = Database().get_connection()
        registros: list[RegistroHora] = []
        
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute("""
                    SELECT id_registro,
                    id_empleado,
                    id_proyecto,
                    fecha,
                    horas_trabajadas,
                    descripcion_tarea
                    FROM registro_horas
                """)
            filas = cursor.fetchall()
            for fila in filas:
                empleado = None
                proyecto = None
                if fila['id_empleado'] is not None:
                    empleado = Empleado_dao.obtener_por_id(fila['id_empleado'])
                if fila['id_proyecto'] is not None:
                    proyecto = Proyecto_dao.obtener_por_id(fila['id_proyecto'])
                registros.append(RegistroHora(empleado,
                                        proyecto,
                                        fila['fecha'],
                                        fila['horas_trabajadas'],
                                        fila['descripcion_tarea'],
                                        fila['id_registro']))
        except Exception as e:
            print(f"err:: no se pudo obtener los empleados ::err = {e}")
        finally:
            conn.close()
        return registros
    
    @staticmethod
    def obtener_por_id(id: int) -> RegistroHora:
        conn = Database().get_connection()
        registro = None
        
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id_registro,
                id_empleado,
                id_proyecto,
                fecha,
                horas_trabajadas,
                descripcion_tarea
                FROM registro_horas
                WHERE id_registro = ?
                """, (id,))
            fila = cursor.fetchone()
            if fila:
                empleado = None
                proyecto = None
                if fila['id_empleado'] is not None:
                    empleado = Empleado_dao.obtener_por_id(fila['id_empleado'])
                if fila['id_proyecto'] is not None:
                    proyecto = Proyecto_dao.obtener_por_id(fila['id_proyecto'])
                registro = RegistroHora(empleado,
                            proyecto,
                            fila['fecha'],
                            fila['horas_trabajadas'],
                            fila['descripcion_tarea'],
                            fila['id_registro'])
        except Exception as e:
            print(f"err:: no se pudo obtener el registro ::err = {e}")
        finally:
            conn.close()
        return registro
    
    @staticmethod
    def actualizar(registro: RegistroHora) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            empleado_id = registro.empleado.id_empleado if registro.empleado else None
            proyecto_id = registro.proyecto.id_proyecto if registro.proyecto else None
            
            cursor.execute("""
                    UPDATE registro_horas
                    SET id_empleado = ?,
                    id_proyecto = ?,
                    fecha = ?,
                    horas_trabajadas = ?,
                    descripcion_tarea = ?
                    WHERE id_registro = ?
                """, (empleado_id, proyecto_id, registro.fecha, registro.horas_trabajadas, registro.descripcion_tarea, registro.id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo actualizar el registro ::err = {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def eliminar(id: int) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                    DELETE FROM registro_horas
                    WHERE id_registro = ?
                """, (id, ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo eliminar el registro ::err = {e}")
            return False
        finally:
            conn.close()