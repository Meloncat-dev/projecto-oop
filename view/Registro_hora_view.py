from modelos.utils import leer_numero
from modelos.RegistroHora import RegistroHora

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