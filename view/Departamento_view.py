from modelos.utils import leer_numero
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
    