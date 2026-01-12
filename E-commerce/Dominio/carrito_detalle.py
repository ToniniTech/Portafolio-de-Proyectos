
class CarritoDetalle():
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        
    def CalcularSubTotal(self):
        return self.producto.precio * self.cantidad
    
    def CalcularTotal(self, envios, impuestos):
        return (self.producto.precio * self.cantidad) + envios + impuestos

    def CalcularEnvio(self):
        pass

    def CalcularImpuestos(self):
        pass    

    def AplicarDescuentos(self):
        pass

    def ObtenerItems(self):
        pass

    
