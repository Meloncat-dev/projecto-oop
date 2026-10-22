import sqlite3

class Database:
    
    _instance = None
    _db_path = "empresa.db"
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def get_connection(self):
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = on")
        return conn

    def init_db(self) -> None:
        conn = self.get_connection()
        try:
            cursor: sqlite3.Cursor = conn.cursor()          
            # Tabla Departamento
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL
                )

            """)

            # Tabla empleado
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    rut TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    id_departamento INTEGER,
                    FOREIGN KEY (id_departamento) REFERENCES departamento (id_departamento)
                )
            """)

            # Tabla RegistroHoras
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registro_horas (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_empleado INTEGER,
                    fecha TEXT NOT NULL,
                    horas_trabajadas REAL NOT NULL,
                    descripcion_tarea TEXT,
                    FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado)
                )
            """)

            # Tabla Proyecto
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    presupuesto REAL NOT NULL,
                    fecha_inicio TEXT NOT NULL,
                    descripcion TEXT
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS asignacion_proyecto (
                    id_empleado INTEGER,
                    id_proyecto INTEGER,
                    
                    PRIMARY KEY (id_empleado, id_proyecto),
                    
                    FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado),
                    FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

if __name__ == "__main__":
    try:
        db = Database()
        db.init_db()
        print("Base de datos inicializada correctamente.")
    except sqlite3.Error as e:
        print(f"ERROR: {e}")
