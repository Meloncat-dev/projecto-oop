from modelos import Departamento

class Empleado:
    MAILPROV = ["gmail.com", "outlook.com", "yahoo.com"]
    def __init__(self, nombre: str, rut: str, email: str, id_empleado: int, departamento: Departamento.Departamento | None = None):
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.departamento = departamento
        
        if not isinstance(id_empleado, int) or isinstance(id_empleado, bool):
            raise TypeError("el id debe ser un numero entero")
        
        self.id_empleado = id_empleado

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new: str):
        if not isinstance(new, str) or len(new.strip()) < 3:
            raise ValueError("el nombre debe tener minimo 3 letras")
        
        self._nombre = new.strip().title()
    
    @property
    def rut(self):
        return self._rut
    
    @rut.setter
    def rut(self, new: str):
        if not isinstance(new, str) or not new.strip():
            raise ValueError("no puede estar vacio")
        
        self._rut = new.strip().upper()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new: str):
        
        if not isinstance(new, str) or not new.strip():
            raise ValueError("el email no puede estar vacio")
        
        part = new.strip().split("@")
        
        if len(part) != 2 or not part[0] or part[1] not in self.MAILPROV:
            raise ValueError(f"el email no puede estar vacio y debe contener una de las siguientes {self.MAILPROV}")
        
        self._email = new.strip()
    
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, new: Departamento.Departamento | None):
        if new is not None and not isinstance(new, Departamento.Departamento):
            raise TypeError("debe ser instancia de departamento")
        
        self._departamento = new
