from modelos.utils import leer_numero, confirmar
from modelos.Empleado import Empleado
from modelos.Departamento import Departamento
from modelos.Departamento_dao import Departamento_dao


class Empleado_view:

    @staticmethod
    def menu() -> int:
        print("\n" + "#" * 7 + "-" * 30 + "#" * 7)
        print("|" + " " * 5 + "Empleado: Gestion" + " " * 20 + "|")
        print("|" + " " * 8 + "1. agregar Empleado" + " " * 15 + "|")
        print("|" + " " * 8 + "2. editar Empleado" + " " * 16 + "|")
        print("|" + " " * 8 + "3. eliminar Empleado" + " " * 14 + "|")
        print("|" + " " * 8 + "4. imprimir Empleado" + " " * 14 + "|")
        print("|" + " " * 8 + "5. imprimir todos los Empleados" + " " * 3 + "|")
        print("|" + " " * 8 + "0. volver al menu principal" + " " * 7 + "|")
        print("#" * 7 + "-" * 30 + "#" * 7)

        return leer_numero("ingrese una opcion: ")

    @staticmethod
    def mensaje(msg: str) -> None:
        print(f"[Empleados]: {msg}")
    
    @staticmethod
    def formulario_creacion_empleado(depas: list[Departamento]) -> dict:
        print("\n" + "-"*7 + "AGREGAR EMPLEADO" + "-"*7)
        nombre = input("ingrese el nombre del empleado")
        rut = input("ingrese un rut (xxxxxxxx-x(el caracter despues del guion puede ser numerico o letra)): ")
        email = input("ingrese un email (ejemplo@mail.dominio): ")
        
        print("-"*4 + "LISTA DE DEPARTAMENTOS" + "-"*4)
        if depas:
            for d in depas:
                print(d)
        else:
            print("no hay departamentos")
        
        depa_op = leer_numero("ingrese el id del departamento")
        depa_id = depa_op if depas or depa_op > 0 else None
        
        return {
            "nombre": nombre,
            "rut": rut,
            "email": email,
            "depa id": depa_id
        }
    
    @staticmethod
    def formulario_actualisacion(emp: Empleado) -> dict:
        print("\n" + "-"*7 + "EDITANDO DEPARTAMENTO" + "-"*7)
        print("-"*7 + "DEJE EN BLANCO SI NO QUIERE CAMBIAR" + "-"*7)
        nuevo_nombre = input(f"nombre actual ({emp.nombre}): ")
        
        nuevo_rut = input(f"rut actual ({emp.rut}): ")
        try:
            nuevo_rut = nuevo_rut if nuevo_rut.strip() and len(nuevo_rut) == 10 and "-" in nuevo_rut else emp.rut
        except ValueError:
            nuevo_rut = emp.rut
        
        nuevo_email = input(f"email actual ({emp.email}): ")
        try:
            nuevo_email = nuevo_email if nuevo_email.strip() and "@" in nuevo_email else emp.email
        except ValueError:
            nuevo_email = emp.email
            
        return {
            "nombre": nuevo_nombre,
            "rut": nuevo_rut,
            "email": nuevo_email
        }
    
    @staticmethod
    def mostrar_uno(emp: Empleado):
        print("\n" + "-"*7 + "DATOS EMPLEADO" + "-"*7)
        print(emp)
        

    @staticmethod
    def mostrar_lista(emps: list[Empleado]):
        print("\n" + "-"*7 + "EMPLEADOS" + "-"*7)
        if not emps:
            print("no hay empleados")
        else:
            for emp in emps:
                print(emp)
        print("-"*23)
            
    @staticmethod
    def confirmar_eliminacion(empleado: str):
        return confirmar(f"seguro de que quiere eliminar a {empleado}: ")
    