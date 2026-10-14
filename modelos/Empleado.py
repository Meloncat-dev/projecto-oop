from modelos import Departamento

class Empleado:
    def __init__(self, nombre: str, rut: str, email: str, id_empleado: int, departamento: Departamento.Departamento | None = None):
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.departamento = departamento
        self.id_empleado = id_empleado

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new: str):
        self._nombre = new
    
    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self, new: str):
        self._rut = new
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new: str):
        self.email = new
    
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, new: Departamento.Departamento):
        self._departamento = new
    
    