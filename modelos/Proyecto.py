import modelos.Empleado as emp

class Proyecto:
    def __init__(self, nombre: str, presupuesto: float, fecha_inicio: str, id_proyecto: str):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.fecha_inicio = fecha_inicio
        self.equipo: list[emp.Empleado] = []
        self.id_proyecto = id_proyecto
    
    