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
    def formular_proyecto():
        print("\n" + "-"*7 + "AGREGAR PROYECTO" + "-"*7)
        nombre = input("ingrese un nombre: ")
        presupuesto = leer_numero("ingrese un presupuesto: ")
        fecha_inicio = input("ingrese una fecha: ")
        descripcion = input("describa el proyecto: ")
        
        return {
            "nombre": nombre,
            "presupuesto": presupuesto,
            "fecha inicio": fecha_inicio,
            "descripcion": descripcion
        }
    
    @staticmethod
    def formular_actualizacion(proyect: Proyecto):
        print("\n" + "-"*7 + "ACTUALIZAR PROYECTO" "-"*7)
        nuevo_nombre = input(f"nombre actual ({proyect.nombre}): ")
        
        nuevo_presupuesto = leer_numero(f"presupuesto actual (${proyect.presupuesto}): ")
        
        nueva_fecha_inicio = input(f"fecha actual ({proyect.fecha_inicio})")
        
        nueva_descripcion = input(f"descripcion actual ({proyect.descripcion})")
        
        return {
            "nombre": nuevo_nombre,
            "presupuesto": nuevo_presupuesto,
            "fecha inicio": nueva_fecha_inicio,
            "descripcion": nueva_descripcion
        }
    
    @staticmethod
    def confirmar_eliminacion(proyecto: Proyecto) -> bool:
        return confirmar(f"desea eliminar el proyecto {proyecto.nombre}: ")
    
    @staticmethod
    def mostrar_uno(proy: Proyecto):
        print("\n" + "-"*7 + "DATOS DEL PROYECTO" + "-"*7)
        print(proy)
    
    @staticmethod
    def mostrar_lista(proys: lsit[Proyecto]):
        print("\n" + "-"*7 + "PROYECTOS" + "-"*7)
        if not proys:
            print("no hay proyectos")
        else:
            for proy in proys:
                print(proy)
    