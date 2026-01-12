from enum import Enum
from carrito_detalle import CarritoDetalle

class estadoCarrito(Enum): # Define el estado del carrito
    ACTIVO = 1
    INACTIVO = 0

class Carrito(): # Entidad ya que posee un ser, un ID 
    def __init__(self, carrito_id, catalogo_productos):
        self.carrito_id = carrito_id
        self.catalogo = catalogo_productos
        self.estado = estadoCarrito.ACTIVO
        self.items = [] #lista vacía 


    def _validar_activo(self):
        if self.estado != estadoCarrito.ACTIVO:
            raise Exception('El carrito no esta activo')

    def agregarProducto(self, nombre_producto: str, cantidad:int):
        self._validar_activo() # Validamos si el carrito esta activo
        
        if nombre_producto not in self.catalogo: # Verifica que el producto se encuentre en el catalogo
            raise Exception('Producto no existe')
        
        if cantidad <= 0: # Verifica que la cantidad ingresada de productos es mayor a cero
            raise Exception('La cantidad debe ser mayor a cero')

        producto = self.catalogo[nombre_producto]

        self.items.append(CarritoDetalle(producto, cantidad))

        return f'{nombre_producto} x {cantidad} agregado al carrito'
    
    def eliminarProducto(self, nombre_producto: str):
        self._validar_activo() # Validamos si el carrito esta activo
        
        for i, item in enumerate(self.items): 
            if item.producto.nombre == nombre_producto:
                self.items.pop(i)
                return f'Producto: {nombre_producto} eliminado del carrito'
        
        raise Exception('Producto no encontrado')

    def editarProducto(self, nombre_producto, cantidad):
        self._validar_activo() # Validamos si el carrito esta activo
        
        if cantidad <= 0:
            raise Exception('La cantidad debe ser mayor a cero') # Verificamos que la edición de la cantidad sea mayor a cero
        
        for item in self.items:
            if item.producto.nombre == nombre_producto:
                item.cantidad = cantidad
                return f'Producto: {nombre_producto} - Cantidad modificada: {cantidad}'
        
        raise Exception('Producto no encontrado')
    
    def VerificarStock(self):
        pass

    def obtenerItems(self):
        return self.items
    




