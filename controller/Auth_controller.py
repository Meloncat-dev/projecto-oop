from config.settings import Settings
from modelos.Usuario import Usuario
from modelos.Usuario_dao import UsuarioDAO
from view.Auth_view import Auth_view

class Auth_controller:
    
    def __init__(self):
        self.view = Auth_view()
        
    def iniciar_secion(self) -> Usuario:
        UsuarioDAO.inicializar_admin_por_defecto()
        max_intentos = Settings.MAX_LOGIN_ATTEMPTS
        
        for intento in range(1, max_intentos + 1):
            self.view.mostrar_banner_signup(intento, max_intentos)
            credenciales = self.view.pedir_credenciales()
            username = credenciales["username"]
            clave = credenciales["password"]
            
            valid, msg_valid = Usuario.validar_credenciales_acceso(username, clave)
            if not valid:
                self.view.mostrar_error(f"Validacion fallida: {msg_valid}")
                continue
            
            usuario_bd = UsuarioDAO.obtener_por_username(username)
            if usuario_bd is not None and usuario_bd.verificar_credenciales(clave):
                self.view.mostrar_bienvenida(usuario_bd)
                return usuario_bd
            
            self.view.mostrar_error(
                "Credenciales incorrectas: contraseña incorrecta o usuario inexistente"
            )
        self.view.mostrar_error(
            f"ah superado el limite de intentos ({max_intentos})"
            "Acceso bloqueado por seguridad"
        )
        return None
    
    def ejecutar(self, usuario_actual: Usuario | None = None) -> None:
        while True:
            op = self.view.mostrar_menu_usuarios()
            match op:
                case 1:
                    self.registrar_user()
                case 2:
                    self.listar_usuarios()
                case 3:
                    self.eliminar_user()
                case 0:
                    self.view.msotrar_mensaje("volviendo al menu principal")
                    break
                case _:
                    self.view.mostrar_error("opcion invalida")
    
    def registrar_user(self) -> None:
        datos = self.view.formular_usuario_nuevo()
        
        valid, msg_valid = Usuario.validar_credenciales_acceso(datos["username"], datos["clave"])
        
        if not valid:
            self.view.mostrar_error(msg_valid)
            return
        
        if not datos["nombre completo"]:
            self.view.mostrar_error("el nomre completo no puede estar vacio")
            return
        
        if datos["clave"] != datos["confirmacion"]:
            self.view.mostrar_error("las contraseñas ingresadas no coinciden")
            return
        
        try:
            password_encript = Usuario.encriptar_contra(datos["clave"])
            nw_user = Usuario(
                username= datos["username"],
                pass_hash= password_encript,
                nombre_completo= datos["nombre completo"],
                rol= datos["rol"]
            )
            
            if UsuarioDAO.crear(nw_user):
                self.view.msotrar_mensaje(
                    f"Usuario '{nw_user.username}' registrado exitosamente"
                )
            else:
                self.view.mostrar_error("no fue posible guardar el usuario en la base de datos")
        except (ValueError, TypeError) as e:
            self.view.mostrar_error(f"datos invalidos: {e}")
    
    def listar_usuarios(self) -> None:
        usuarios = UsuarioDAO.obtener_todos()
        self.view.mostrar_lista_usuarios(usuarios)
        
    def eliminar_user(self, user_act: Usuario | None = None) -> None:
        id_usuario = self.view.solisitar_id_usuario()
        usuario = UsuarioDAO.obtener_por_id(id_usuario)
        
        if not usuario:
            self.view.mostrar_error("usuario no encontrado")
            return
        
        if user_act and usuario.id_usuario == user_act.id_usuario:
            self.view.mostrar_error("no puedes eliminar tu usuario mientras estas con la sesion iniciada")
            return
        
        if self.view.confirmar_eliminacion(usuario.username):
            if UsuarioDAO.eliminar(id_usuario):
                self.view.mostrar_error(f"Usuario '{usuario.username}' eliminado exitosamente")
            else:
                self.view.mostrar_error("error al eliminar al usuario en la base de datos")
        else:
            self.view.msotrar_mensaje("operacion canselada")
