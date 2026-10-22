from modelos.utils import leer_numero
from modelos.Proyecto import Proyecto

class Proyecto_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*30 + "#"*7)
        print("|" + " "*5 + "Proyectos: Gestion" + " "*19 + "|")
        print("|" + " "*8 + "1." + " "*19 + "|")
        print("#"*7 + "-"*30 + "#"*7)
        
        return leer_numero("ingrese una opcion")
