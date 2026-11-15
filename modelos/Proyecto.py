import modelos.Empleado as emp

class Proyecto:
    def __init__(self, nombre: str, presupuesto: float, fecha_inicio: str, descripcion: str, id_proyecto: int):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.fecha_inicio = fecha_inicio
        self.descripcion = descripcion
        self.id_proyecto = id_proyecto
    
    