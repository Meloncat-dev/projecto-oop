class Departamento:
    def __init__(self, nombre: str, id_departamento: int | None = None):
        self.nombre = nombre
        self.empleados = []
        self.id_departamento = id_departamento
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new: str):
        self._nombre = new
    