from view.Registro_hora_view import Resgistro_hora_view

class Registro_hora_controller:
    def __init__(self):
        self.view = Resgistro_hora_view()
        
    def ejecutar(self):
        while True:
            opcion = self.view.menu()
            
            match opcion:
                case 1:
                    pass
                case 0:
                    self.view.mensaje("saliendo del gestor de Registros de hora")
                    break
                case _:
                    self.view.mensaje("opcion invalida")