from modelos.Empleado import Empleado
from view.Empleado_view import Empleado_view
from modelos.Empleado_dao import Empleado_dao
from modelos.Departamento_dao import Departamento_dao

class Empleado_controller:
    def __init__(self):
        self.view = Empleado_view()
    
    def ejecutar(self) -> None:
        while True:
            opcion = self.view.menu()
            
            match opcion:
                case 1:
                    self.agregar()
                case 2:
                    self.editar()
                case 3:
                    self.eliminar()
                case 4:
                    self.imprimir_uno()
                case 5:
                    self.imprimir_todo()
                case 0:
                    self.view.mensaje("saliendo del gestor de Empleados")
                    break
                case _:
                    self.view.mensaje("opcion invalida")
                    
    def agregar(self):
        datos = self.view.formulario_creacion_empleado()
        
        depa = Departamento_dao.obtener_por_id(datos["depa id"])
        
        
        try:
            emp = Empleado(
                datos["nombre"],
                datos["rut"],
                datos["email"],
                depa
            )
            exito = Empleado_dao.crear(emp)
            
            if exito:
                self.view.mensaje("empleado creado con exito")
            else:
                self.view.mensaje("fallo al crear el empleado")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos {e}")
    
    def editar(self):
        id = self.view.pedir_id()
        
        emp = Empleado_dao.obtener_por_id(id)
        if not emp:
            self.view.mensaje("no se encontro ningun empleado")
            return
        
        
        
        datos = self.view.formulario_actualisacion(emp)
        
        depa = Departamento_dao.obtener_por_id(datos["depa id"])
        
        try:
            nuevo_emp = Empleado(
                datos["nombre"],
                datos["rut"],
                datos["email"],
                depa
            )
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"fallo en los datos {e}")
    
    def eliminar(self):
        id = self.view.pedir_id()
        
        emp = Empleado_dao.obtener_por_id(id)
        if not emp:
            self.view.mensaje("no se pudo encontrar al empleado")
            return
        
        if self.view.confirmar_eliminacion(emp.nombre):
            exito = Empleado_dao.eliminar(id)
            if exito:
                self.view.mensaje("eliminacion exitosa")
            else:
                self.view.mensaje("no se logro eliminar el empleado")
        else:
            self.view.mensaje("operacion cancelada")
    
    def imprimir_uno(self):
        pass
    
    def imprimir_todo(self):
        pass