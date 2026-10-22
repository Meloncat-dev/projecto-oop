from modelos.utils import leer_numero
from modelos.Departamento import Departamento

class Departamento_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*33 + "#"*7)
        print("|" + " "*6 + "Departamento: Gestion" + " "*18 + "|")
        print("|" + " "*9 + "1. agregar Departamento" + " "*13 + "|")
        print("|" + " "*9 + "1. editar Departamento" + " "*14 + "|")
        print("|" + " "*9 + "1. eliminar Departamento" + " "*12 + "|")
        print("|" + " "*9 + "1. imprimir Departamento" + " "*12 + "|")
        print("|" + " "*9 + "1. imprimir todos los Departamentos" + " "*1 + "|")
        print("|" + " "*9 + "1. agregar Departamento" + " "*13 + "|")
        print("#"*7 + "-"*33 + "#"*7)
        
        return leer_numero("ingrese una opcion: ")