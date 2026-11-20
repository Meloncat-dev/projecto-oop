from modelos import Empleado
from modelos import Proyecto

class RegistroHora:
    def __init__(self, empleado: Empleado.Empleado, proyecto: Proyecto.Proyecto, fecha: str, horas_trabajadas: float, descripcion: str, id_registro: int):
        self.empleado = empleado
        self.proyecto = proyecto
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion_tarea = descripcion
        self.id = id_registro
    
    def __str__(self):
        print(
            f"empleado: {self.empleado.nombre}"
            f"proyecto: {self.proyecto.nombre}"
            f"fecha: {self.fecha}"
            f"horas_trabajadas: {self.descripcion_tarea}"
            f"descripcion: {self.descripcion_tarea}"
            f"ID: {self.id}"
        )
        