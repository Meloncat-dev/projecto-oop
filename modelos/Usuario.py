import hashlib
import hmac
import re

class Usuario:
    
    ROLES: set[str] = {"Recursos humanos", "Administrador", "Gerente","Empleado"}

    def __init__(
            self,
            username: str,
            pass_hash: str,
            nombre_completo: str,
            rol: str = "Empleado",
            id_usuario: int | None = None
            ):
        self.id_usuario = id_usuario
        self.username = username
        self.password_hash = pass_hash
        self.nombre_completo = nombre_completo
        self.rol = rol

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, new: str) -> None:
        if not isinstance(new, str) or not new.strip():
            raise ValueError("el nombre de usuario no puede estar vacio")
        clean = new.strip().lower()

        if len(clean) < 3:
            raise ValueError("el nombre de usaurio deve ser de almenos 3 caracteres")
        if not re.match(r"^[a-zA-Z0-9_.-]+$", clean):
            raise ValueError("el nombre de usuario solo puede contener letras minusculas o mayusculas, numeros, puntos, guiones altos o bajos.")
        self._username = clean
    
    @property
    def password_hash(self) -> str:
        return self._password_hash
        
    @password_hash.setter
    def password_hash(self, new: str) -> None:
        if not isinstance(new, str) or not new.strip():
            raise ValueError("el hash de la contraseña no puede estar vacio")
        
        clean = new.strip().lower()
        
        if len(clean) != 64 or not re.match(r"^[a-f0-9]{64}$", clean):
            raise ValueError("la contraseña debe almacenarse como un hash standar SHA-256 valido de 64 caracteres HEX")
        
        self._password_hash = clean
        
    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo
    
    @nombre_completo.setter
    def nombre_completo(self, new: str) -> None:
        if not isinstance(new, str) or len(new.strip()) < 3:
            raise ValueError("el nombre completo no puede estar vacio y ebe tener minimo 3 caracteres")

        self._nombre_completo = new.strip().title()
        
    @property
    def rol(self) -> str:
        return self._rol
    
    @rol.setter
    def rol(self, new: str) -> None:
        if not isinstance(new, str) or not new.strip():
            raise ValueError("el rol del usuario no puede estar vacio")
        
        clean_rol = new.strip().capitalize()
        
        if clean_rol not in self.ROLES:
            opciones = ", ".join(sorted(self.ROLES))
            raise ValueError(f"Rol '{new}' no valido. Opcioens permitidas: {opciones}.")
        
        self._rol = clean_rol
        
    @staticmethod
    def encriptar_contra(r_pass: str) -> str:
        if not isinstance(r_pass, str) or not r_pass.strip():
            raise ValueError("la clave no puede estar vacia ni contener solo espacios")
        
        clean_pass = r_pass.strip()
        if len(clean_pass) < 4:
            raise ValueError("la contraseña debe tener almenos 4 caracteres")
        
        return hashlib.sha256(clean_pass.encode("utf-8")).hexdigest()
    
    @staticmethod
    def validar_credenciales_acceso(user: str, r_pass: str) -> tuple[bool, str]:
        if not isinstance(user, str) or not user.strip():
            return (False, "el campo 'Usuario' no puede estar vacio.")
        if not isinstance(r_pass, str) or not r_pass.strip():
            return (False, "el campo 'Clave no puede estar vacio")
        
        clean_user = user.strip()
        clean_pass = r_pass.strip()
        
        if len(clean_user) < 3:
            return (False, "nombre de usuario invalido, el nombre de usuario debe tener almenos 3 caracteres")
        
        if not re.match(r"^[a-zA-Z0-9_.-]+$", clean_user):
            return (False, "el nombre de usuario contiene caracteres invalidos.")
        
        if len(clean_pass) < 4:
            return (False, "la clave debe tener al menos 4 caracteres.")
        
        return(True, "clave y usuario en formato valido")
    
    def verificar_credenciales(self, clave: str) -> bool:
        if not isinstance(clave, str) or not clave.strip():
            return False
        try:
            hash = self.encriptar_contra(clave)
            return hmac.compare_digest(self._password_hash, hash)
        except ValueError:
            return False
            
    def __str__(self):
        id_str = self.id_usuario if self.id_usuario is not None else "Nuevo"
        hash_acortado = f"{self.password_hash[:12]}...{self.password_hash[-6:]}"
        return (
            f"username: {self.username}\n"
            f"nombre completo: {self.nombre_completo}\n"
            f"password hashed: {hash_acortado}\n"
            f"rol: {self.rol}\n"
            f"ID: {id_str}\n"
        )