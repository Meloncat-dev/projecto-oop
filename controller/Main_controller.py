from view.Main_view import Main_view
from controller.Auth_controller import Auth_controller
from controller.Empleado_controller import Empleado_controller
from controller.Departamento_controller import Departamento_controller
from controller.Proyecto_controller import Proyecto_controller
from controller.Registro_hora_controller import Registro_hora_controller
from modelos.Usuario import Usuario

class Main_controller:
    def __init__(self):
        self.view = Main_view()
        self.auth = Auth_controller()
        self.empleado = Empleado_controller()
        self.departamento = Departamento_controller()
        self.proyecto = Proyecto_controller()
        self.registro_hora = Registro_hora_controller()
        self.user_act: Usuario | None = None
    
    def ejecutar(self) -> None:
        
        self.user_act = self.auth.iniciar_secion()
        if not self.user_act:
            self.view.mensaje("el programa a finalizado devido a credenciales invalidas.")
            return
        
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
                case 5:
                    self.auth.ejecutar()
                case 9:
                    self.view.mensaje(f"cerrando la secion de '{self.user_act.username}'...")
                    self.user_act = self.auth.iniciar_secion()
                    if not self.user_act:
                        self.view.mensaje("el programa a finalizado por credenciales invalidas")
                        break
                case 0:
                    self.view.mensaje("cerrando programa")
                    break
                case _:
                    self.view.mensaje("opcion invalida")