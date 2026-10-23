from view.Proyecto_view import Proyecto_view

class Proyecto_controller:
    def __init__(self):
        self.view = Proyecto_view()
    
    def ejecutar(self) -> None:
        while True:
            opcion = self.view.menu()
            
            match opcion:
                case 1:
                    pass
                case 0:
                    self.view.mensaje("saliendo del gestor de Proyectos")
                    break
                case _:
                    self.view.mensaje("opcion invalida")
                    