from view.Main_view import Main_view
from controller.Empleado_controller import Empleado_controller
from controller.Departamento_controller import Derpartamento_controller
from controller.Proyecto_controller import Proyecto_controller
from controller.Registro_hora_controller import Registro_hora_controller

class Main_controller:
    def __init__(self):
        self.view = Main_view()
        self.empleado = Empleado_controller()
        self.departamento = Derpartamento_controller()
        self.proyecto = Proyecto_controller()
        self.registro_hora = Registro_hora_controller()
    
    def ejecutar(self) -> None:
        while True:
            opcion = self.view.menu()
            
            match opcion:
                case 1:
                    self.empleado.ejecutar()
                case 2:
                    self.departamento.ejecutar()
                case 3:
                    self.proyecto.ejecutar()
                case 4:
                    self.registro_hora.ejecutar()
                case 0:
                    self.view.mensaje("cerrando programa")
                    break
                case _:
                    self.view.mensaje("opcion invalida")