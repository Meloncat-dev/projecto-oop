from modelos import Empleado

class Departamento:
    def __init__(self, nombre: str, id_departamento: int | None = None):
        self.nombre = nombre
        self.id_departamento = id_departamento
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, new: str):
        if not isinstance(new, str) or len(new.strip()) < 3:
            raise ValueError("el nombre debe tener minimo 3 caracteres")
        
        self._nombre = new
    
    def __str__(self) -> str:
        return (f"nombre: {self.nombre} \n"
        f"ID: {self.id_departamento}"
        )
    