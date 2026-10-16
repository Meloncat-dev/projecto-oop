from modelos import Empleado
from modelos import Proyecto

class RegistroHora:
    def __init__(self, empleado: Empleado.Empleado, proyecto: Proyecto.Proyecto, fecha: str, horas_trabajadas: float, descripcion: str, id_registro):
        self.empleado = empleado
        self.proyecto = proyecto
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion_tarea = descripcion
        self.id = id_registro