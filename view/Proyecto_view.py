from modelos.utils import leer_numero
from modelos.Proyecto import Proyecto

class Proyecto_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*30 + "#"*7)
        print("|" + " "*5 + "Proyectos: Gestion" + " "*19 + "|")
        print("|" + " "*8 + "1. agregar proyecto" + " "*15 + "|")
        print("|" + " "*8 + "2. editar proyecto" + " "*16 + "|")
        print("|" + " "*8 + "3. eliminar proyecto" + " "*14 + "|")
        print("|" + " "*8 + "4. imprimir proyecto" + " "*14 + "|")
        print("|" + " "*8 + "5. imprimir todos los proyectos" + " "*3 + "|")
        print("|" + " "*8 + "0. volver al menu principal" + " "*7 + "|")
        print("#"*7 + "-"*30 + "#"*7)
        
        return leer_numero("ingrese una opcion: ")
    
    @staticmethod
    def mensaje(msg: str) -> None:
        print(f"[Proyectos]: {msg}")
