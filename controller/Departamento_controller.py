from view.Departamento_view import Departamento_view
from modelos.Departamento_dao import Departamento_dao

class Derpartamento_controller:
    def __init__(self):
        self.view = Departamento_view()
        self.depa_dao = Departamento_dao()
    
    def ejecutar(self) -> None:
        while True:
            opcion = self.view.menu()
            
            match opcion:
                case 1:
                    pass
                case 0:
                    self.view.mensaje("saliendo del gestor de Departamentos")
                    break
                case _:
                    self.view.mensaje("opcion invalida")