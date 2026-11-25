from view.Proyecto_view import Proyecto_view
from modelos.Proyecto import Proyecto
from modelos.Proyecto_dao import Proyecto_dao
from modelos.Empleado_dao import Empleado_dao

class Proyecto_controller:
    def __init__(self):
        self.view = Proyecto_view()
    
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
                case 6:
                    self.asignar_empleado()
                case 0:
                    self.view.mensaje("saliendo del gestor de Proyectos")
                    break
                case _:
                    self.view.mensaje("opcion invalida")
                    
    def agregar(self):
        datos = self.view.formular_proyecto()
        
        try:
            proy = Proyecto(
                datos["nombre"],
                datos["presupuesto"],
                datos["fecha inicio"],
                datos["descripcion"]
            )
            
            exito = Proyecto_dao.crear(proy)
            
            if exito:
                self.view.mensaje("proyecto creado con exito")
            else:
                self.view.mensaje("fallo al crear el proyecto")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos: {e}")
            
    def editar(self):
        id = self.view.solicitar_id()
        
        proy = Proyecto_dao.obtener_por_id(id)
        
        datos = self.view.formular_edicion(proy)
        
        try:
            proy.nombre = datos["nombre"]
            proy.presupuesto = datos["presupuesto"]
            proy.fecha_inicio = datos["fecha"]
            proy.descripcion = datos["descripcion"]
            
            exito = Proyecto_dao.actualizar(proy)
            
            if exito:
                self.view.mensaje("edicion exitosa")
            else:
                self.view.mensaje("fallo al editar")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos")
            
    def eliminar(self):
        id = self.view.solicitar_id()
        
        proy = Proyecto_dao.obtener_por_id(id)
        
        confirmacion = self.view.confirmar_eliminacion(proy)
        
        if confirmacion:
            exito = Proyecto_dao.eliminar(id)
            
            if exito:
                self.view.mensaje("proyecto eliminado con exito")
            else:
                self.view.mensaje("fallo al eliminar el proyecto")
        else:
            self.view.mensaje("operacion cancelada")
    
    def imprimir_uno(self):
        id = self.view.solicitar_id()
        
        proy = Proyecto_dao.obtener_por_id(id)
        
        self.view.mostrar_proyecto(proy)
        
    def imprimir_todo(self):
        proys = Proyecto_dao.obtener_todos()
        
        self.view.mostrar_lista(proys)
        
    def asignar_empleado(self):
        id_proy = self.view.solicitar_id()
        proy = Proyecto_dao.obtener_por_id(id_proy)
        if not proy:
            self.view.mensaje("no existe el proyecto")
            return
        
        id_emp = self.view.solicitar_id()
        empleado = Empleado_dao.obtener_por_id(id_emp)
        if not empleado:
            self.view.mensaje("no existe el empleado")
            return
        
        exito = Proyecto_dao.asignar_empleado(empleado, proy)
        
        if exito:
            self.view.mensaje("asignacion de empleado exitosa")
        else:
            self.view.mensaje("fallo al asignar al empleado")
            
        
    