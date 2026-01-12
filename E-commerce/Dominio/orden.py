class Orden():
    def __init__(self, orden_id, fecha_compra, total, estado):
        self.orden_id = orden_id
        self.fecha_compra = fecha_compra
        self.total = total
        self.estado = estado

class detalleOrden():
    def __init__(self, detalle_id, cantidad, precio_unitario, subtotal):
        self.detalle_id = detalle_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

