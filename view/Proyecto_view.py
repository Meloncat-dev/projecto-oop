from modelos.utils import leer_numero, confirmar
from modelos.Proyecto import Proyecto


class Proyecto_view:

    @staticmethod
    def menu() -> int:
        print("\n" + "#" * 7 + "-" * 30 + "#" * 7)
        print("|" + " " * 5 + "Proyectos: Gestion" + " " * 19 + "|")
        print("|" + " " * 8 + "1. agregar proyecto" + " " * 15 + "|")
        print("|" + " " * 8 + "2. editar proyecto" + " " * 16 + "|")
        print("|" + " " * 8 + "3. eliminar proyecto" + " " * 14 + "|")
        print("|" + " " * 8 + "4. imprimir proyecto" + " " * 14 + "|")
        print("|" + " " * 8 + "5. imprimir todos los proyectos" + " " * 3 + "|")
        print("|" + " " * 8 + "6. asignar empleado a proyecto" + " " * 4 + "|")
        print("|" + " " * 8 + "0. volver al menu principal" + " " * 7 + "|")
        print("#" * 7 + "-" * 30 + "#" * 7)

        return leer_numero("ingrese una opcion: ")

    @staticmethod
    def mensaje(msg: str) -> None:
        print(f"[Proyectos]: {msg}")

    @staticmethod
    def formular_proyecto() -> dict:
        print("\n-------AGREGAR PROYECTO-------")
        nombre = input("ingresa un nombre para el proyecto: ")
        presupuesto = leer_numero("ingrese un presupuesto para el proyecto: ")
        fecha = input("ingrese la fecha del comienzo del proyecto: ")
        descripcion = input("describa en pocas palabras el proyecto: ")
        
        return {
            "nombre": nombre,
            "presupuesto": presupuesto,
            "fecha inicio": fecha,
            "descripcion": descripcion
        }
    
    @staticmethod
    def formular_edicion(proy: Proyecto) -> dict:
        nuevo_nombre = input("ingrese un nuevo nombre para el proyecto: ")
        
        try:
            nuevo_nombre = nuevo_nombre if nuevo_nombre.strip() and len(nuevo_nombre) >= 3 else proy.nombre
        except ValueError:
            nuevo_nombre = proy.nombre
        
        nuevo_presupuesto = leer_numero("ingrese el nuevo presupuesto: ")
        
        try:
            nuevo_presupuesto = nuevo_presupuesto if isinstance(nuevo_presupuesto, int) else proy.presupuesto
        except TypeError:
            nuevo_presupuesto = proy.presupuesto
        
        nueva_fecha = input("ingrese la nueva fecha de inicio: ")
        
        try:
            nueva_fecha = nueva_fecha if nueva_fecha.strip() and len(nueva_fecha) == 10 and nueva_fecha.count("/") == 2 else proy.fecha_inicio
        except ValueError:
            nueva_fecha = proy.fecha_inicio
        
        nueva_descripcion = input("ingrese la nueva descripcion(trate de que sea breve): ")
        
        try:
            nueva_descripcion = nueva_descripcion if nueva_descripcion.strip() else proy.descripcion
        except ValueError:
            nueva_descripcion = proy.descripcion
            
        return {
            "nombre": nuevo_nombre,
            "presupuesto": nuevo_presupuesto,
            "fecha": nueva_fecha,
            "descripcion": nueva_descripcion
        }
        
    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("ingrese un ID: ")
    
    @staticmethod
    def confirmar_eliminacion(proy: Proyecto) -> bool:
        return confirmar(f"esta seguro de eliminar el proyecto '{proy.nombre}': ")
    
    @staticmethod
    def mostrar_proyecto(proy: Proyecto) -> None:
        print("\n-------DATOS DEL PROYECTO-------")
        print(proy)
        print("-"*32)
    
    @staticmethod
    def mostrar_lista(proys: list[Proyecto]) -> None:
        print("\n-------PROYECTOS-------")
        if not proys:
            print("no hay proyectos")
        else:
            for p in proys:
                print(p)
                print("-"*23)
            