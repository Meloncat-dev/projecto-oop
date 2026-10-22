from modelos.utils import leer_numero

class Main_view:
    @staticmethod
    def menu() -> int:
        print("\n" + "#"*7 + "-"*30 + "#"*7)
        print("|" + " "*5 + "Echotech solutions:Menu principal" + " "*4 + "|")
        print("|" + " "*8 + "1. Gestion de Empleados" + " "*11 + "|")
        print("|" + " "*8 + "2. Gestion de Departamentos" + " "*7 + "|")
        print("|" + " "*8 + "3. Gestion de Proyectos" + " "*11 + "|")
        print("|" + " "*8 + "4. Gestion de Registros de hora" + " "*3 + "|")
        print("|" + " "*8 + "0. salir" + " "*26 + "|")
        print("#"*7 + "-"*30 + "#"*7)
        
        return leer_numero("ingresa una opcion: ")