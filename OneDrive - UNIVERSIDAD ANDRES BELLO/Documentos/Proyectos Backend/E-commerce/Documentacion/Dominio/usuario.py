import bcrypt as bc 
from direccion import Direccion

class Usuario():
    def __init__(self,usuario_id:int, nombre:str, rut:int, email:str, contraseña:str, direccion):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.contraseña = contraseña
        self.direccion = direccion
    
    def cambiar_direccion(self, nueva_direccion): # Metodo para cambiar la direccion registrada del Usuario
        if not isinstance(nueva_direccion, Direccion):
            TypeError('La instancia debe ser una Direccion')

        if self.direccion == nueva_direccion:
            raise Exception('Los valores deben ser diferentes a los actuales')

        self.direccion = nueva_direccion

class gestorUsuarios:

    def __init__(self):
        self.usuarios = []
        pass # Lista vacia para guardar instancias de la clase Usuario

    def registrar_usuarios(self, usuario_id:int, nombre:str, rut:int, email:str, contraseña:str, direccion):
        if any(u.email == email for u in self.usuarios): # Verifica que el email no este registrado
            return "Email ya registrado"
        
        if any(u.rut == rut for u in self.usuarios):
            return "Rut ya registrado" # Verifica que el rut no este registrado
        
        if not self.validar_contraseña(contraseña):
            return "Contraseña no segura" 
        
        password_hash = self.hashear_contraseña(contraseña)

        nuevo_usuario = Usuario(usuario_id, nombre, rut, email, password_hash, direccion)

        self.usuarios.append(nuevo_usuario)

        return "Usuario registrado exitosamente"

    def buscar_usuario(self, usuario_id):
        return next((u for u in self.usuarios if u.usuario_id == usuario_id), None)
    
    def editar_direccion(self, usuario_id, nueva_direccion):
        usuario = self.buscar_usuario(usuario_id)

        if not usuario:
            return 'Usuario no encontrado'
        
        return usuario.cambiar_direccion(nueva_direccion)

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
    
    def describir_usuario(self):  
        return [u.describir() for u in self.usuarios]
            
    def login(self, email, contraseña):
        pass

    
    def describir(self):
        return (
            f"{self.usuario_id}, {self.nombre}, {self.rut}, {self.email}, {self.password_hash}, "
            f"{self.direccion.calle}, {self.direccion.numero}, {self.direccion.ciudad}, "
            f"{self.direccion.comuna}, {self.direccion.codigo_postal}"
        )


direccion1 = Direccion('Curiñanca', 730, 'San Miguel', 'Santiago', 8009000)
direccion2 = Direccion('Cuadro verde', 1223, 'Estacion central', 'Santiago', 5900700)
direccion3 = Direccion('Cuadro verde', 1223, 'Estacion central', 'Santiago', 5900700)
direccion4 = Direccion('Ingeniero Pedro Gallo', 101, 'Maipu', 'Santiago', 59007400)



print('---- Prueba funcional ----\n')
"Requisitos contraseña"
"Debe tener 12 o más caracteres,"
"Debe tener al menos una mayuscula"
"Debe tener al menos una miniscula"
"Debe tener al menos un caracteres especial"

gestor = gestorUsuarios()
usuario1 = gestor.registrar_usuarios(2, 'Camila Zapata', 195683655, 'czignacia@gmail.com', 'Ant563852458**', direccion2)
usuario2 = gestor.registrar_usuarios(3, 'Anthony Viveros', 269323000, 'tony@gmail.com', 'Cz123455656**', direccion1)
print(usuario1)
print(usuario2)


usuario1 = gestor.editar_direccion(2, direccion4)
lista_usuarios = gestor.describir_usuario()
print(lista_usuarios)





'''print(usuario2.describir())
print(usuario2.cambiar_direccion(direccion1))
print(usuario1.describir())
print(usuario1.cambiar_direccion(direccion4))'''