from modelos.utils import leer_numero
from modelos.Empleado import Empleado
from modelos.Departamento import Departamento

class Empleado_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*30 + "#"*7)
        print("|" + " "*5 + "Empleado: Gestion" + " "*20 + "|")
        print("|" + " "*8 + "1. agregar Empleado" + " "*15 + "|")
        print("|" + " "*8 + "2. editar Empleado" + " "*16 + "|")
        print("|" + " "*8 + "3. eliminar Empleado" + " "*14 + "|")
        print("|" + " "*8 + "4. imprimir Empleado" + " "*14 + "|")
        print("|" + " "*8 + "5. imprimir todos los Empleados" + " "*3 + "|")
        print("|" + " "*8 + "0. volver al menu principal" + " "*7 + "|")
        print("#"*7 + "-"*30 + "#"*7)
        return leer_numero("ingrese una opcion: ")
    
    @staticmethod
    def mensaje(msg: str) -> None:
        print(f"[Empleados]: {msg}")