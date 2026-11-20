import hashlib
import hmac
import re

class Usuario:

    def __init__(
            self,
            username: str,
            pass_hash: str,
            nombre_completo: str,
            rol: str = "Operador",
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