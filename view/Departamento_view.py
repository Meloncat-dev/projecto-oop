from modelos.utils import leer_numero, confirmar
from modelos.Departamento import Departamento

class Departamento_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*33 + "#"*7)
        print("|" + " "*6 + "Departamento: Gestion" + " "*18 + "|")
        print("|" + " "*9 + "1. agregar Departamento" + " "*13 + "|")
        print("|" + " "*9 + "2. editar Departamento" + " "*14 + "|")
        print("|" + " "*9 + "3. eliminar Departamento" + " "*12 + "|")
        print("|" + " "*9 + "4. imprimir Departamento" + " "*12 + "|")
        print("|" + " "*9 + "5. imprimir todos los Departamentos" + " "*1 + "|")
        print("|" + " "*9 + "0. volver al menu principal" + " "*9 + "|")
        print("#"*7 + "-"*33 + "#"*7)
        
        return leer_numero("ingrese una opcion: ")
    
    @staticmethod
    def mensaje(msg: str) -> None:
        print(f"[Departamentos]: {msg}")
        
    @staticmethod
    def formular_depto():
        print("\n-------AGREGAR DEPARTAMENTO_______")
        nombre = input("ingrese un nombre para el departamento: ")
        
        return {"nombre": nombre}
    
    @staticmethod
    def solicitar_id():
        return leer_numero("ingrese un ID: ")
    
    @staticmethod
    def mostrar_dpto(depa):
        print("\n-------DATOS DEL DEPARTAMENTO-------")
        print(depa)
        print("-"*36)
        
    @staticmethod
    def mostrar_lista(depas):
        print("\n-------DEPARTAMENTOS-------")
        if not depas:
            print("no hay departamentos")
        else:
            for d in depas:
                print(d)
        print("-"*27)
    
    @staticmethod
    def formular_edicion(depa: Departamento):
        print(f"\n------- EDITANDO DEPARTAMENTO [{depa.id_departamento}]-------")
        print("-------DEJE EN BLANCO SI NO QUIERE CAMBIARLO-------")
        nuevo_nombre = input(f"Nombre actual ({depa.nombre}): ")
        if not nuevo_nombre.strip():
            nuevo_nombre = depa.nombre
        
        return {
            "id_departamento": depa.id_departamento,
            "nombre": nuevo_nombre
        }
    
    @staticmethod
    def confirmar_eliminacion(nombre):
        return confirmar(f"segure de que va a aliminar el departamento de '{nombre}'")
    