from modelos import Empleado

class Departamento:
    def __init__(self, nombre: str, id_departamento: int | None = None):
        self.nombre = nombre
        self.empleados: list[Empleado.Empleado] = []
        self.id_departamento = id_departamento
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, new: str):
        self._nombre = new
    
    def __str__(self) -> str:
        empleados_str = ", ".join(
            empleado.nombre
            for empleado in self.empleados
        )
        return (f"nombre: {self.nombre} \n"
        f"empleados: {empleados_str} \n"
        f"ID: {self.id_departamento}"
        )
    