""" Agregado de la entidad Usuario (value object). 

Por composición se crea una clase Direccion para separar los atributos de la clase Usuario.

Solo a través de la clase Usuario se pueden realizar los cambios en los atributos de la clase Direccion cumpliendo con el paradigma
de programación raiz agregada (aggregate root)"""

class Direccion: 
    def __init__(self, calle: str, numero: int, ciudad: str, comuna: str, codigo_postal:int):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.comuna = comuna
        self.codigo_postal = codigo_postal

    def __eq__(self, value): # Metodo mágico. Compara los atributos para saber si son iguales en valor.
        if not isinstance(value, Direccion):
            return NotImplemented
        
        return(
            value.calle == self.calle and
            value.numero == self.calle and 
            value.ciudad == self.ciudad and
            value.comuna == self.comuna and
            value.codigo_postal == self.codigo_postal
        )
        
    def describir_direccion(self):
        return f'Direccion: {self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.codigo_postal}'
    
class GestorDirecciones:
    def __init__(self):
        self._direcciones = []
        pass 




