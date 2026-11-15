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
        print("\n------- AGREGAR PROYECTO -------")
        nombre = input("Ingrese el nombre del proyecto: ")
        presupuesto = input("Ingrese el presupuesto: ")
        fecha_inicio = input("Ingrese la fecha de inicio (AAAA-MM-DD): ")
        descripcion = input("Ingrese una descripción: ")

        return {
            "nombre": nombre,
            "presupuesto": presupuesto,
            "fecha_inicio": fecha_inicio,
            "descripcion": descripcion
        }

    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("Ingrese un ID: ")

    @staticmethod
    def mostrar_proyecto(proyecto: Proyecto) -> None:
        print("\n------- DATOS DEL PROYECTO -------")
        print(proyecto)
        print("-" * 36)

    @staticmethod
    def mostrar_lista(proyectos: list[Proyecto]) -> None:
        print("\n------- PROYECTOS -------")
        if not proyectos:
            print("No hay proyectos")
        else:
            for proyecto in proyectos:
                print(proyecto)
        print("-" * 27)

    @staticmethod
    def formular_edicion(proyecto: Proyecto) -> dict:
        print(f"\n------- EDITANDO PROYECTO [{proyecto.id_proyecto}] -------")
        print("Deje en blanco los campos que no desea cambiar.")

        nombre = input(f"Nombre actual ({proyecto.nombre}): ")
        presupuesto = input(f"Presupuesto actual ({proyecto.presupuesto}): ")
        fecha = input(f"Fecha actual ({proyecto.fecha_inicio}): ")
        descripcion = input(
            f"Descripción actual ({proyecto.descripcion or 'Sin descripción'}): "
        )

        return {
            "nombre": nombre.strip() or proyecto.nombre,
            "presupuesto": presupuesto.strip() or proyecto.presupuesto,
            "fecha_inicio": fecha.strip() or proyecto.fecha_inicio,
            "descripcion": descripcion.strip() or proyecto.descripcion
        }

    @staticmethod
    def confirmar_eliminacion(nombre: str) -> bool:
        return confirmar(
            f"¿Seguro que desea eliminar el proyecto '{nombre}'?"
        )

    @staticmethod
    def formular_asignacion() -> dict:
        print("\n------- ASIGNAR EMPLEADO A PROYECTO -------")
        id_proyecto = leer_numero("Ingrese el ID del proyecto: ")
        id_empleado = leer_numero("Ingrese el ID del empleado que desea asignar: ")

        return {
            "id_proyecto": id_proyecto,
            "id_empleado": id_empleado
        }