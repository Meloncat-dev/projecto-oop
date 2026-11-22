from modelos.utils import leer_numero, confirmar
from modelos.Usuario import Usuario

class Auth_view:
    
    @staticmethod
    def mostrar_banner_signup(act_try: int, max_try: int) -> None:
        print("\n" + "|" + "-"*55 + "|")
        print("|" + " "*7 + "Echo Tech Solutions: Inicio Secion" + " "*14 + "|")
        print("|" + "-"*55 + "|")
        print(" "*8 + f"Intento {act_try}/{max_try}")
        print("*"*57)

    @staticmethod
    def pedir_credenciales() -> dict:
        username = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()
        return {
            "username": username,
            "password": password
        }
    
    @staticmethod
    def mostrar_bienvenida(usuario: Usuario) -> None:
        print("\n" + "|" + "-"*65 + "|")
        print("|" + " "*4 + f"[ACCESO CONSEDIDO] Bienvenido/a, {usuario.nombre_completo}" + " "*3 + "|")
        print("|" + " "*4 + f"Usuario: {usuario.username} | Rol: {usuario.rol}" + " "*26 + "|")
        print("|" + "-"*65 + "|")
        
    @staticmethod
    def mostrar_menu_usuarios() -> int:
        print("\n" + "-"*45)
        print("   GESTION DE USUARIOS Y CREDENCIALES   ")
        print("-"*45)
        print("1.- Registrar un nuevo usuario")
        print("2.- Listar usuarios y verificar hashes")
        print("3.- Eliminar usuario")
        print("0.- Volver al menu principal")
        print("-"*45)
        return leer_numero("Seleccione una opcion: ")
    
    @staticmethod
    def formular_usuario_nuevo() -> dict:
        print("\n" + "-"*3 + "REGISTRAR USUARIO" + "-"*3)
        username = input("ingrese su nombre de usuario: ").strip()
        nombre_completo = input("ingrese su nombre real: ").strip()
        clave = input("ingrese una clave: ").strip()
        confirmacion = input("ingrese otra vez la clave: ").strip()
        
        print("---ROLES DISPONIBLES---")
        print("1. Administrador\n2. Recursos humanos\n3. Gerente\n4. Empleado(defecto)")
        opcion_rol = leer_numero("selecciona un rol(1-4)")
        mapa_roles = {1: "Administrador", 2: "Recursos humanos", 3: "Gerente", 4: "Empleado"}
        rol = mapa_roles.get(opcion_rol, "")
        
        return {
            "username": username,
            "nombre completo": nombre_completo,
            "clave": clave,
            "confirmacion": confirmacion,
            "rol": rol
        }
        
    @staticmethod
    def mostrar_lista_usuarios(users: list[Usuario]) -> None:
        print("\n---lista de usuarios registrados---")
        if not users:
            print("no hay usuarios registrados")
        else:
            for u in users:
                print(u)
        print("-"*64)
    
    @staticmethod
    def solisitar_id_usuario() -> int:
        return leer_numero("ingrese el id del usuario a eliminar: ")
    
    @staticmethod
    def confirmar_eliminacion(username: str) -> bool:
        return confirmar(f"esta seguro de eliminar al usuario '{username}'?")
    
    @staticmethod
    def msotrar_mensaje(msg: str) -> None:
        print(f"\n[AUTENTICACION]: {msg}")
        
    @staticmethod
    def mostrar_error(err: str) -> None:
        print(f"[ERROR DE CREDENCIALES]: {err}")
    