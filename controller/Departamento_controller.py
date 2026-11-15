from view.Departamento_view import Departamento_view
from modelos.Departamento_dao import Departamento_dao
from modelos.Departamento import Departamento

class Departamento_controller:
    def __init__(self):
        self.view = Departamento_view()
    
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
                    self.imprimir_dpto()
                case 5:
                    self.imprimir_todos()
                case 0:
                    self.view.mensaje("saliendo del gestor de Departamentos")
                    break
                case _:
                    self.view.mensaje("opcion invalida")
    
    def agregar(self):
        datos = self.view.formular_depto()
        try:
            nuevo_depa = Departamento(datos["nombre"])
            exito = Departamento_dao.crear(nuevo_depa)
            if exito:
                self.view.mensaje(f"departamento agregado existosamente. ID = {nuevo_depa.id_departamento}")
            else:
                self.view.mensaje("error al guardar en la base de datos")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos: {e}")
    
    def editar(self):
        id_dpto = self.view.solicitar_id()
        depa = Departamento_dao.obtener_por_id(id_dpto)
        if not depa:
            self.view.mensaje("departamento no encontrado")
            return
        
        datos = self.view.formular_edicion(depa)
        try:
            depa.nombre = datos["nombre"]
            
            exito = Departamento_dao.actualizar(depa)
            if exito:
                self.view.mensaje("se logro editar con exito el departamento")
            else:
                self.view.mensaje("fallo al editar el departamento")
        except (ValueError, TypeError) as e:
            self.view.mensaje(f"error en los datos modificados: {e}")
    
    def eliminar(self):
        id_dpto = self.view.solicitar_id()
        depa = Departamento_dao.obtener_por_id(id_dpto)
        if not depa:
            self.view.mensaje("departamento no encontrado")
            return
        
        if self.view.confirmar_eliminacion(depa.nombre):
            exito = Departamento_dao.eliminar(id_dpto)
            if exito:
                self.view.mensaje("departamento eliminado")
            else:
                self.view.mensaje("error al eliminar")
        else:
            self.view.mensaje("operacion canselada")
    
    def imprimir_dpto(self):
        id_dpto = self.view.solicitar_id()
        depa = Departamento_dao.obtener_por_id(id_dpto)
        if depa:
            self.view.mostrar_dpto(depa)
        else:
            self.view.mensaje("no se encontro el departamento")
        
    def imprimir_todos(self):
        depas = Departamento_dao.obtener_todos()
        self.view.mostrar_lista(depas)