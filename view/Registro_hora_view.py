from modelos.utils import leer_numero
from modelos.RegistroHora import RegistroHora
from modelos.Empleado import Empleado
from modelos.Proyecto import Proyecto

class Resgistro_hora_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*36 + "#"*7)
        print("|" + " "*5 + "Registro Hora: Gestion" + " "*21 + "|")
        print("|" + " "*8 + "1. agregar Registro de hora" + " "*13 + "|")
        print("|" + " "*8 + "2. editar Registro de hora" + " "*14 + "|")
        print("|" + " "*8 + "3. eliminar Registro de hora" + " "*12 + "|")
        print("|" + " "*8 + "4. imprimir Registro de hora" + " "*12 + "|")
        print("|" + " "*8 + "5. imprimir todos los Registros de hora" + " "*1 + "|")
        print("|" + " "*8 + "0. volver al menu principal" + " "*13 + "|")
        print("#"*7 + "-"*36 + "#"*7)
        
        return leer_numero("ingrese una opcion: ")
    
    @staticmethod
    def mensaje(msg: str) -> None:
        print(f"[Registros Hora]: {msg}")
        
    @staticmethod
    def formular_registro_hora(emps: list[Empleado], proys: list[Proyecto]) -> dict:
        print("\n" + "-"*7 + "AGREGAR REGISTRO DE HORAS" + "-"*7)
        print("-"*12 + "LISTA EMPLEADOS" + "-"*12)
        
        if emps:
            for emp in emps:
                print(emp)
                print("-"*39)
        else:
            print("no hay empleados")
            return
        
        emp_op = leer_numero("que empleado va a elegir: ")
        emp_id = emp_op if emps or emp_op > 0 else None
        
        print("-"*12 + "LISTA PROYECTOS" + "-"*12)
        
        if proys:
            for proy in proys:
                print(proy)
                print("-"*39)
        else:
            print("no hay proyectos")
        
        proy_op = leer_numero("que proyecto va a elegir: ")
        proy_id = proy_op if proys or proy_op > 0 else None
        
        fecha = input("ingrese una fecha: ")
        
        horas = leer_numero("ingrese cuantas horas trabajo: ")
        
        descripcion = input("describa en que trabajo: ")
        
        return {
            "empleado": emp_id,
            "proyecto": proy_id,
            "fecha": fecha,
            "horas trabajadas": horas,
            "descripcion": descripcion            
        }        
        