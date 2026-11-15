from sqlite3 import Cursor
from config.database import Database
from modelos.Proyecto import Proyecto

class Proyecto_dao:
    @staticmethod
    def crear(proyecto: Proyecto) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO proyecto
                (nombre, presupuesto, fecha_inicio, descripcion)
                VALUES (?, ?, ?, ?)
            """, (proyecto.nombre, proyecto.presupuesto, proyecto.fecha_inicio, proyecto.descripcion))
            conn.commit()
            proyecto.id_proyecto = cursor.lastrowid
            return True
        except Exception as e:
            print(f"err:: no se pudo crear el proyecto ::err = {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def obtener_todos() -> list[Proyecto]:
        conn = Database().get_connection()
        proyectos: list[Proyecto] = []
        
        try:
            cursor: Cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id_proyecto,
                nombre,
                presupuesto,
                fecha_inicio,
                descripcion
                FROM proyecto
            """)
            filas = cursor.fetchall()
            for fila in filas:
                proyectos.append(Proyecto(fila['nombre'],
                            fila['presupuesto'],
                            fila['fecha_inicio'],
                            fila['descripcion'],
                            fila['id_proyecto']))
        except Exception as e:
            print(f"err:: no se pudo obtener los proyectos ::err = {e}")
        finally:
            conn.close()
        return proyectos
    
    @staticmethod
    def obtener_por_id(id: int) -> Proyecto:
        conn = Database().get_connection()
        proyecto: Proyecto = None
        
        try: 
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                    SELECT id_proyecto,
                    nombre,
                    presupuesto,
                    fecha_inicio,
                    descripcion
                    FROM proyecto WHERE id_proyecto = ?
                """, (id, ))
            fila = cursor.fetchone()
            
            if fila:
                proyecto = Proyecto(fila['nombre'], fila['presupuesto'], fila['fecha_inicio'], fila['descripcion'], fila['id_proyecto'])
        except Exception as e:
            print(f"err:: no se pudo obtener el proyecto ::err = {e}")
        finally:
            conn.close()
        return proyecto
    
    @staticmethod
    def actualizar(proyecto: Proyecto) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                    UPDATE proyecto
                    SET nombre = ?,
                    presupuesto = ?,
                    fecha_inicio = ?,
                    descripcion = ?
                    WHERE id_proyecto = ?
                """, (proyecto.nombre, proyecto.presupuesto, proyecto.fecha_inicio, proyecto.descripcion, proyecto.id_proyecto))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo actualizar el proyecto ::err = {e}")
            return False
        finally:
            conn.close()
            
    @staticmethod
    def eliminar(id: int) -> bool:
        conn = Database().get_connection()
        
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                    DELETE FROM proyecto
                    WHERE id_proyecto = ?
                """, (id, ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"err:: no se pudo eliminar el proyecto ::err = {e}")
            return False
        finally:
            conn.close()
            
    @staticmethod
    def asignar_empleado(id_empleado: int, id_proyecto: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO asignacion_proyecto (id_empleado, id_proyecto)
                VALUES (?, ?)
            """, (id_empleado, id_proyecto))
            conn.commit()
            return True

        except Exception as e:
            print(f"err:: no se pudo asignar el empleado al proyecto ::err = {e}")
            return False

        finally:
            conn.close()