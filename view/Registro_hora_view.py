from modelos.utils import leer_numero, confirmar
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
        
    @staticmethod
    def formulario_actualizacion(register: RegistroHora, emps: list[Empleado], proys: list[Proyecto]) -> dict:
        print("\n-------ACTUALIZAR REGISTRO HORA-------")
        print("-"*12 + "LISTA EMPLEADOS" + "-"*12)
        
        if emps:
            for emp in emps:
                print(emp)
                print("-"*39)
        else:
            print("no hay empleados")
            return
        
        nuevo_emp_op = leer_numero("eliga el nuevo empleado: ")
        
        nuevo_emp_id = nuevo_emp_op if emps or nuevo_emp_op > 0 or not None else register.empleado.id_empleado
        
        print("-"*12 + "LISTA PROYECTOS" + "-"*12)
        
        if proys:
            for proy in proys:
                print(proy)
                print("-"*39)
        else:
            print("no hay proyectos")
        
        proy_op = leer_numero("que proyecto va a elegir: ")
        nuevo_proy_id = proy_op if proys or proy_op > 0 or not None else register.proyecto.id_proyecto
        
        nueva_fecha = input("ingrese la nueva fecha de registro: ")
                
        try:
            nueva_fecha = nueva_fecha if nueva_fecha.strip() and len(nueva_fecha) == 10 and nueva_fecha.count("/") == 2 else register.fecha
        except ValueError:
            nueva_fecha = register.fecha
            
        nueva_hora = leer_numero("ingrese las nueva cantidad de horas trabajadas: ")
        
        try:
            nueva_hora = nueva_hora if isinstance(nueva_hora, int) else register.horas_trabajadas
        except TypeError:
            nueva_hora = register.horas_trabajadas
            
        nueva_descripcion = input("ingrese la nueva descripcion(trate de que sea breve): ")
        
        try:
            nueva_descripcion = nueva_descripcion if nueva_descripcion.strip() else register.descripcion_tarea
        except ValueError:
            nueva_descripcion = register.descripcion_tarea
        
    
    @staticmethod
    def mostrar_registro(register: RegistroHora) -> None:
        print("\n-------DATOS DEL REGISTRO HORA-------")
        print(register)
        print("-"*37)
    
    @staticmethod
    def mostrar_lista(registers: list[RegistroHora]) -> None:
        print("\n-------REGISTROS HORA-------")
        if not registers:
            print("no hay registros de hora")
        else:
            for r in registers:
                print(r)
                print("-"*28)
    
    @staticmethod
    def solicitar_id() -> int:
        return leer_numero("ingrese un ID: ")
    
    @staticmethod
    def confirmar_eliminacion() -> bool:
        return confirmar("esta segurod e eliminar el registro hora: ")
        