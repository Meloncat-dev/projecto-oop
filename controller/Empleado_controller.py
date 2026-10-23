from view.Empleado_view import Empleado_view

class Empleado_controller:
    def __init__(self):
        self.view = Empleado_view()
    
    def ejecutar(self) -> None:
        while True:
            opcion = self.view.menu()
            
            match opcion:
                case 1:
                    pass
                case 0:
                    self.view.mensaje("saliendo del gestor de Empleados")
                    break
                case _:
                    self.view.mensaje("opcion invalida")