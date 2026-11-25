from view.Registro_hora_view import Resgistro_hora_view
from modelos.RegistroHora import RegistroHora
from modelos.Registro_hora_dao import Registro_hora_dao
from modelos.Empleado_dao import Empleado_dao
from modelos.Proyecto_dao import Proyecto_dao

class Registro_hora_controller:
    def __init__(self):
        self.view = Resgistro_hora_view()
        
    def ejecutar(self):
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
                    self.mostrar()
                case 5:
                    self.mostrar_todo()
                case 0:
                    self.view.mensaje("saliendo del gestor de Registros de hora")
                    break
                case _:
                    self.view.mensaje("opcion invalida")
    
    def agregar(self):
        emps = Empleado_dao.obtener_todos()
        proys = Proyecto_dao.obtener_todos()
        
        datos = self.view.formular_registro_hora(emps, proys)
        emp = Empleado_dao.obtener_por_id(datos["empleado"])
        proy = Proyecto_dao.obtener_por_id(datos["proyecto"])
        
        try:
            register = RegistroHora(
                emp,
                proy,
                datos["fecha"],
                datos["horas"],
                datos["descripcion"]
            )
            
            exito = Registro_hora_dao.crear(register)
            
            if exito:
                self.view.mensaje("se creo exitosamente el registro hora")
            else:
                self.view.mensaje("fallo al crear el registro")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos {e}")
    
    def editar(self):
        id = self.view.solicitar_id()
        
        register = Registro_hora_dao.obtener_por_id(id)
        
        emps = Empleado_dao.obtener_todos()
        proys = Proyecto_dao.obtener_todos()
        
        datos = self.view.formulario_actualizacion(register, emps, proys)
        
        emp = Empleado_dao.obtener_por_id(datos["empleado"])
        proy = Proyecto_dao.obtener_por_id(datos["proyecto"])
        
        try:
            register.empleado = emp
            register.proyecto = proy
            register.fecha = datos["fecha"]
            register.horas_trabajadas = datos["horas"]
            register.descripcion_tarea = datos["descripcion"]
            
            exito = Registro_hora_dao.actualizar(register)
            
            if exito:
                self.view.mensaje("edicion exitosa")
            else:
                self.view.mensaje("fallo al editar")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos {e}")
    
    def eliminar(self):
        id = self.view.solicitar_id()
        
        confirmar = self.view.confirmar_eliminacion()
        
        if confirmar:
            exito = Registro_hora_dao.eliminar(id)
            
            if exito:
                self.view.mensaje("eliminacion exitosa")
            else:
                self.view.mensaje("fallo al eliminar el registro")
        else:
            self.view.mensaje("operacion cancelada")
    
    def mostrar(self):
        id = self.view.solicitar_id()
        
        register = Registro_hora_dao.obtener_por_id(id)
        
        self.view.mostrar_registro(register)
    
    def mostrar_todo(self):
        registers = Registro_hora_dao.obtener_todos()
        
        self.view.mostrar_lista(registers)
        
        