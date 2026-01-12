import bcrypt as bc 
from direccion import Direccion

class Usuario():
    def __init__(self,usuario_id:int, nombre:str, rut:int, email:str, password_hash:str, direccion):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.password_hash = password_hash
        self.direccion = direccion
    
    def cambiar_direccion(self, nueva_direccion): # Metodo para cambiar la direccion registrada del Usuario
        if not isinstance(nueva_direccion, Direccion):
            TypeError('La instancia debe ser una Direccion')

        if self.direccion == nueva_direccion:
            return 'Los valores deben diferentes a los actuales'
        
        self.direccion == nueva_direccion

        return self.describir()
    
    def describir(self):
        return f'{self.usuario_id}, {self.nombre}, {self.rut}, {self.email}, {self.password_hash}, {self.direccion.describir_direccion()}'

class gestorUsuarios():

    def __init__(self):
        self.usuarios = [] # Lista vacia para guardar instancias de la clase Usuario

    def registrar_usuarios(self, usuario_id:int, nombre:str, rut:int, email:str, contraseña:str):
        if any(u.email == email for u in self.usuarios): # Verifica que el email no este registrado
            return "Email ya registrado"
        
        if any(u.rut == rut for u in self.usuarios):
            return "Rut ya registrado" # Verifica que el rut no este registrado
        
        if not self.validar_contraseña(contraseña):
            return "contraseña no segura" 
        
        password_hash = self.hashear_contraseña(contraseña)

        nuevo_usuario = Usuario(usuario_id, nombre, rut, email, password_hash)

        self.usuarios.append(nuevo_usuario)

        return "Usuario registrado exitosamente"

    def validar_contraseña(self, contraseña): # Valida que la contraseña cumpla con los requerimientos de contraseña segura
        return (
            len(contraseña) >= 12 and
            any(c.islower() for c in contraseña) and
            any(c.isupper() for c in contraseña) and
            any(c.isdigit() for c in contraseña) and
            any(not c.isalnum() for c in contraseña)
        )

    def hashear_contraseña(self, contraseña): # Se hashea la contraseña para una mayor seguridad
        return bc.hashpw(contraseña.encode(), bc.gensalt())

    def login(self, email, contraseña):
        pass


